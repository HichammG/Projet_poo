from Personne import Personne
from utils import db_management
# classe administrateur

class Etudiant(Personne):
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique,matricule,classe):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self._classe = classe

    # additional getters
    def get_classe(self):
        return self._classe

    # additional setters
    def set_classe(self, classe):
        self._classe = classe
    
     #afficher les collègues d'un etudiant dans la meme classe
    def list_etudiant_DB(self, matricule):
        # connect to DB
        sql=f"SELECT nom,prenom FROM poo.etudiant WHERE etudiant.class_ID = (SELECT class_ID from poo.etudiant where ID='{matricule}')"
        res=db_management.query_from_DB(sql)
        print("les étudiants de la meme classe")
        print(res)
        
    #modifier les informations personnelles d'un etudiant
    def modifier(self,Etudiant_ID, val_input):
        sql=f"UPDATE poo.etudiant SET Email='{val_input}' WHERE ID='{Etudiant_ID}'"
        db_management.insert_in_db(sql)
        print('Email modifié')
