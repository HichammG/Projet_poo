# from Administrateur import Administrateur
import mysql.connector
import mysql
# Ad1=Administrateur('amira', 'rekkache', '1000-01-01', 'alger', '@mail', '1234','12345678')
# Ad1.create_classe('new_class')

#Fonctions de connexion à la base de données
class db_management:
    @classmethod
    def query_from_DB(self,sql):
        cnx = mysql.connector.connect(user='root', host="127.0.0.1")
        cursor = cnx.cursor()
        res = cursor.execute(sql)
        cnx.close()
        return(cursor.fetchall())
    @classmethod
    def insert_in_db(self,sql):
        cnx = mysql.connector.connect(user='root', host="127.0.0.1")
        cursor = cnx.cursor()
        res = cursor.execute(sql)
        cnx.commit()
        cnx.close()