from Administrateur import Administrateur
from Enseignant import Enseignant
from Etudiant import Etudiant
import mysql.connector
import mysql
from utils import db_management
from classe import classe


# Console interactive 

user_type=None
connected=False
choix_operation = None

while(user_type ==None ):
    print("Bonjour et bienvenue dans la plateforme de gestion d'absence")
    temp=input("Si vous etes administrateur tapez 1, si vous êtes enseignant tapez 2 si vous êtes etudiant tapez 3 : ")
    
    if temp=='1': 
        user_type="Admin"
        break
    elif temp=='2': 
        user_type="Enseignant"
        break
    elif temp=='3': 
        user_type="Etudiant"
        break
    else:
        print("Faux choix")

#connexion d'administrateur à l'application via login et mot de passe 
while(user_type=='Admin' and connected == False):
    print("Si vous voulez quitter le menu tappez q")
    input_email=input('Veuillez inserer votre email : ')
    input_password=input('veuillez inserer votre mot de passe')
    if input_email=="q" or input_password=="q":
        break
        
    # Chercher l'admin dans la base de données
    sql=(f"SELECT mot_de_passe FROM poo.admin where Email='{input_email}'")
    real_password = db_management.query_from_DB(sql)[0][0]
    if real_password == input_password :
        print("Vous etes connecte en tant qu'administrateur")
        sql1=f"SELECT * FROM poo.admin WHERE Email='{input_email}'"
        
        res=db_management.query_from_DB(sql1)
        # print(res)
        a,b,c,d,e,f,g = res[0][1], res[0][2], str(res[0][4]), res[0][5], res[0][3],int(res[0][0]), str(res[0][6])
        # a,b,c,d,e,f,g= 'nom', 'prenom', '1900-12-12', 'LIEUU', '@', 55, 'jhjhsdfbv'
        my_obj=Administrateur(a,b,c,d,e,f,g)
        connected=True
        break
    else:
        print("Votre email ou mot de passe est incorrecte")
        connected = False

#Administrateur
while(user_type=='Admin' and connected == True and choix_operation==None):
    choix_operation=input("Si vous voulez créer une classe tapez 1,\n Si vous voulez ajouter une personne à une classe tapez 2, \n Si vous voulez Afficher les enseignant et les etudiants d'une classe tapez 3, \n Sivous voulez retirer une personne d'une classe tapez 4, \n Si vous voulez modifier les information d'une personne tapez 5, \n Si vous voulez visualiser les classes d'un enseignant tapez 6, \n Si vous voulez visualiser la classe d'un etudiant tapez 7, Si vous voulez quitter ce menu tapez n'importe quel autre caractere")
    if choix_operation=='1':
        classe_name=input("Entrer le nom de la classe")
        # creation de classroom a partir de l'objet admin
        my_obj.create_classroom(classe_name)
        print("classe créée")
        choix_operation=None
        
    elif choix_operation=='2':
        choix_type=input("Tapez 1 pour un enseignant, ou 2 pour un etudiant")
        classe_ID_input = input("Entrer l'ID de la classe souhaitée")
        personne_ID_choix=input("Entrer l'ID de la personne a ajouter")
        my_obj.ajouter_personne_classe(choix_type, classe_ID_input, personne_ID_choix)

    elif choix_operation=='3':
        classe_ID_input = int(input("Entrer l'ID de la classe souhaitée"))
        my_obj.afficher_classe(classe_ID_input)
        
    elif choix_operation=='4':
        choix_type=input("Tapez 1 pour un enseignant, ou 2 pour un etudiant")
        classe_ID_input = int(input("Entrer l'ID de la classe souhaitée"))
        personne_ID_choix=int(input("Entrer l'ID de la personne a retirer"))
        my_obj.retirer_personne_classe(choix_type,classe_ID_input,personne_ID_choix)
        
    elif choix_operation=='5':
        choix_type=input("Tapez 1 pour un enseignant, ou 2 pour un etudiant")
        personne_ID_choix=int(input("Entrer l'ID de la personne a modifier"))
        column_input=input("Entrer le nom de la colonne à modifier")
        val_input=input('Entrer la nouvelle valeur')
        my_obj.modifier_personne(choix_type,personne_ID_choix, column_input, val_input)
        
    elif choix_operation=='6':
        personne_ID_choix=input("Entrer l'ID de l'enseignant")
        my_obj.visualiser_classes_enseignant(personne_ID_choix)
        
    elif choix_operation=='7':
        personne_ID_choix=input("Entrer l'ID de l'etudiant")
        my_obj.afficher_classe_etudiant(personne_ID_choix)
        
    else:
        break

#Enseignant
while(user_type=='Enseignant'):
    print("Si vous voulez quitter tapez q")
    Enseignant_ID = input('Veuillez renseigner votre ID')
    if Enseignant_ID=='q': break
    # chercher l'enseignant dans la base de données
    sql=(f"SELECT * FROM poo.enseignant where ID='{Enseignant_ID}'")
    res =db_management.query_from_DB(sql)[0]
    my_obj=Enseignant(res[1], res[2], res[3], res[4], res[5], res[0], None)
   
    choix_operation=input("Si vous souhaitez afficher les classes auquelles vous appartenez tapez 1, \n Si vou souhaitez visualiser les etudiants d'une classe tapez 2, \n Si vous souhaitez modifier vos informations tapez 3")
    if choix_operation=="1":
        my_obj.visualiser_classes_enseignant(Enseignant_ID)
    elif choix_operation=="2":
        choix_classe=input("Veuillez saisir l'ID de la classe" )
        sql=f"SELECT * FROM poo.class_enseignant where class_ID = '{choix_classe}' AND enseignant_ID = '{Enseignant_ID}'"
        exist_in=len(db_management.query_from_DB(sql))
        if exist_in==0:
            print("Vous n'appartenez pas à cette classe")
            break
        else:
            my_obj.visualiser_classe(choix_classe)
    elif choix_operation=='3':
        column_input=input("Entrer le nom de la colonne à modifier")
        val_input=input("Entrer la nouvelle valeur de cette colonnes")
        my_obj.changer_info(Enseignant_ID, column_input, val_input)

#Etudiant
while(user_type=='Etudiant'):
    print("Si vous voulez quitter tapez q")
    Etudiant_ID = input('Veuillez renseigner votre ID')
    if Etudiant_ID=='q': break

    sql=(f"SELECT * FROM poo.etudiant where ID={Etudiant_ID}")
    res = db_management.query_from_DB(sql)[0]
    print(len(res))
    my_obj=Etudiant(res[1], res[2], res[3], res[4], res[5], res[0], res[6])
    print(my_obj)
    choix_operation=input("Si vous voulez visualiser les etudiants dans votre classe tapez 1, \n Si vous voulez modifier votre adresse email tapez 2")
    if choix_operation=='1':
        my_obj.list_etudiant_DB(Etudiant_ID)
    elif choix_operation=='2':
        val_input=input("Tapez votre nouveau Email")
        my_obj.modifier(Etudiant_ID, val_input)
        
