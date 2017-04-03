#/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask
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
		i = randrange(8)
		moulinette = []
		for i in range(0,len(datas)): # i est compris entre 0 et 20
			try:
				for data in datas:
					questions = [('Quel est le numéro du département ' + data[3] + ' ?'),
					('Quel est le département qui à pour numéro ' + data[4] + ' ?'),
					('Quelle est la préfecture du département ' + data[4] + ' ?'),
					(data[5] + ' est la préfecture de quel département ?'),
					('Dans quel département se trouve la préfecture de ' + data[5] + ' ?'),
					('Dans quelle région se trouve le département ' + data[4] + ' ?'),
					(data[4] + ' est un département. Quand quelle région se trouve-t-il ?'),
					('Quel est le chef-lieu de la région' + data[1] + '?')]
					moulinette.append(questions[i])
					i = randrange(8)

				return json.dumps(moulinette, indent = 4)
		#pou question[0] 'Quel est le numéro du département ' + data[3] + '?' on prend le 1er élément de datas 
		# on prend ensuite question[1]
		# on passe au 2 élément de datas
			except:
				return "La fonction for ne fonctionne pas"
	except:
		return " connexion au serveur a échoué" 

app.run(host='0.0.0.0', port=11001)





