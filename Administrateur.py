import mysql.connector
import mysql.connector
from Personne import Personne
from classe import classe
# classe administrateur

class Administrateur(Personne):
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule, mot_de_passe):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__mot_de_pass = mot_de_passe

    # additional getters
    def get_mot_de_pass(self):
        return self.__mot_de_pass

    # additional setters
    def set_mot_de_pass(self, mot_de_passe):
        self.__mot_de_pass = mot_de_passe

    # Connexion a l application via un login et un mot de passe
    def connect(self, login: str, mot_de_passe: str):
        # fonction de connexion
        pass

    def create_in_DB (self):
        #connect to DB
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
#        var=(f"INSERT INTO admin (nom, prenom, mail, date_naissance, lieu_naissance,password ) values ({self.get_nom()}, {self.get_prenom()}, {self.get_adresse_electronique()}, {self.get_date_de_naissance()}, {self.get_lieu_de_naissance()}, {self.get_mot_de_pass()});")
        res=cursor.execute("SELECT * FROM admin")
#        cnx.commit()
#        cursor.close()
        cnx.close()
        print(res)
        print("Admin object created in database")

    def read_from_DB(self, matricule):
        # connect to DB
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        res = cursor.execute("SELECT * FROM admin")

        cnx.close()
        print(res)
        print("Admin object read from database")

    def create_classe(self, nom1):
        c=classe(nom1)
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        query= "INSERT INTO classroom(name) VALUES (%s)"

        cursor.execute(query, nom1)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Classroom object read from database")