from Personne import Personne
# classe administrateur

class Etudiant(Personne):
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique,matricule, cours_assigne, numero_tel,classe):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__cours_assigne = cours_assigne
        self.__numero_tel = numero_tel
        self.__classe = classe

    # additional getters
    def getCours_assigne(self):
        return self.__cours_assigne

    # additional setters
    def setCours_assigne(self, cours_assigne):
        self.__cours_assigne = cours_assigne

    def getNumeroTel(self):
        return self.__numero_tel

    # additional setters
    def setCours_assigne(self, numero):
        self.__numero_tel = numero

