# coding: UTF-8
#importon le module postgresql 
import psycopg2
import csv
#connection à la base de donnée postgres

class database:
	conn = psycopg2.connect(user='dave', password ='dave', host='localhost', database='db')
	cur = conn.cursor()

	#Ajout d'une table via un fichier excel
	def ajout(self):
		a = self.cur
		b = self.conn
		#créons une table 
		a.execute("create table personne (id int primary key, Nom varchar(10), Prenom varchar(12), Adresse varchar(15), Facture text ) ")
		#importons le fichier execel dans ta la table créer 
		csv_file = ("/home/debian/Bureau/classeur2.csv")
		sql = ("COPY personne from STDIN DELIMITER ';' CSV HEADER ")
		a.copy_expert(sql,open(csv_file,'r'))
		#enregistrons toutes actions dans la base de données
		b.commit()

		#affichons la table créer
		a.execute("select * from personne ")
		rows = a.fetchall()
		print(rows)
	#definisson une focntion pour modifier une colone de la table 
	def modif(self):
		a = self.cur
		b = self.conn
		a.execute("update personne set facture = 'AAA' ")
		b.commit()
		a.execute("select * from personne")
		rows = a.fetchall()
		print(rows)

	# d&finissons une fonction pour crypter une colone
	#il faut avant ça créer l'extension pgcrypto dans la base de donnée
	def crypt(self):
		a = self.cur
		b = self.conn
		a.execute("update personne set facture =pgp_sym_encrypt(facture,'AES_KEY')")
		b.commit()
		a.execute("select * from personne")
		rows = a.fetchall()
		print(rows)

	#définisson une fonction pour dérytper la colone
	def decrypt(self):
		a = self.cur
		b = self.conn
		a.execute("update personne set facture=pgp_sym_decrypt(facture::bytea,'AES_KEY')")
		b.commit()
		a.execute("select * from personne")
		rows = a.fetchall()
		print(rows)
	# cette fontion nous permettra d'afficher la table 
	def aff(self):
		a = self.cur
		b = self.conn
		a.execute("select * from personne")
		rows = a.fetchall()
		print(rows)

#definission une varaible pour permettre à l'utilisateur de choisir l'action a exécuté

A = int(input("entrez 1 pour l'ajout d'une table \n entrez 2 pour modifier une colone \n entrez 3 pour crypter  une colonne \n entrez 4 pour decrypter la colonne \n entrez 5 pour afficher la table "))
if (A == 1):
	try:
		create = database()
		create.ajout()
		pass
	except psycopg2.errors.DuplicateTable :
		print("la tabale existe ")
		pass

elif A == 2 :
	create = database()
	create.modif()

elif A == 3 :
	create = database()
	create.crypt()

elif A == 4 :
	try:
		create = database()
		create.decrypt()
		pass
	except psycopg2.errors.ExternalRoutineInvocationException:
		print ("la table n'est pas crypté")
		pass

elif A == 5 :
		create = database()
		create.aff()
else :
	try:
		print("le chiffre doit être compris  entre 1 et 5 ")
		pass
	except ValueError : 
		print("veuillez entrez un nombre en 1 et 5 ")
		pass





