#-*- coding:Utf-8-*-

import os # On importe le module os

from random import randrange
import psycopg2

try:
    input('insere du texte pour tester : ')
except:
    print("le fichier ne fonctionne pas.")

dbcon = psycopg2.connect('host=vps338664.ovh.net port=5432 dbname=geoquizz user=geodds password=acsdds')
dbcur = dbcon.cursor() 
dbcur.execute("SELECT * FROM question")
data = str(dbcur.fetchall())

print(data)


os.system("pause")