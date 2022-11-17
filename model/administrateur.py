# classe administrateur
class administrateur(personne):
    def __init__(self, nom: str, prenom: str, date_de_naissance: str, lieu_de_naissance: str, adresse_electronique: str,
                 matricule: int, mot_de_passe: str):
        super().init(
            nom: str, prenom: str, date_de_naissance: str, lieu_de_naissance: str, adresse_electronique: str, matricule: int)
        self._mot_de_pass = mot_de_passe

    # additional getters
    def get_mot_de_pass(self):
        return self._mot_de_pass

    # additional setters
    def set_mot_de_pass(self, mot_de_passe):
        self._mot_de_pass = mot_de_passe

    # Connexion a l application via un login et un mot de passe
    def connect_to_app(self, login: str, mot_de_passe: str):
        # fonction de connexion
        pass