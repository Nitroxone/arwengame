import os
import pickle
import sys

clear=lambda:os.system("cls")
pause=lambda:input("Appuyez sur une touche pour continuer.")

def print_separator(length):
	for loop in range(length-1):
		sys.stdout.write("-")
		sys.stdout.flush()
	print("-")

def main_menu():
	while True:
		inMainMenu=True
		clear()
		print("Arwen - Créateur et éditeur du jeu")
		print_separator(35)
		print("1. Créer une arme")
		print("2. Créer une armure")
		print("3. Créer un livre")
		print_separator(35)
		print("A. Voir la liste des armes")
		print("B. Voir la liste des armures")
		print("C. Voir la liste des livres")
		print("0. Quitter")
		choice=input(" > ")
		if choice=="1":
			create_weapon()
		elif choice=="2":
			create_armor()
		elif choice=="3":
			create_book()
		elif choice.lower()=="a":
			show_weapons_list()
		elif choice.lower()=="b":
			show_armors_list()
		elif choice.lower()=="c":
			show_books_list()
		elif choice=="0":
			exit()

def create_weapon():
	clear()
	global weaponName
	weaponName=input("Entrez un nom pour la variable de l'arme : ")
	globals()[weaponName]=Weapon()
	global savefilename
	savefilename="data/weapons/{}_data".format(weaponName)
	while True:
		inWeaponCreation=True
		clear()
		print("Création d'une arme")
		print_separator(15)
		print("Nom :",globals()[weaponName].name)
		print("Description :",globals()[weaponName].desc)
		print("Dégâts :",globals()[weaponName].dmg)
		print("Coût en vigueur :",globals()[weaponName].scost)
		print("Valeur de défense :",globals()[weaponName].blockvalue)
		print("Prix :",globals()[weaponName].price)
		print("Poids :",globals()[weaponName].weight)
		print_separator(15)
		print("1. Éditer le nom")
		print("2. Éditer la description")
		print("3. Éditer les dégâts")
		print("4. Éditer le coût en vigueur")
		print("5. Éditer la valeur de défense")
		print("6. Éditer le prix")
		print("7. Éditer le poids")
		print("0. Sauvegarder l'arme")
		choice=input(" > ")
		if choice=="1":
			clear()
			globals()[weaponName].name=input("Entrez un nom pour l'arme : ")
		elif choice=="2":
			clear()
			globals()[weaponName].desc=input("Entrez une description pour l'arme : ")
		elif choice=="3":
			clear()
			globals()[weaponName].dmg=int(input("Entrez une valeur pour les dégâts de l'arme : "))
		elif choice=="4":
			clear()
			globals()[weaponName].scost=int(input("Entrez une valeur pour le coût en vigueur de l'arme : "))
		elif choice=="5":
			clear()
			globals()[weaponName].blockvalue=int(input("Entrez une valeur de défense pour l'arme : "))
		elif choice=="6": 
			clear()
			globals()[weaponName].price=int(input("Entrez une valeur pour le prix de l'arme : "))
		elif choice=="7":
			clear()
			globals()[weaponName].weight=int(input("Entrez une valeur pour le poids de l'arme : "))
		elif choice=="0":
			save_weapon(globals()[weaponName])
			break

def create_armor():
	clear()
	global armorName
	armorName=input("Entrez un nom pour la variable de l'armure : ")
	globals()[armorName]=Armor()
	global savefilename
	savefilename="data/armors/{}_data".format(armorName)
	while True:
		inArmorCreation=True
		clear()
		print("Création d'une armure")
		print_separator(15)
		print("Nom :",globals()[armorName].name)
		print("Description :",globals()[armorName].desc)
		print("Résistance physique :",globals()[armorName].pres)
		print("Résistance magique :",globals()[armorName].mres)
		print("Prix :",globals()[armorName].price)
		print("Poids :",globals()[armorName].weight)
		print_separator(15)
		print("1. Éditer le nom")
		print("2. Éditer la description")
		print("3. Éditer la résistance physique")
		print("4. Éditer la résistance magique")
		print("5. Éditer le prix")
		print("6. Éditer le poids")
		print("0. Sauvegarder l'arme")
		choice=input(" > ")
		if choice=="1":
			clear()
			globals()[armorName].name=input("Entrez un nom pour l'armure : ")
		elif choice=="2":
			clear()
			globals()[armorName].desc=input("Entrez une description pour l'armure : ")
		elif choice=="3":
			clear()
			globals()[armorName].pres=int(input("Entrez une valeur pour la résistance physique de l'armure : "))
		elif choice=="4":
			clear()
			globals()[armorName].mres=int(input("Entrez une valeur pour la résistance magique de l'armure : "))
		elif choice=="5":
			clear()
			globals()[armorName].price=int(input("Entrez une valeur pour le prix de l'armure : "))
		elif choice=="6":
			clear()
			globals()[armorName].weight=int(input("Entrez une valeur pour le poids de l'armure : "))
		elif choice=="0":
			save_armor(globals()[armorName])
			break

def create_book():
	clear()
	global bookName
	bookName=input("Entrez un nom pour la variable du livre : ")
	globals()[bookName]=Book()
	global savefilename
	savefilename="data/items/books/{}_data".format(bookName)
	while True:
		inBookCreation=True
		clear()
		print("Création d'un livre")
		print_separator(15)
		print("Nom :",globals()[bookName].name)
		print("Description :",globals()[bookName].desc)
		print("Contenu :",globals()[bookName].contentpreview) #contentpreview
		print_separator(15)
		print("1. Éditer le nom")
		print("2. Éditer la description")
		print("3. Éditer le contenu")
		print("4. Lire le contenu")
		print("0. Sauvegarder le livre")
		choice=input(" > ")
		if choice=="1":
			clear()
			globals()[bookName].name=input("Entrez un nom pour le livre : ")
		elif choice=="2":
			clear()
			globals()[bookName].desc=input("Entrez une description pour le livre : ")
		elif choice=="3":
			globals()[bookName].content=text_editor()
			globals()[bookName].contentpreview=' '.join(globals()[bookName].content.split()[:3])+' ...'
		elif choice=="4":
			clear()
			print(globals()[bookName].content)
			pause()
		elif choice=="0":
			save_book(globals()[bookName])
			break
			
def save_weapon(weapon):
	clear()
	print("Sauvegarde ...")
	weapon_data={"var":weaponName,
				 "name":weapon.name,
				 "desc":weapon.desc,
				 "dmg":weapon.dmg,
				 "scost":weapon.scost,
			     "blockvalue":weapon.blockvalue,
			     "price":weapon.price,
			     "weight":weapon.weight}
	with open(savefilename,"wb") as file:
		pickle.dump(weapon_data,file)
	print("Arme sauvegardée.")
	pause()
	
def save_armor(armor):
	clear()
	print("Sauvegarde ...")
	armor_data={"var":armorName,
				"name":armor.name,
				"desc":armor.desc,
				"pres":armor.pres,
				"mres":armor.mres,
				"price":armor.price,
				"weight":armor.weight}
	with open(savefilename,"wb") as file:
		pickle.dump(armor_data,file)
	print("Armure sauvegardée.")
	pause()

def save_book(book):
	clear()
	print("Sauvegarde ...")
	book_data={"var":bookName,
			   "name":book.name,
			   "desc":book.desc,
			   "content":book.content,
			   "contentpreview":book.contentpreview}
	with open(savefilename,"wb") as file:
		pickle.dump(book_data,file)
	print("Livre sauvegardé.")
	pause()

def show_armors_list():
	clear()
	datafiles=os.listdir("data/armors/")
	for file in datafiles:
		file="data/armors/{}".format(file)
		with open(file,"rb") as armorfile:
			armor_data=pickle.load(armorfile)
		armorVar=armor_data["var"]
		armorName=armor_data["name"]
		armorDesc=armor_data["desc"]
		armorPres=armor_data["pres"]
		armorMres=armor_data["mres"]
		armorPrice=armor_data["price"]
		armorWeight=armor_data["weight"]
		print(armorName,"(",armorVar,")")
		print(armorDesc)
		print("PRES :",armorPres)
		print("MRES :",armorMres)
		print("PRIC :",armorPrice)
		print("WGHT :",armorWeight)
		print_separator(25)
	choice=input("Entrez le nom de l'armure à modifier : ")
	choice="{}_data".format(choice)
	for file in datafiles:
		if choice.lower()==file.lower():
			file="data/armors/{}".format(file)
			with open(file,"rb") as armorfile:
				armor_data=pickle.load(armorfile)
			armorVar=armor_data["var"]
			armorName=armor_data["name"]
			armorDesc=armor_data["desc"]
			armorPres=armor_data["pres"]
			armorMres=armor_data["mres"]
			armorPrice=armor_data["price"]
			armorWeight=armor_data["weight"]
			inArmorEdition=True
			oldVarName="data/armors/{}_data".format(armorVar)
			while inArmorEdition:
				clear()
				print("Édition d'une armure")
				print_separator(20)
				print("1. Variable :",armorVar)
				print("2. Nom :",armorName)
				print("3. Description :",armorDesc)
				print("4. PRES :",armorPres)
				print("5. MRES :",armorMres)
				print("6. PRIC :",armorPrice)
				print("7. WGHT :",armorWeight)
				print("A. Sauvegarder les modifications")
				print("B. Quitter")
				print_separator(20)
				choice=input(" > ")
				if choice=="1":
					clear()
					armorVar=input("Entrez une variable pour l'arme : ")
				elif choice=="2":
					clear()
					armorName=input("Entrez un nom pour l'arme : ")
				elif choice=="3":
					clear()
					armorDesc=input("Entrez une description pour l'arme : ")
				elif choice=="4":
					clear()
					armorPres=int(input("Entrez une valeur pour la PRES : "))
				elif choice=="5":
					clear()
					armorMres=int(input("Entrez une valeur pour la MRES : "))
				elif choice=="6":
					clear()
					armorPrice=int(input("Entrez une valeur pour le PRIC : "))
				elif choice=="7":
					clear()
					armorWeight=int(input("Entrez une valeur pour la WGHT : "))
				elif choice.lower()=="a":
					clear()
					print("Sauvegarde ...")
					os.remove(oldVarName)
					armor_data={"var":armorVar,
								"name":armorName,
								"desc":armorDesc,
								"pres":armorPres,
								"mres":armorMres,
								"price":armorPrice,
								"weight":armorWeight}
					savefilename="data/armors/{}_data".format(armorVar)
					with open(savefilename,"wb") as file:
						pickle.dump(armor_data,file)
					print("Modifications sauvegardées.")
					pause()
				elif choice.lower()=="b":
					inArmorEdition=False
		elif choice.lower()=="cancel":
			return
	
def show_weapons_list():
	clear()
	datafiles=os.listdir("data/weapons/")
	for file in datafiles:
		file="data/weapons/{}".format(file)
		with open(file,"rb") as weaponfile:
			weapon_data=pickle.load(weaponfile)
		weaponVar=weapon_data["var"]
		weaponName=weapon_data["name"]
		weaponDesc=weapon_data["desc"]
		weaponDmg=weapon_data["dmg"]
		weaponScost=weapon_data["scost"]
		weaponBlockvalue=weapon_data["blockvalue"]
		weaponPrice=weapon_data["price"]
		weaponWeight=weapon_data["weight"]
		print(weaponName,"(",weaponVar,")")
		print(weaponDesc)
		print("Dégâts :",weaponDmg)
		print("Coût en vigueur :",weaponScost)
		print("Valeur de défense :",weaponBlockvalue)
		print("Prix :",weaponPrice)
		print("Poids :",weaponWeight)
		print_separator(25)
	choice=input("Entrez le nom de l'arme à modifier : ")
	choice="{}_data".format(choice)
	for file in datafiles:
		if choice.lower()==file.lower():
			file="data/weapons/{}".format(file)
			with open(file,"rb") as weaponfile:
				weapon_data=pickle.load(weaponfile)
			weaponVar=weapon_data["var"]
			weaponName=weapon_data["name"]
			weaponDesc=weapon_data["desc"]
			weaponDmg=weapon_data["dmg"]
			weaponScost=weapon_data["scost"]
			weaponBlockvalue=weapon_data["blockvalue"]
			weaponPrice=weapon_data["price"]
			weaponWeight=weapon_data["weight"]
			inWeaponEdition=True
			oldVarName="data/weapons/{}_data".format(weaponVar)
			while inWeaponEdition:
				clear()
				print("Édition d'une arme")
				print_separator(20)
				print("1. Variable :",weaponVar)
				print("2. Nom :",weaponName)
				print("3. Description :",weaponDesc)
				print("4. Dégâts :",weaponDmg)
				print("5. Coût en vigueur :",weaponScost)
				print("6. Valeur de défense :",weaponBlockvalue)
				print("7. Prix :",weaponPrice)
				print("8. Poids :",weaponWeight)
				print("A. Sauvegarder les modifications")
				print("B. Quitter")
				print_separator(20)
				choice=input(" > ")
				if choice=="1":
					clear()
					weaponVar=input("Entrez une variable pour l'arme : ")
				elif choice=="2":
					clear()
					weaponName=input("Entrez un nom pour l'arme : ")
				elif choice=="3":
					clear()
					weaponDesc=input("Entrez une description pour l'arme : ")
				elif choice=="4":
					clear()
					weaponDmg=int(input("Entrez une valeur de dégâts pour l'arme : "))
				elif choice=="5":
					clear()
					weaponScost=int(input("Entrez une valeur de coût en vigueur pour l'arme : "))
				elif choice=="6":
					clear()
					weaponBlockvalue=int(input("Entrez une valeur de défense pour l'arme : "))
				elif choice=="7":
					clear()
					weaponPrice=int(input("Entrez un prix pour l'arme : "))
				elif choice=="8":
					clear()
					weaponWeight=int(input("Entrez un poids pour l'arme : "))
				elif choice.lower()=="a":
					clear()
					print("Sauvegarde ...")
					os.remove(oldVarName)
					weapon_data={"var":weaponVar,
								 "name":weaponName,
								 "desc":weaponDesc,
								 "dmg":weaponDmg,
								 "scost":weaponScost,
								 "blockvalue":weaponBlockvalue,
								 "price":weaponPrice,
								 "weight":weaponWeight}
					savefilename="data/weapons/{}_data".format(weaponVar)
					with open(savefilename,"wb") as file:
						pickle.dump(weapon_data,file)
					print("Modifications sauvegardées.")
					pause()
				elif choice.lower()=="b":
					inWeaponEdition=False
		elif choice.lower()=="cancel":
			return

def show_books_list():
	clear()
	datafiles=os.listdir("data/items/books/")
	for file in datafiles:
		file="data/items/books/{}".format(file)
		with open(file,"rb") as bookfile:
			book_data=pickle.load(bookfile)
		bookVar=book_data["var"]
		bookName=book_data["name"]
		bookDesc=book_data["desc"]
		bookContent=book_data["content"]
		bookContentpreview=book_data["contentpreview"]
		print(bookName,"(",bookVar,")")
		print(bookDesc)
		print("Contenu :",bookContentpreview)
		print_separator(25)
	choice=input("Entrez le nom du livre à modifier : ")
	choice="{}_data".format(choice)
	for file in datafiles:
		if choice.lower()==file.lower():
			file="data/items/books/{}".format(file)
			with open(file,"rb") as bookfile:
				book_data=pickle.load(bookfile)
			bookVar=book_data["var"]
			bookName=book_data["name"]
			bookDesc=book_data["desc"]
			bookContent=book_data["content"]
			bookContentpreview=book_data["contentpreview"]
			inBookEdition=True
			oldVarName="data/items/books/{}_data".format(bookVar)
			while inBookEdition:
				clear()
				print("Édition d'un livre")
				print_separator(20)
				print("1. Variable :",bookVar)
				print("2. Nom :",bookName)
				print("3. Description :",bookDesc)
				print("4. Contenu :",bookContentpreview)
				print("5. Lire le contenu")
				print("A. Sauvegarder les modifications")
				print("B. Quitter")
				print_separator(20)
				choice=input(" > ")
				if choice=="1":
					clear()
					bookVar=input("Entrez une variable pour le livre : ")
				elif choice=="2":
					clear()
					bookName=input("Entrez un nom pour le livre : ")
				elif choice=="3":
					clear()
					bookDesc=input("Entrez une description pour le livre : ")
				elif choice=="4":
					bookContent=text_editor()
					bookContentpreview=' '.join(bookContent.split()[:3])+' ...'
				elif choice=="5":
					clear()
					print(bookContent)
					print_separator(20)
					pause()
				elif choice.lower()=="a":
					clear()
					print("Sauvegarde ...")
					os.remove(oldVarName)
					book_data={"var":bookVar,
							   "name":bookName,
							   "desc":bookDesc,
							   "content":bookContent,
							   "contentpreview":bookContentpreview}
					savefilename="data/items/books/{}_data".format(bookVar)
					with open(savefilename,"wb") as file:
						pickle.dump(book_data,file)
					print("Modifications sauvegardées.")
					pause()
				elif choice.lower()=="b":
					inBookEdition=False
		elif choice.lower()=="cancel":
			return

def text_editor():
	content=""
	while True:
		clear()	
		print(content)
		print_separator(20)
		print("1. Ajouter du texte")
		print("2. Sauter une ligne")
		print("3. Retour à la ligne")
		print("4. Tout effacer")
		print("A. Sauvegarder le texte")
		print("B. Quitter")
		choice=input(" > ")
		if choice=="1":
			print_separator(15)
			content+=input("Ajouter > ")
		elif choice=="2":
			content+="\n\n"
		elif choice=="3":
			content+="\n"
		elif choice=="4":
			content=""
		elif choice.lower()=="a":
			return content
		elif choice.lower()=="b":
			return 
		elif choice=="":
			content+="\n"
		
class Weapon(object):
        	
	def __init__(self):
		self.name="Aucun nom"
		self.desc="Aucune description"
		self.dmg=0
		self.scost=0
		self.blockvalue=0
		self.price=0
		self.weight=0
		
class Armor(object):

	def __init__(self):
		self.name="Aucun nom"
		self.desc="Aucune description"
		self.pres=0
		self.mres=0
		self.price=0
		self.weight=0

class Book(object):

	def __init__(self):
		self.name="Aucun nom"
		self.desc="Aucune description"
		self.content=""
		self.contentpreview="Aucun contenu"
		
main_menu()	

