#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask
from flask_cors import CORS, cross_origin
import json
from random import randrange
import psycopg2

app = Flask(__name__)
CORS(app)

modeles = {
	0 :{
	"question" : 'Quel est le numéro du département %s ?',
	"question_index": 3,
	"propositions_colonne": "num_departement",
	"reponse_index" : 2
	},
	1 :{
	"question" : 'Quel est le département qui a pour numéro %s ?',
	"question_index": 3,
	"propositions_colonne": "num_departement",
	"reponse_index" : 2
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
	"question" : ' %s est un département. Quand quelle région se trouve-t-il ?',
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

def mauvaises_rep(colonne, br):

	try:
		dbcur.execute("SELECT DISTINCT " + colonne + ", random() FROM departement WHERE " + colonne + " <> %s ORDER BY random() LIMIT 3", [br])
		mauvaises_reponses = dbcur.fetchall()
		return [str(mauvaises_reponses[0][0]), str(mauvaises_reponses[1][0]), str(mauvaises_reponses[2][0])]
	
	except Exception as e:
		print e.message, e.args

def check (reponse_user, reponse):

	try:
		return reponse_user
	except Exception as e:

		print e.message, e.args
	
@app.route('/')
def moulinette():

	try:
		dbcur.execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		i = randrange(8)
		moulinette = []
		for data in datas:
			moulinette.append({
				"question": modeles[i]['question'] % (data[modeles[i]['question_index']]),
				"propositions": mauvaises_rep(modeles[i]['propositions_colonne'], data[modeles[i]['reponse_index']]),
				"reponse": data[modeles[i]['reponse_index']]})
			i = randrange(8)
		return json.dumps(moulinette, indent = 4)

	except Exception as e:
		print e.message, e.args

app.run(host='0.0.0.0', port=11001)
