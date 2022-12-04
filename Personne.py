#class mere Personne
class Personne():
    #Constructeur de la classe
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule):
        self.__nom = nom
        self.__prenom=prenom
        self.__date_de_naissance = date_de_naissance
        self.__lieu_de_naissance = lieu_de_naissance
        self.__adresse_electronique = adresse_electronique
        self.__matricule = matricule
    #getters
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_date_de_naissance(self):
        return self.__date_de_naissance
    def get_lieu_de_naissance(self):
        return self.__lieu_de_naissance
    def get_adresse_electronique(self):
        return self.__adresse_electronique
    def get_matricule(self):
        return self.__matricule
    #setters
    def set_nom(self,nom):
        self.__nom = nom
    def set_prenom(self,prenom):
        self.__prenom = prenom
    def set_date_de_naissance(self,date_de_naissance):
        self.__date_de_naissance = date_de_naissance
    def set_lieu_de_naissance(self,lieu_de_naissance):
        self.__lieu_de_naissance = lieu_de_naissance
    def set_adresse_electronique(self,adresse_electronique):
        self.__adresse_electronique = adresse_electronique
    def set_matricule(self,matricule):
        self.__matricule = matricule
        
    def visualiser_classes_enseignant(self,personne_ID_choix):
        pass
    
    def visualiser_classe(self, choix_classe):
        pass
    
    def changer_info(self,Enseignant_ID, column_input, val_input):
        pass
    
    def list_etudiant_DB(self, matricule):
        pass
    
    def modifier(self,Etudiant_ID, val_input):
        pass
    
    def create_classroom(self,name):
        pass
    
    def ajouter_personne_classe(self,choix_type, classe_ID_input, personne_ID_choix):
        pass
    
    def afficher_classe(self, classe_ID_input):
        pass
    
    def retirer_personne_classe(self,choix_type,classe_ID_input,personne_ID_choix):
        pass
    
    def modifier_personne(self,choix_type,personne_ID_choix, column_input, val_input):
        pass
    
    def visualiser_classes_enseignant(self,personne_ID_choix):
        pass
    
    def afficher_classe_etudiant(self,personne_ID_choix):
        pass
