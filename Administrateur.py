from utils import db_management
import mysql.connector
import mysql.connector
from Personne import Personne
from classe import classe


# classe administrateur

class Administrateur(Personne):
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique,matricule, mot_de_passe):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__mot_de_pass = mot_de_passe

    # getters
    def get_mot_de_pass(self):
        return self.__mot_de_pass

    # setters
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


    def create_classroom(self,name):
        c=classe(name)
        sql2=f"INSERT INTO poo.classroom (Nom) VALUES ('{name}')"
        db_management.insert_in_db(sql2)

    def ajouter_personne_classe(self,choix_type, classe_ID_input, personne_ID_choix):
        if choix_type=='1':
            sql=f"INSERT INTO poo.class_enseignant VALUES ('{classe_ID_input}', '{personne_ID_choix}')"
            db_management.insert_in_db(sql)
            print("Personne ajoutée à la classe")
        elif choix_type=='2':
            sql=f"UPDATE poo.etudiant SET class_ID={classe_ID_input} WHERE etudiant.ID={personne_ID_choix}"
            db_management.insert_in_db(sql)
            print("Personne ajoutée à la classe")
        
    def afficher_classe(self, classe_ID_input):
        sql=f"SELECT nom, prenom from poo.etudiant WHERE class_ID='{classe_ID_input}'"
        etudiants=db_management.query_from_DB(sql)
        sql=f"select nom, prenom from poo.enseignant where ID=(select enseignant_ID from poo.class_enseignant  where class_ID='{classe_ID_input}')"
        enseignants=db_management.query_from_DB(sql)
        print("Les enseignants de cette classe sont:")
        print(enseignants)
        print("les etudiants de cette classe sont:")
        print(etudiants)

    def retirer_personne_classe(self,choix_type,classe_ID_input,personne_ID_choix):
        if choix_type=='1':
            sql=f"DELETE FROM poo.class_enseignant WHERE (class_ID='{classe_ID_input}'AND enseignant_ID='{personne_ID_choix}'"
            db_management.insert_in_db(sql)
            print("Personne retirée de la classe")
        elif choix_type=='2':
            sql=f"UPDATE poo.etudiant SET class_ID=NULL WHERE etudiant.ID={personne_ID_choix}"
            db_management.insert_in_db(sql)
            print("Personne retirée de la classe")

    def modifier_personne(self,choix_type,personne_ID_choix, column_input, val_input):
        if choix_type=='1':
            sql=f"UPDATE poo.enseignant SET {column_input}='{val_input}' WHERE ID='{personne_ID_choix}'"
            db_management.insert_in_db(sql)
            print("Personne modifiée")
        elif choix_type=='2':
            sql=f"UPDATE poo.etudiant SET {column_input}='{val_input}' WHERE ID='{personne_ID_choix}'"
            db_management.insert_in_db(sql)
            print("Personne modifiée")
    
    def visualiser_classes_enseignant(self,personne_ID_choix):
        sql=f"SELECT nom FROM poo.classroom WHERE ID=(SELECT class_ID from poo.class_enseignant WHERE enseignant_ID='{personne_ID_choix}')"
        res=db_management.query_from_DB(sql)
        print(res[0][0])

    def afficher_classe_etudiant(self,personne_ID_choix):
        sql=f"SELECT nom, prenom from poo.etudiant where class_ID=(SELECT class_ID from poo.etudiant WHERE ID='{personne_ID_choix}')"
        etudiants=db_management.query_from_DB(sql)
        sql=f"SELECT nom, prenom from poo.enseignant where ID=(SELECT enseignant_ID from poo.class_enseignant where(SELECT class_ID from poo.etudiant WHERE ID='{personne_ID_choix}'))"
        enseignants=db_management.query_from_DB(sql)
        print("Les enseignants de cette classe sont:")
        print(enseignants)
        print("les etudiants de cette classe sont:")
        print(etudiants)