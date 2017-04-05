#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask, request
import json
from random import randrange
import psycopg2


app = Flask(__name__)


@app.route('/')
def index():
	try:
		dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
		dbcur = dbcon.cursor()
		dbcur.execute("SELECT * FROM test ORDER BY random() LIMIT 20")
		datas = dbcur.fetchall()
		moulinette = []
		QR = {}
		i = randrange(8)
		for i in range(0,len(datas)): # i est compris entre 0 et 20
			try:
				for data in datas:
					modeles = {
					0 : {'Quel est le numéro du département ' + data[4] + ' ?': {str(data[3]) : str(data[3]), str(data[3])}},
					1 : {'Quel est le département qui à pour numéro ' + data[3] + ' ?': {str(data[4]) : str(data[4]), str(data[4])}},
					2 : {'Quelle est la préfecture du département ' + data[4] + ' ?' : {str(data[5]) : str(data[5]), str(data[5])}},
					3 : {data[5] + ' est la préfecture de quel département ?': {str(data[4]) : str(data[4]), str(data[4])}},
					4 : {'Dans quel département se trouve la préfecture de ' + data[5] + ' ?': {str(data[4]) : str(data[4]), str(data[4])}},
					5 : {'Dans quelle région se trouve le département ' + data[4] + ' ?': {str(data[1]) : str(data[1]), str(data[1])}},
					6 : {data[4] + ' est un département. Quand quelle région se trouve-t-il ?': {str(data[1]) : str(data[1]), str(data[1])}},
					7 : {'Quel est le chef-lieu de la région' + data[1] + '?': {str(data[2]) : str(data[2]), str(data[2])}}
					}
					moulinette.append(modeles[i])
					i = randrange(8)
				QR = {"QR" : moulinette}
				return json.dumps(QR, indent = 4)
				#On utilise la méthode dump pour enregistrer l'objet.
			except:
				return "La fonction for ne fonctionne pas"
	except:
		return " connexion au serveur a échoué" 

app.run(host='0.0.0.0', port=11001)