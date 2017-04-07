#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask
import json
from random import randrange
import psycopg2


app = Flask(__name__)

dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')

def mauvaises_rep(colonne, br):
	try:
		dbcur = dbcon.cursor()
		dbcur.execute("SELECT " + colonne + " FROM departement WHERE " + colonne + " <> '" + br + "' ORDER BY random() LIMIT 3")
		#dbcur.execute("SELECT prefecture FROM departement WHERE prefecture <> ' avignon ' ORDER BY random() LIMIT 2")
		#SELECT prefecture FROM departement WHERE prefecture <> 'Avignon' ORDER BY random() LIMIT 3;
		mauvaises_reponses = dbcur.fetchall()
		# str(mauvaises_reponses) = [ "Orne, Rh\u00f4ne, Bouches-du-Rh\u00f4ne" ]
		#["bourgogne","FC"]
		return [str(mauvaises_reponses[0][0]), str(mauvaises_reponses[1][0]), str(mauvaises_reponses[2][0])]

	except:
		return "La fonction mauvaises_rep ne fonctionne pas"

@app.route('/')
def moulinette():
	try:
		dbcur = dbcon.cursor()
		dbcur.execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		i = randrange(8)
		moulinette = []
		questions = {}
		for data in datas:
			modeles = {
			0 :[{
			"question" : 'Quel est le numéro du département ' + data[3] + ' ?',
			"propositions" : mauvaises_rep("num_departement", data[2]),
			"reponse" : str(data[2])
			}],
			1 :[{
			"question" : 'Quel est le département qui a pour numéro ' + data[2] + ' ?',
			"propositions" : mauvaises_rep("nom_departement", data[3]),
			"reponse" : str(data[3])
			}],
			2 :[{
			"question" : 'Quelle est la préfecture du département ' + data[3] + ' ?',
			"propositions" :  mauvaises_rep("prefecture", data[4]),
			"reponse" : str(data[4])
			}],
			3 :[{
			"question" : data[4] + ' est la préfecture de quel département ?',
			"propositions" :  mauvaises_rep("nom_departement", data[3]),
			"reponse" : str(data[3])
			}],
			4 :[{
			"question" : 'Dans quel département se trouve la préfecture de ' + data[4] + ' ?',
			"propositions" :  mauvaises_rep("num_departement", data[3]),
			"reponse" : str(data[3])
			}],
			5 :[{
			"question" : 'Dans quelle région se trouve le département ' + data[3] + ' ?',
			"propositions" :  mauvaises_rep("nom_region", data[0]),
			"reponse" : str(data[0])
			}],
			6 :[{
			"question" : data[3] + ' est un département. Quand quelle région se trouve-t-il ?',
			"propositions" :  mauvaises_rep("nom_region", data[0]),
			"reponse" : str(data[0])
			}],
			7 :[{
			"question" : 'Quel est le chef-lieu de la région' + data[0] + '?',
			"propositions" :  mauvaises_rep("chef_lieu", data[1]),
			"reponse" : str(data[1])
			}],
			}
			moulinette.append(modeles[i])
			i = randrange(8)
		questions = {"moulinette" : moulinette}
		return json.dumps(questions, indent = 4)
	except:
		return " connexion au serveur a échoué"

app.run(host='0.0.0.0', port=11001)
