#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask, session, request
from flask_cors import CORS, cross_origin
import json
from random import randrange
import psycopg2
import random

app = Flask(__name__)
app.secret_key = "u74*^`LS9>R2{SW"
CORS(app, supports_credentials = True)

modeles = {
	0 :{
	"question" : 'Quel est le numéro du département %s ?',
	"question_index": 3,
	"propositions_colonne": "num_departement",
	"reponse_index" : 2
	},
	1 :{
	"question" : 'Quel est le département qui a pour numéro %s ?',
	"question_index": 2,
	"propositions_colonne": "num_departement",
	"reponse_index" : 3
	},
	2 :{
	"question" : 'Quelle est la préfecture du département %s ?',
	"question_index": 3,
	"propositions_colonne": "prefecture",
	"reponse_index" : 4
	},
	3 :{
	"question" : '%s est la préfecture de quel département ?',
	"question_index": 4, 
	"propositions_colonne": "nom_departement",
	"reponse_index" : 3
	},
	4 :{
	"question" : 'Dans quel département se trouve la préfecture de %s ?',
	"question_index": 4, 
	"propositions_colonne": "nom_departement",
	"reponse_index" : 3
	},
	5 :{
	"question" : 'Dans quelle région se trouve le département %s ?',
	"question_index": 3, 
	"propositions_colonne": "nom_region",
	"reponse_index" : 0
	},
	6 :{
	"question" : ' %s est un département. Dans quelle région se trouve-t-il ?',
	"question_index": 3, 
	"propositions_colonne": "nom_region",
	"reponse_index" : 0
	},
	7 :{
	"question" : 'Quel est le chef-lieu de la région %s ?',
	"question_index": 0, 
	"propositions_colonne": "chef_lieu",
	"reponse_index" : 1
	}
	}

dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
dbcur = dbcon.cursor()
dbcur.execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")

def mauvaises_rep(colonne, br):

	try:
		dbcur.execute("SELECT DISTINCT " + colonne + ", random() FROM departement WHERE " + colonne + " <> %s ORDER BY random() LIMIT 2", [br])
		#SELECT DISTINCT nom_region, random() FROM departement WHERE nom_region <> 'Bretagne' ORDER BY random() LIMIT 3;
		mauvaises_reponses = dbcur.fetchall()
		propositions = [str(br), mauvaises_reponses[0][0], mauvaises_reponses[1][0]]
		random.shuffle(propositions)
		return propositions
	
	except Exception as e:
		print (e.message, e.args)
		return ""
	
@app.route('/', methods=['GET'])
def moulinette():

	try:
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		i = randrange(8)
		session['reponses'] = []
		moulinette = []
		for data in datas:
			moulinette.append({
			"question": modeles[i]['question'] % (data[modeles[i]['question_index']]),
			"propositions": mauvaises_rep(modeles[i]['propositions_colonne'], data[modeles[i]['reponse_index']]),
			})
			session['reponses'].append(data[modeles[i]['reponse_index']])
			i = randrange(8)
		return json.dumps(moulinette, indent = 4)

	except:
		return ""

@app.route('/check', methods = ['POST', 'GET'])
def check():
	if request.method == 'POST':
		boolean = str(str(request.form['reponse']) == str(session['reponses'][int(request.form['question'])]))
		print(request.form['reponse'])
		print(str(session['reponses'][int(request.form['question'])]))
		return boolean

if __name__ == '__main__':
	app.debug = True
	SESSION_TYPE = 'filesystem'

app.run(host='0.0.0.0', port=11001)
