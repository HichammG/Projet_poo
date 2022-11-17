#classe enseignant
class enseignant(personne):
    def __init__(self, nom:str, prenom:str, date_de_naissance:str, lieu_de_naissance:str, adresse_electronique:str, matricule:int):
        super().init(nom:str, prenom:str, date_de_naissance:str, lieu_de_naissance:str, adresse_electronique:str, matricule:int)

    #additional getters

    #additional setters