#/usr/bin/env python
# -*- coding:utf-8 -*-

#import os # On importe le module os

from flask import Flask
from random import randrange
import psycopg2

app = Flask(__name__)


@app.route('/')
def data():
	try:
		dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
		dbcur = dbcon.cursor() 
		dbcur.execute("SELECT * FROM test ORDER BY random() LIMIT 1")
		datas = dbcur.fetchall()		
		for data in datas:
			return "quelle est la préfecture du département " + data[4] + " ?"
	except:
		return " connexion au serveur a échoué" 

app.run(host='0.0.0.0', port=11001)




