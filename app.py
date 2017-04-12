#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask, session, request
from flask_cors import CORS
from random import randrange, shuffle
import json
import psycopg2

app = Flask(__name__)
app.secret_key = "u74*^`LS9>R2{SW"
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
	"propositions_table": "region",
	"reponse_index" : 0
	},
	6 :{
	"question" : ' %s est un département. Quand quelle région se trouve-t-il ?',
	"question_index": 3, 
	"propositions_colonne": "nom_region",
	"propositions_table": "region",
	"reponse_index" : 0
	},
	7 :{
	"question" : 'Quel est le chef-lieu de la région %s ?',
	"question_index": 0, 
	"propositions_colonne": "chef_lieu",
	"propositions_table": "region",
	"reponse_index" : 1
	}
}

def getdbcursor():
	if not 'dbcur' in session:
		dbcon = psycopg2.connect('host=localhost port=5432 dbname=geoquizz user=geodds password=acsdds')
		dbcon.autocommit = True
		session['dbcur'] = dbcon.cursor()
		session['dbcur'].execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")
		session['dbcur'].execute("CREATE TEMP TABLE region AS SELECT DISTINCT nom_region,chef_lieu FROM test")
	return session['dbcur']

def destroycursor():
	session.pop('dbcur')

def creerquestion(data):
	modele = modeles[randrange(len(modeles))]
	marqueur = data[modele['question_index']]
	reponse = data[modele['reponse_index']]
	session['reponses'].append(reponse)
	return {
		"question": modele['question'] % marqueur,
		"propositions": getprops(reponse, modele)
	}

def getprops(reponse, modele):
	try:
		dbcur = getdbcursor()
		if not "propositions_table" in modele:
			modele["propositions_table"] = "departement"
		table = modele["propositions_table"]
		colonne = modele["propositions_colonne"]
		dbcur.execute("SELECT " + colonne + " FROM " + table + " WHERE " + colonne + " <> %s ORDER BY random() LIMIT 3", [reponse])
		props = map(lambda a: a[0], dbcur.fetchall()) + [reponse]
		shuffle(props)
		return props
	except Exception as e:
		print(e)
		return "Erreur lors de la génération des propositions"

@app.route('/init', methods=['GET'])
def moulinette():
	try:
		dbcur = getdbcursor()
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		lignes = dbcur.fetchall()
		questions = []
		session['reponses'] = []
		for ligne in lignes:
			questions.append(creerquestion(ligne))
		destroycursor()
		return json.dumps(questions, indent = 4)
	except Exception as e:
		print(e)
		return "Erreur lors de la connexion à la base de données, merci de réessayer plus tard"

@app.route('/check', methods=['GET', 'POST'])
def check():
	if request.method == 'GET':
		print request
	return str(request.args.get('reponse') == session['reponses'][int(request.args.get('question'))])



if __name__ == '__main__':
	app.debug = True

app.run(host='0.0.0.0', port=11010)


