from Personne import Personne
# classe administrateur

class Administrateur(Personne):
    def __init__(self, nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique,matricule, mot_de_passe):
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