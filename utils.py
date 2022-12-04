import mysql.connector
import mysql


#Fonctions de connexion à la base de données
class db_management:
    
#fonction de modification dans la base de donner
    @classmethod
    def query_from_DB(self,sql):
#connexion la base de données
        cnx = mysql.connector.connect(user='root', host="127.0.0.1")
        cursor = cnx.cursor()
        res = cursor.execute(sql)
        cnx.close()
        return(cursor.fetchall())
    
# fonction d'insertion à la base de données
    @classmethod
    def insert_in_db(self,sql):
        cnx = mysql.connector.connect(user='root', host="127.0.0.1")
        cursor = cnx.cursor()
        res = cursor.execute(sql)
        cnx.commit()
        cnx.close()
