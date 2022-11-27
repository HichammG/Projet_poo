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
<<<<<<< HEAD
    def setNumeroTel(self, numero):
=======
    def setCours_assigne(self, numero):
>>>>>>> origin/master
        self.__numero_tel = numero
    
     #afficher les collègues d'un etudiant dans la meme classe
    def list_etudiant_DB(self, matricule):
        # connect to DB
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        res = cursor.execute("SELECT nom,prenom FROM etudiant join classroom WHERE etudiant.classroom_id = classroom.classroom_id")

        cnx.close()
        print(res)
        print("les étudiants de la meme classe")

