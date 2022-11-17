#class mere
class personne():
    #Constructeur de la classe
    def__init__(self, nom:str, prenom:str, date_de_naissance:str, lieu_de_naissance:str, adresse_electronique:str, matricule:int):
        self._nom=nom
        self._prenom=prenom
        self._date_de_naissance=date_de_naissance
        self._lieu_de_naissance=lieu_de_naissance
        self._adresse_electronique=adresse_electronique
        self._matricule=matricule
    #getters
    def get_nom(self):
        return self._nom
    def get_prenom(self):
        return self._prenom
    def get_date_de_naissance(self):
        return self._date_de_naissance
    def get_lieu_de_naissance(self):
        return self._lieu_de_naissance
    def get_adresse_electronique(self):
        return self._adresse_electronique
    def get_matricule(self):
        return self._matricule
    #setters
    def set_nom(sel,fnom):
        self._nom=nom
    def set_prenom(self,prenom):
        self._prenom=prenom
    def set_date_de_naissance(self,date_de_naissance):
        self._date_de_naissance=date_de_naissance
    def set_lieu_de_naissance(self,lieu_de_naissance):
        self._lieu_de_naissance=lieu_de_naissance
    def set_adresse_electronique(self,adresse_electronique):
        self._adresse_electronique=adresse_electronique
    def set_matricule(self,matricule):
        self._matricule=matricule