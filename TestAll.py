
from Personne import Personne
import mysql.connector
from
cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='poo')
cursor = cnx.cursor()

choix = input("Si vous etes un étudiant choisissez 'E' , si vous etes un enseignant choisissez 'T' si vous etes un administrateur choisissez 'A' ")
matr = int(input("Donner votre matricule"))

match choix:
    case "E":
        """verifier la matricule"""

        n = int(input("Souhaitez vous voir votre classe et vos collègues '1' ou bien modifier vos information '2' "))

        if (n == 1):
            cls =cursor.execute("SELECT classe FROM where matricule=matr")
            cursor.execute("select nom , prenom from etudiant where classe=cls ")
            data=cursor.fetchall()
            for i in data:
                print(i)

        if (n== 2):
            numeroTel=input("Entrer votre numéro de téléphone: ")
            mail= input("Entrer votre adresse electronique")
            cursor.execute("update Etudiant set numeroTel={} , mail={}".format(numeroTel,mail))


        else:
            print("Merci pour votre visite !")

    case "T":
        print("enseignat")
    case "A":
        print("administrateur")

    case _:
        print("Nous ne reconnaissons pas ce choix.")