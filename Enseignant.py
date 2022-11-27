from Personne import Personne

class Enseignant (Personne):
    def __init__(self,nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule,numero_tel):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__numero_tel = numero_tel

    def getNumeroTel(self):
        return self.__numero_tel

        # additional setters

    def setNumeroTel(self, numero):
        self.__numero_tel = numero