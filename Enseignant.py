from Personne import Personne
from utils import db_management

class Enseignant (Personne):
    def __init__(self,nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule,numero_tel):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__numero_tel = numero_tel

    def getNumeroTel(self):
        return self.__numero_tel

        # additional setters

    def setNumero_Tel(self, numero):
        self.__numero_tel = numero

    def visualiser_classes_enseignant(self,personne_ID_choix):
        sql=f"SELECT nom FROM poo.classroom WHERE ID=(SELECT class_ID from poo.class_enseignant WHERE enseignant_ID='{personne_ID_choix}')"
        res=db_management.query_from_DB(sql)
        if len(res)>0:
            print(res[0][0])
        else: 
            print ("[]")

    def visualiser_classe(self, choix_classe):
        sql = f"SELECT * FROM poo.etudiant where class_ID='{choix_classe}'"
        res= db_management.query_from_DB(sql)
        print(res)

    def changer_info(self,Enseignant_ID, column_input, val_input):
        sql=f"UPDATE poo.enseignant SET {column_input}='{val_input}' WHERE ID='{Enseignant_ID}'"
        db_management.insert_in_db(sql)
        print("Personne modifiée")
        
