#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask, session, redirect, url_for, escape, request
from flask_cors import CORS, cross_origin
import json
from random import randrange
import psycopg2
import random
<<<<<<< HEAD

=======
>>>>>>> origin

app = Flask(__name__)
app.secret_key = 'super secret key'
CORS(app)

modeles = {
	0 :{
	"question" : 'Quel est le numéro du département %s ?',
	#%s = data[modeles[i]['question_index']]
	"question_index": 3,
	#l'indice de la colonne ou l'on va chercher le nom_departement dans la BDD
	"propositions_colonne": "num_departement",
	#on prépare num_departement pour lancer fonction mauvaises_rep
	"reponse_index" : 2
	#
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
dbcur.execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")
<<<<<<< HEAD
	
@app.route('/', methods=['GET', 'POST'])
=======

def mauvaises_rep(colonne, br):

	try:
		dbcur.execute("SELECT DISTINCT " + colonne + ", random() FROM departement WHERE " + colonne + " <> %s ORDER BY random() LIMIT 2", [br])
		#SELECT DISTINCT nom_region, random() FROM departement WHERE nom_region <> 'Bretagne' ORDER BY random() LIMIT 3;
		mauvaises_reponses = dbcur.fetchall()
		return rand_rep(str(br), str(mauvaises_reponses[0][0]), str(mauvaises_reponses[1][0]))
	
	except Exception as e:
		print e.message, e.args
		return ""

def rand_rep(br, prop1, prop2):

	try:
		# recuperer les 3 propositions dans un tab
		tab = [br, prop1, prop2]
		 # melanger le tab
		random.shuffle(tab)
		# retourner les propositions
		return tab

	except Exception as e:
		print e.message, e.args
		return ""

# def check (reponse_user, reponse):

# 	try:
# 		return reponse_user 
# 	except Exception as e:
# 		print e.message, e.args
	
@app.route('/')
>>>>>>> origin
def moulinette():

	try:
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		i = randrange(8)
		reponse = []
		moulinette = []
		for data in datas:
			moulinette.append({
				"question": modeles[i]['question'] % (data[modeles[i]['question_index']]),
				#on pose la question de l'indice i où %s = data[0][3]
				"propositions": mauvaises_rep(modeles[i]['propositions_colonne'], data[modeles[i]['reponse_index']]),
				#"propositions" = mauvaises_rep('nom_region', 1) 
				#on donne le nom de la colonne de la rep qu'on veut et l'indice dans lequel on veut trouver la réponse
				#"reponse": data[modeles[i]['reponse_index']]
				})
			reponse.append(data[modeles[i]['reponse_index']])
			i = randrange(8)
		#session['moulinette'] = moulinette
		session['reponse'] = reponse
		return json.dumps(moulinette, indent = 4)
		#return str(session['moulinette'])
		#return str(session['reponse'])

	except Exception as e:
		print e.message, e.args
		return ""

def mauvaises_rep(colonne, br):
	try:
		dbcur.execute("SELECT DISTINCT " + colonne + ", random() FROM departement WHERE " + colonne + " <> %s ORDER BY random() LIMIT 2", [br])
		#SELECT DISTINCT nom_region, random() FROM departement WHERE nom_region <> 'Bretagne' ORDER BY random() LIMIT 3;
		mauvaises_reponses = dbcur.fetchall()
		return rand_rep(str(br), str(mauvaises_reponses[0][0]), str(mauvaises_reponses[1][0]))
	
	except Exception as e:
		print e.message, e.args
		return ""

def rand_rep(br, prop1, prop2):
	try:
		# recuperer les 3 propositions dans un tab
		tab = [br, prop1, prop2]
		 # melanger le tab
		random.shuffle(tab)
		# retourner les propositions
		return tab

	except Exception as e:
		print e.message, e.args
		return ""
<<<<<<< HEAD

@app.route('/check', methods=['POST'])
def check():
	try:
		if request.method == 'POST':
			reponse_user = request.form['reponse'] #'Bourgogne'
			indice_question = request.form['question'] #14
			print session

			#reponse ('reponse',)

			return "try session['reponse'] "
			# if (reponse_user == str(session['reponse'][indice_question])):
			# 	return "True"
			# else:
			# 	return "False"
	except Exception as e:
		print e.message, e.args
		return "la fct check ne fonctionne pas"

if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'

	sess.init_app(app)

app.run(host='0.0.0.0', port=11001)


=======

app.run(host='0.0.0.0', port=11011)
>>>>>>> origin
