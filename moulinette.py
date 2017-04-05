#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask
import json
from random import randrange
import psycopg2


app = Flask(__name__)

@app.route('/')

# def departement():
# 	try:
# 		dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
# 		dbcur = dbcon.cursor()
# 		dbcur.execute("SELECT nom_departement FROM test ORDER BY random() LIMIT 20")
# 		departements = dbcur.fetchall()
# 	except:
# 		return "département() ne fonctionne pas"

# def mauvrep():
	# def qui genère des réponse aléatoire en fonction de la colonne de la question

def moulinette():
	try:
		dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
		dbcur = dbcon.cursor()
		dbcur.execute("CREATE TEMP TABLE departement AS SELECT DISTINCT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM test")
		dbcur.execute("SELECT nom_region,chef_lieu,num_departement,nom_departement,prefecture FROM departement ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		i = randrange(8)
		moulinette = []
		for i in range(0,len(datas)): # i est compris entre 0 et 20
			try:
				for data in datas:
					modeles = { 
					0 : ('Quel est le numéro du département ' + data[3] + ' ?', str(data[2])),
					1 : ('Quel est le département qui a pour numéro ' + data[3] + ' ?', str(data[2])),
					2 : ('Quelle est la préfecture du département ' + data[3] + ' ?', str(data[4])),
					3 : (data[4] + ' est la préfecture de quel département ?', str(data[3])),
					4 : ('Dans quel département se trouve la préfecture de ' + data[4] + ' ?', str(data[3])),
					5 : ('Dans quelle région se trouve le département ' + data[3] + ' ?', str(data[0])),
					6 : (data[3] + ' est un département. Dans quelle région se trouve-t-il ?', str(data[0])),
					7 : ('Quel est le chef-lieu de la région' + data[0] + '?', str(data[1]))
					}
					moulinette.append(modeles[i])
					i = randrange(8)
				return str(moulinette)
				#On utilise la méthode dump pour enregistrer l'objet.
			except:
				return "La fonction for ne fonctionne pas"
	except:
		return " connexion au serveur a échoué" 

app.run(host='0.0.0.0', port=11002)





