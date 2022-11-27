from Personne import Personne

class Enseignant (Personne):
    def __init__(self,nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule,numero_tel):
        super().__init__(nom, prenom, date_de_naissance, lieu_de_naissance, adresse_electronique, matricule)
        self.__numero_tel = numero_tel

    def getNumeroTel(self):
        return self.__numero_tel

        # additional setters

    def setCours_assigne(self, numero):
        self.__numero_tel = numero
        
           #modifier les informations d'un enseignant dans la base de données
    def modifier_info(self,mail,numeroTel):
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        cursor.execute("UPDATE enseignant.mail={}  , enseignant.numeroTel={} WHERE etudiant.etudiant_id=self.get_mmatricule ".format(numeroTel,mail))
        cnx.commit()
        cnx.close()
        print("les étudiants de la meme classe")

    #trouver un enseignant dans la base de donner à partir de matricule
    @classmethod
     def findByMatricul(self,mat):
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        ens = cursor.execute("select enseignant where enseignant.enseignant_id=matr")
        cnx.close()
        return ens

     def visualise_classe(self):
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
        cursor = cnx.cursor()
        ens = cursor.execute("select classroom_nom from enseignant join classroom join enseignement where enseignant.enseignant_id =enseignement.enseignant_id and enseignement.classroom_id = classroom.classroom_id and enseignant.enseignant_id=self.get_matricule")
        cnx.close()
        return ens

