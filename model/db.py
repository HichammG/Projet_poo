from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify
import jwt
import mysql.connector
from mysql.connector import errorcode

#class user_model():


    #def __init__(self):
     #   try:
cnx = mysql.connector.connect(user='root', password='password',host='127.0.0.1', database='poo')
            #self.con = mysql.connector.connect(host=dbconfig['localhost'],user=dbconfig['root'],password=dbconfig['password'],database=dbconfig['poo'])
            #self.con.autocommit=True
           # self.cur = self.con.cursor(dictionary=True)
         #   print("Connected")
        #except mysql.connector.Error as err:
       #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #        print("Something is wrong with your user name or password")
         #   elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #        print("Database does not exist")
         #   else:
          #      print(err)
        #else:
       #     cnx.close()
cursor = cnx.cursor()
classement = {
    'id' : 3,
    'nom': 'mm',
}
query = ("INSERT INTO classroom( nom) VALUES ('class100');")
query2 = ("SELECT * FROM classroom;")
res=cursor.execute(query2)
#cnx.commit()

for (id,nom) in cursor:
  print("{}, {} ".format(id, nom))
cursor.close()
cnx.close()


