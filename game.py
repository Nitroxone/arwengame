import os
import pickle
import sys
import time
import random
import operator

class Engine:

	def __init__(self):
		print("Chargement du jeu...")

	def clear(self):
		os.system("cls")

	def pause(self):
		input("Appuyez sur une touche pour continuer ...")

	def print_separator(self,length):
		for loop in range(length-1):
			sys.stdout.write('-')
			sys.stdout.flush()
		print('-')

	def delayed_print(self,message):
		for letter in message:
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(0.1)

	def displayError(self,errorName):
		if errorName.lower()=='invalidchoice':
			self.clear()
			print('Erreur : choix invalide. Veuillez réessayer.')
			self.pause()
		elif errorName.lower()=='weaponnotunlocked':
			self.clear()
			print('Vous n\'avez pas encore déverrouillé cette arme !')
			self.pause()
		elif errorName.lower()=='armornotunlocked':
			self.clear()
			print('Vous n\'avez pas encore déverrouillé cette armure !')
			self.pause()
		elif errorName.lower()=='notenoughpotions':
			self.clear()
			print('Vous n\'avez plus de potion de ce type !')
			self.pause()
		elif errorName.lower()=='dungeonunavailable':
			self.clear()
			print('Vous n\'avez pas encore débloqué l\'accès à ce donjon !')
			self.pause()
		elif errorName.lower()=='invalidfilename':
			self.clear()
			print('Nom de fichier incorrect.')
			self.pause()
		elif errorName.lower()=='notenoughgold':
			self.clear()
			print('Vous ne possédez pas assez d\'or.')
			self.pause()
		elif errorName.lower()=='incorrectvalue':
			self.clear()
			print('Erreur : valeur incorrecte.')
			self.pause()
		elif errorName.lower()=='mustenternumbers':
			self.clear()
			print('Erreur : vous devez entrer des chiffres.')
			self.pause()
		elif errorName.lower()=='notenoughstamina':
			self.clear()
			print('Erreur : vous n\'avez pas assez de vigueur.')
			self.pause()
		elif errorName.lower()=='notenoughmana':
			self.clear()
			print('Erreur : vous n\'avez pas assez de mana.')
			self.pause()
		elif errorName.lower()=='alreadyequippedweapon':
			self.clear()
			print('Erreur : l\'arme choisie est déjà équipée.')
			self.pause()
		elif errorName.lower()=='alreadyequippedarmor':
			self.clear()
			print('Erreur : l\'armure choisie est déjà équipée.')
			self.pause()

	def displayGold(self):
		print("Or possédé :",inventory.gold)

class Game:

	def run(self):
		while player.health>0:
			engine.clear()
			print(player.location)
			print("Que faites-vous ?")
			print("1. Avancer")
			print("2. Inventaire")
			print("3. Équipement")
			print("4. Statut")
			print("5. Sauvegarder la partie")
			print("6. Charger la partie")
			if player.location.lower()=="repaire":
				print("7. Marché noir")
			print("0. Quitter le jeu")
			choice_main=input(" > ")
			if choice_main=="1":
				if player.location.lower()=="repaire":
					game.selectNextLocation()
				else:
					game.move_forward()
			elif choice_main=="2":
				inventory.display_items()
			elif choice_main=="3":
				player.display_equipment()
			elif choice_main=="4":
				player.display_status()
			elif choice_main=="5":
				game.save_game()
			elif choice_main=="6":
				game.load_game()
			elif choice_main=="7":
				if player.location.lower()=="repaire":
					game.shop()
				else:
					engine.displayError("invalidChoice")
			elif choice_main=="0":
				askSaveBeforeQuit()
				break
			elif choice_main=="godmode":
				engine.clear()
				print("Godmode activé.")
				engine.pause()
				player.maxhealth=9999
				player.health=player.maxhealth
				player.maxstamina=9999
				player.stamina=player.maxstamina
				player.maxmana=9999
				player.mana=player.maxmana
				player.gold=9999
			if player.health<=0:
				game_over()
				break

	def selectNextLocation(self):
		inSelectNextLocation=True
		while inSelectNextLocation is True:
			engine.clear()
			print("Sélectionnez un donjon à explorer.")
			engine.print_separator(35)
			print("1. Antre de Khyrr Ikhu")
			print("2. Caverne du Grobbit")
			print("3. Palais de Limper Athris")
			print("4. Antichambre du Flan-bit")
			print("0. Rester dans le repaire")
			choice=input(" > ")
			if choice=="1":
				if player.khyrrikhu==True:
					player.location="Antre de Khyrr Ikhu - Première Salle"
					engine.clear()
					print("Vous entrez dans l'Antre de Khyrr Ikhu !")
					engine.pause()
					inSelectNextLocation=False
				else:
					engine.displayError("dungeonUnavailable")
			elif choice=="2":
				if player.grobbit==True:
					player.location="Caverne du Grobbit - Première Salle"
					engine.clear()
					print("Vous entrez dans la Caverne du Grobbit !")
					engine.pause()
					inSelectNextLocation=False
				else:
					engine.displayError("dungeonUnavailable")
			elif choice=="3":
				if player.limperathris==True:
					player.location="Palais de Limper Athris - Première Salle"
					engine.clear()
					print("Vous entrez dans le Palais de Limper Athris !")
					engine.pause()
					inSelectNextLocation=False
				else:
					engine.displayError("dungeonUnavailable")
			elif choice=="4":
				if player.flanbit==True:
					player.location="Antichambre du Flan-bit - Première Salle"
					engine.clear()
					print("Vous entrez dans l'Antichambre du Flan-bit !")
					engine.pause()
					inSelectNextLocation=False
				else:
					engine.displayError("dungeonUnavailable")
			elif choice=="0":
				inSelectNextLocation=False

	def move_forward(self):
		engine.clear()
		engine.delayed_print("Vous avancez ...")
		if player.location=="Antre de Khyrr Ikhu - Première Salle":
			game.combatscene(guerrierTribal)
		elif player.location=="Antre de Khyrr Ikhu - Deuxième Salle":
			game.combatscene(colosseTribal)
		elif player.location=="Antre de Khyrr Ikhu - Troisième Salle":
			game.combatscene(boss_khyrrikhu)
		elif player.location=="Caverne du Grobbit - Première Salle":
			game.combatscene(soldatPelagique)
		elif player.location=="Caverne du Grobbit - Deuxième Salle":
			game.combatscene(mastodontePelagique)
		elif player.location=="Caverne du Grobbit - Troisième Salle":
			game.combatscene(boss_grobbit)
		elif player.location=="Palais de Limper Athris - Première Salle":
			game.combatscene(gardeImperial)
		elif player.location=="Palais de Limper Athris - Deuxième Salle":
			game.combatscene(duellisteImperial)
		elif player.location=="Palais de Limper Athris - Troisième Salle":
			game.combatscene(boss_limperathris)
		elif player.location=="Antichambre du Flan-bit - Première Salle":
			game.combatscene(princeGelatineux)
		elif player.location=="Antichambre du Flan-bit - Deuxième Salle":
			game.combatscene(baronGelatineux)
		elif player.location=="Antichambre du Flan-bit - Troisième Salle":
			game.combatscene(boss_flanbit)

	def combatscene(self,enemy):
		engine.clear()
		print(player.name,"se bat contre",enemy.name,"!")
		engine.pause()
		enemyBlocks=False
		enemyWeaken=False
		duelBonusPlayer=False
		duelBonusEnemy=False
		foliesanguinaireMalus=False
		protectiondivineBonus=False
		boucliermagiqueBonus=False
		if power_boucliermagique.unlocked is True:
			boucliermagiqueBonus=True
		canalisationBonus=False
		colereBonus=False
		affaiblissementBonus=False
		renforcementBonus=False
		while True:
			if power_renaissance.unlocked is True:
				if player.health<=player.maxhealth/2:
					player.stamina+=player.maxstamina*25/100
					player.checkStats()
			engine.clear()
			playerRound=True
			playerBlocks=False
			print(player.name)
			print("HP :",player.health,"/",player.maxhealth)
			print("SP :",player.stamina,"/",player.maxstamina)
			print("MP :",player.mana,"/",player.maxmana)
			print("---------------")
			print(enemy.name)
			print("HP :",enemy.health,"/",enemy.maxhealth)
			print("SP :",enemy.stamina,"/",enemy.maxstamina)
			print("MP :",enemy.mana,"/",enemy.maxmana)
			print("---------------")
			print(" 1. Attaquer avec",player.equipped_weapon.name)
			print(" 2. Bloquer les coups")
			print(" 3. Utiliser une potion")
			print(" 4. Utiliser une compétence")
			print(" 0. Passer le tour")
			choice=input(" > ")
			if choice=="1":
				if player.stamina>=player.equipped_weapon.scost:
					atkformula=game.compute_atkformula(enemyBlocks,player.equipped_weapon.dmg,enemy.pres,enemy.blockvalue,enemy.health)
					if duelBonusPlayer is True:
						atkformula+=atkformula*25/100
						duelBonusPlayer=False
					if colereBonus is True:
						atkformula+=atkformula*75/100
						colereBonus=False
					if power_derniersouffle.unlocked is True:
						if player.health<=player.maxhealth*25/100:
							atkformula+=atkformula*15/100
					enemy.health-=atkformula
					player.stamina-=player.equipped_weapon.scost
					engine.clear()
					print(player.name,"attaque",enemy.name,"avec",player.equipped_weapon.name,"et inflige",atkformula,"dégâts !")
					engine.pause()
					playerRound=False
				else:
					engine.displayError("notenoughstamina")
			elif choice=="2":
				engine.clear()
				playerBlocks=True
				playerRound=False
				print(player.name,"bloque les coups !")
				engine.pause()
			elif choice=="3":
				usedPotion=False
				while usedPotion is False:
					engine.clear()
					print("Entrez le nom d'une potion pour l'utiliser.")
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(20)
					for item in inventory.potions:
						if item.amount>0:
							print(" -",item.name,"x",item.amount)
					choice=input(" > ")
					if choice.lower()=="annuler":
						break
					else:
						for potion in inventory.potions:
							if choice.lower()==potion.name.lower():
								player.use_potion(potion)
								usedPotion=True
				if usedPotion is True:
					playerRound=False
			elif choice=="4":
				usedSkill=False
				while usedSkill is False:
					engine.clear()
					print("Entrez le nom d'une compétence pour l'utiliser.")
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(20)
					print("MP :",player.mana,"/",player.maxmana)
					engine.print_separator(20)
					for skill in (sorted(player.skills, key=operator.attrgetter('mcost'))):
						if skill.unlocked is True:
							print("[",skill.mcost,"]"," -",skill.name,":",skill.desc)
					choice=input(" > ")
					if choice.lower()=="annuler":
						break
					else:
						for skill in player.skills:
							if choice.lower()==skill.name.lower():
								if skill.unlocked is True:
									atkformula=player.use_skill(skill,enemy.mres,enemy.health,enemy.stamina,enemy.mana,enemy.maxhealth,enemy.maxstamina,enemy.maxmana)
									if canalisationBonus is True:
										if atkformula>0:
											atkformula=atkformula*2
											enemy.health-=atkformula
											canalisationBonus=False
										else:
											pass
									else:
										enemy.health-=atkformula
									if affaiblissementBonus is True:
										enemy.mres+=50
										affaiblissementBonus=False
									if atkformula>0 or skill.name==skill_bouledefeu.name:
										engine.clear()
										print(player.name,"utilise",skill.name.lower(),"et inflige ",atkformula," dégâts !")
										engine.pause()
										usedSkill=True
									if atkformula is not False:
										if skill.name==skill_duel.name:
											enemy.mana=0
											player.mana=0
											duelBonusEnemy=True
											duelBonusPlayer=True
										if skill.name==skill_foliesanguinaire.name:
											enemy.health-=60-enemy.mres
											foliesanguinaireMalus=True
										if skill.name==skill_protectiondivine.name:
											protectiondivineBonus=True
										if skill.name==skill_canalisation.name:
											canalisationBonus=True
										if skill.name==skill_colere.name:
											colereBonus=True
										if skill.name==skill_affaiblissement.name:
											if enemy.mres<200:
												enemy.mres-=50
											else:
												enemy.mres-=enemy.mres*1.5
											affaiblissementBonus=True
										if skill.name==skill_renforcement.name:
											player.equipped_armor.mres+=25
											renforcementBonus=True
										if skill.name!=skill_bouledefeu.name and skill.name!=skill_chatiment.name:
											engine.clear()
											print(player.name,"utilise",skill.name,"!")
											engine.pause()
										usedSkill=True
								else:
									engine.displayError("invalidChoice")
				if usedSkill is True:   
					playerRound=False
			elif choice=="0":
				playerRound=False
				engine.pause()
			else:
				engine.displayError("invalidchoice")
			if player.health<=0:
				break
			elif enemy.health<=0:
				break
			if playerRound==False: #Enemy AI
				if power_fluxtenebreux.unlocked is True:
					player.health-=10
					player.mana+=10
				if power_endurance.unlocked is True:
					player.stamina+=10
					player.mana+=5
				player.checkStats()
				enemyBlocks=False
				if enemyWeaken is True:
					enemy.mana-=skill_bouledefeu.mcost
					atkformula=15-player.equipped_armor.mres
					if atkformula<0:
						atkformula=0
					if foliesanguinaireMalus is True:
						atkformula=atkformula*2
						foliesanguinaireMalus=False
					if protectiondivineBonus is True:
							atkformula=0
							protectiondivineBonus=False
					if boucliermagiqueBonus is True:
						atkformula=0
						player.mana=player.mana/2
						boucliermagiqueBonus=False
					player.health-=atkformula
					engine.clear()
					print(enemy.name,"utilise",skill_bouledefeu.name,"et inflige",atkformula,"dégâts !")
					engine.pause()
					player.equipped_armor.mres+=50
					enemyWeaken=False
					playerRound=True
					if renforcementBonus is True:
						player.equipped_armor.mres-=25
						renforcementBonus=False
				else:
					enemyDecision=game.ai_decision(enemy)
					if enemyDecision=="heal":
						enemy.use_skill(skill_soin)
						engine.clear()
						print(enemy.name,"utilise",skill_soin.name,"et régénère 25HP !")
						engine.pause()
						playerRound=True
					elif enemyDecision=="attack":
						if playerBlocks is True:
							atkformula=enemy.atk-player.equipped_armor.pres-player.equipped_weapon.blockvalue
						elif playerBlocks is False:
							atkformula=enemy.atk-player.equipped_armor.pres
						if atkformula<0:
							atkformula=0
						if duelBonusEnemy is True:
							atkformula+=atkformula*25/100
							duelBonusEnemy=False
						if foliesanguinaireMalus is True:
							atkformula=atkformula*2
							foliesanguinaireMalus=False
						if protectiondivineBonus is True:
							atkformula=0
							protectiondivineBonus=False
						if boucliermagiqueBonus is True:
							atkformula=0
							player.mana=player.mana/2
							boucliermagiqueBonus=False
						player.health-=atkformula
						enemy.stamina-=enemy.scost
						engine.clear()
						print(enemy.name,"attaque",player.name,"et inflige",atkformula,"dégâts !")
						engine.pause()
						playerRound=True
					elif enemyDecision=="regain_stamina":
						enemy.use_skill(skill_transcendance)
						engine.clear()
						print(enemy.name,"utilise",skill_transcendance.name,"et régénère 25SP !")
						engine.pause()
						playerRound=True
					elif enemyDecision=="block":
						enemyBlocks=True
						engine.clear()
						print(enemy.name,"bloque les coups !")
						engine.pause()
						playerRound=True
					elif enemyDecision=="weaken_and_fire":
						enemyWeaken=True
						if player.maxhealth<200:
							player.equipped_armor.mres-=50
						else:
							player.equipped_armor.mres-=player.equipped_armor.mres*1.5
						engine.clear()
						print(enemy.name,"utilise",skill_affaiblissement.name,"!")
						engine.pause()
						playerRound=True
					elif enemyDecision=="fireball":
						enemy.mana-=skill_bouledefeu.mcost
						atkformula=15-player.equipped_armor.mres
						if atkformula<0:
							atkformula=0
						if foliesanguinaireMalus is True:
							atkformula=atkformula*2
							foliesanguinaireMalus=False
						if protectiondivineBonus is True:
							atkformula=0
							protectiondivineBonus=False
						if boucliermagiqueBonus is True:
							atkformula=0
							player.mana=player.mana/2
							boucliermagiqueBonus=False
						player.health-=atkformula
						engine.clear()
						print(enemy.name,"utilise",skill_bouledefeu.name,"et inflige",atkformula,"dégâts !")
						engine.pause()
						playerRound=True
				enemy.mana+=5
				enemy.stamina+=5
				enemy.checkStats()
			if enemy.health<=0:
				break
			elif player.health<=0:
				break
		if player.health<=0:
			enemy.health=enemy.maxhealth
			enemy.stamina=enemy.maxstamina
			enemy.mana=enemy.maxmana
			game_over()
			return
		elif enemy.health<=0:
			enemy.health=enemy.maxhealth
			enemy.stamina=enemy.maxstamina
			enemy.mana=enemy.maxmana
		if enemyWeaken is True:
			if player.maxhealth<200:
				player.equipped_armor.mres+=50
			else:
				player.equipped_armor.mres+=player.equipped_armor.mres*1.5
		if affaiblissementBonus is True:
			if enemy.mres<200:
				enemy.mres+=50
			else:
				enemy.mres+=enemy.mres*1.5
		if renforcementBonus is True:
			player.equipped_armor.mres-=25
		while True:
			engine.clear()
			print(player.name,"a remporté le combat !")
			print("-------------------")
			print(" 1. Butin")
			print(" 2. Sauvegarder la partie")
			choice=input(" > ")
			if choice=="1":
				engine.clear()
				game.combat_loot(enemy)
				game.combatEndTransition(player.location)
				if power_regeneration.unlocked is True:
					player.health+=15
					player.stamina+=15
					player.mana+=15
					player.checkStats()
				return
			elif choice=="2":
				game.save_game()

	def compute_atkformula(self,enemyBlocks,player_dmg,enemy_pres,enemy_blockvalue,enemy_health):
		atkformula=player_dmg-enemy_pres
		if enemyBlocks is True:
			atkformula-=enemy_blockvalue
		if atkformula<0:
			atkformula=0
		return atkformula

	def ai_decision(self,mob):
		if mob.health>0:
			if mob.health<=mob.maxhealth/2: #Enemy heals
				if game.can_use_skill(skill_soin,mob.mana) is True:
					decision="heal"
					return decision
				else:
					cannot_heal=True
			else:
				cannot_heal=True
			if mob.mana>=skill_affaiblissement.mcost+skill_bouledefeu.mcost:
				decision="weaken_and_fire"
				return decision
			if mob.stamina>=mob.scost:
				decision="attack"
				return decision
			else:
				cannot_attack=True
			if mob.stamina<mob.scost:
				if game.can_use_skill(skill_transcendance,mob.mana) is True:
					decision="regain_stamina"
					return decision
				else:
					cannot_regainstamina=True
			else:
				cannot_regainstamina=True
			if mob.mana>=skill_bouledefeu.mcost:
				decision="fireball"
				return decision
			if cannot_heal is True and cannot_attack is True and cannot_regainstamina is True:
				decision="block"
				return decision
		else:
			engine.clear()
			print("FATAL ERROR")
			engine.pause()
			exit()

	def can_use_skill(self,skill,mana):
		if mana>=skill.mcost:
			return True
		else:
			return False

	def combat_loot(self,mob):
		loot=[]
		engine.clear()
		engine.delayed_print("Vous fouillez le cadavre ...")
		time.sleep(1)
		engine.clear()
		gold=random.randint(25,100)
		if mob.name==boss_khyrrikhu.name or mob.name==boss_grobbit.name or mob.name==boss_limperathris.name or mob.name==boss_flanbit.name:
			gold+=100
		loot_table=[(inventory.gold,52),(epeeRouillee,20),(hacheUsee,15),(armureDeCuir,10),(potionSoin,12),(potionVigueur,8),(potionMagie,8)]
		choices=[]
		for item,weight in loot_table:
			choices.extend([item]*weight)
		for loop in range(4):
			item=random.choice(choices)
			loot.append(item)
		if mob.name==boss_khyrrikhu.name:
			loot.append(inventory.gold)
		lootresults={}
		for item in loot:
			lootresults[item]=0
			lootresults[item]+=1
		# print(lootresults)
		while True:
			engine.clear()
			for item,amount in lootresults.items():
				if item==inventory.gold:
					print(" - Or x ",amount+gold)
				else:
					print(" -",item.name,"x",amount)
			engine.print_separator(20)
			print("1. Ajouter le butin à l'inventaire")
			print("2. Abandonner le butin")
			choice=input(" > ")
			if choice=="1":
				for item,amount in lootresults.items():
					if item==inventory.gold:
						inventory.gold+=amount+gold
					else:
						inventory.add_item(item,amount)
				engine.clear()
				print("Butin ajouté à l'inventaire.")
				engine.pause()
				return
			elif choice=="2":
				return

	def combatEndTransition(self,position):
		engine.clear()
		if position=="Antre de Khyrr Ikhu - Première Salle" or position=="Caverne du Grobbit - Première Salle" or position=="Palais de Limper Athris - Première Salle" or position=="Antichambre du Flan-bit - Première Salle":
			print("Vous avez vaincu votre ennemi. Vous progressez dans le donjon et atteignez la deuxième salle ...")
			engine.pause()
			if position=="Antre de Khyrr Ikhu - Première Salle":
				player.location="Antre de Khyrr Ikhu - Deuxième Salle"
			elif position=="Caverne du Grobbit - Première Salle":
				player.location="Caverne du Grobbit - Deuxième Salle"
			elif position=="Palais de Limper Athris - Première Salle":
				player.location="Palais de Limper Athris - Deuxième Salle"
			elif position=="Antichambre du Flan-bit - Première Salle":
				player.location="Antichambre du Flan-bit - Deuxième Salle"
			return
		elif position=="Antre de Khyrr Ikhu - Deuxième Salle" or position=="Caverne du Grobbit - Deuxième Salle" or position=="Palais de Limper Athris - Deuxième Salle" or position=="Antichambre du Flan-bit - Deuxième Salle":
			print("Le monstre s'écroule à terre. Vous avancez vers la troisième et dernière salle, où vous attend un ennemi bien plus puissant !")
			engine.pause()
			if position=="Antre de Khyrr Ikhu - Deuxième Salle":
				player.location="Antre de Khyrr Ikhu - Troisième Salle"
			elif position=="Caverne du Grobbit - Deuxième Salle":
				player.location="Caverne du Grobbit - Troisième Salle"
			elif position=="Palais de Limper Athris - Deuxième Salle":
				player.location="Palais de Limper Athris - Troisième Salle"
			elif position=="Antichambre du Flan-bit - Deuxième Salle":
				player.location="Antichambre du Flan-bit - Troisième Salle"
			return
		elif position=="Antre de Khyrr Ikhu - Troisième Salle":
			print("Khyrr Ikhu est vaincu. Le titan tombe au sol dans un bruit sourd, poussant un ultime hurlement.")
			time.sleep(1)
			print("Un passage semble s'ouvrir dans les murs de feuilles du temple. Vous vous y engouffrez et rejoignez votre repaire.")
			if player.khyrrikhuDefeated is False:
				print("La Caverne du Grobbit est désormais accessible.")
				engine.pause()
				game.dungeonEnd("Khyrr Ikhu","son antre",fouetDeKhyrrIkhu,armureVegetale,"la compétence",skill_chatiment)
				player.grobbit=True
				player.khyrrikhuDefeated=True
				player.location="Repaire"
				return
			else:
				print("Vous avez ramassé",fouetDeKhyrrIkhu.name,"et",armureVegetale.name,"sur le cadavre du boss.")
				engine.pause()
		elif position=="Caverne du Grobbit - Troisième Salle":
			print("Le Grobbit, pris de spasmes violents, se vide de son sang, agitant son corps gras et disgracieux d'une manière pathétique. Il s'écroule finalement sur le sol froid et humide.")
			time.sleep(1)
			print("Derrière lui, un halo blanc attire votre regard et vous sentez l'air frais sur votre visage. Vous vous engouffrez dans une crevasse et rejoignez votre repaire.")
			if player.grobbitDefeated is False:
				print("Le Palais de Limper Athris est désormais accessible.")
				engine.pause()
				game.dungeonEnd("Le Grobbit","sa grotte",massueDuGrobbit,armureRocailleuse,"le pouvoir",power_renaissance)
				player.limperathris=True
				player.location="Repaire"
				return
			else:
				print("Vous avez ramassé",massueDuGrobbit.name,"et",armureRocailleuse,"sur le cadavre du boss.")
				engine.pause()
		elif position=="Palais de Limper Athris - Troisième Salle":
			print("Un coup de grâce achève Limper Athris. Le trône impérial est laissé vacant, les gardes du palais prennent la fuite.")
			time.sleep(1)
			print("Une porte dorée s'ouvre derrière le trône gigantesque. Vous passez le seuil et regagnez votre repaire.")
			if player.limperathrisDefeated is False:
				print("L'Antichambre du Flan-bit est désormais accessible.")
				engine.pause()
				game.dungeonEnd("Limper Athris","son palais",rapiereDeLimperAthris,armureImperiale,"la compétence",skill_duel)
				player.flanbit=True
				player.location="Repaire"
				return
			else:
				print("Vous avez ramassé",rapiereDeLimperAthris,"et",armureImperiale,"sur le cadavre du boss.")
				engine.pause()
		elif position=="Antichambre du Flan-bit - Troisième Salle":
			print("Le colossal Flan-bit est terrassé. L'immense masse gélatineuse explose en mille morceaux translucides qui viennent recouvrir les parois de l'antichambre.")
			time.sleep(1)
			print("Un passage secret s'ouvre dans une paroi gélatineuse et vous vous y engouffrez pour rentrer à votre repaire.")
			if player.flanbitDefeated is False:
				engine.pause()
				game.dungeonEnd("Le Flan-bit","son antichambre",sceptreDuFlanBit,armureGelatineuse,"le pouvoir",power_derniersouffle)
				engine.clear()
				print("Votre quête est terminée ! Vous pouvez désormais refaire tous les donjons si vous le souhaitez. Félicitations, aventurier !")
				engine.pause()
				player.location="Repaire"
				return
			else:
				print("Vous avez ramassé",sceptreDuFlanBit,"et",armureGelatineuse,"sur le cadavre du boss.")
				engine.pause()
		player.health+=player.maxhealth/4
		player.stamina+=player.maxstamina/4
		player.mana+=player.maxmana/4
		player.checkStats()
		player.location="Repaire"
		return

	def dungeonEnd(self,bossname,bosslocation,weapon,armor,skllpwrtype,skllpwr):
		engine.clear()
		print(bossname,"a été vaincu(e) ! Vous avez triomphé de",bosslocation,"et avez récupéré sa gemme de pouvoir.")
		engine.print_separator(30)
		print("Vos HP, SP et MP ont été augmentés par 50. Vous avez également ramassé l'arme",weapon.name,"et l'armure",armor.name,"sur le cadavre du boss.")
		print("En ramassant la gemme de pouvoir, vous avez appris",skllpwrtype,skllpwr.name,".")
		engine.pause()
		inventory.add_item(weapon,1)
		inventory.add_item(armor,1)
		player.unlock_skllpwr(skllpwr)
		player.maxhealth+=50
		player.maxstamina+=50
		player.maxmana+=50
		player.health=player.maxhealth
		player.stamina=player.maxstamina
		player.mana=player.maxmana

	def load_weapons(self):
		datafiles=os.listdir('data/weapons/')
		for file in datafiles:
			file='data/weapons/{}'.format(file)
			with open(file,'rb') as weaponfile:
				weapon_data=pickle.load(weaponfile)
			weaponVar=weapon_data["var"]
			weaponName=weapon_data["name"]
			weaponDesc=weapon_data["desc"]
			weaponDmg=weapon_data["dmg"]
			weaponScost=weapon_data["scost"]
			weaponBlockvalue=weapon_data["blockvalue"]
			weaponPrice=weapon_data["price"]
			globals()[weaponVar]=Weapon(weaponName,weaponDesc,weaponDmg,weaponScost,weaponBlockvalue,weaponPrice,0)
			inventory.weapons[globals()[weaponVar]]=weaponName
		globals()["weaponNone"]=Weapon("Aucune arme","",0,0,0,0,0)
		inventory.weapons[globals()["weaponNone"]]="Aucune arme"

	def load_armors(self):
		datafiles=os.listdir('data/armors/')
		for file in datafiles:
			file='data/armors/{}'.format(file)
			with open(file,'rb') as armorfile:
				armor_data=pickle.load(armorfile)
			armorVar=armor_data["var"]
			armorName=armor_data["name"]
			armorDesc=armor_data["desc"]
			armorPres=armor_data["pres"]
			armorMres=armor_data["mres"]
			armorPrice=armor_data["price"]
			globals()[armorVar]=Armor(armorName,armorDesc,armorPres,armorMres,armorPrice,0)
			inventory.armors[globals()[armorVar]]=armorName
		globals()["armorNone"]=Armor("Aucune armure","",0,0,0,0)
		inventory.armors[globals()["armorNone"]]="Aucune armure"

	def load_potions(self):
		globals()["potionSoin"]=Potion("Potion de soin","Restaure 25 points de santé.",25,15,0)
		globals()["potionVigueur"]=Potion("Potion de vigueur","Restaure 25 points de vigueur.",25,15,0)
		globals()["potionMagie"]=Potion("Potion de magie","Restaure 25 points de magie.",25,15,0)
		globals()["potionSuicide"]=Potion("Potion de suicide","Provoque une mort immédiate.",0,100,0)
		globals()["potionOubli"]=Potion("Potion d'oubli","Sert à désapprendre un pouvoir.",0,200,0)
		inventory.potions[globals()["potionSoin"]]="Potion de soin"
		inventory.potions[globals()["potionVigueur"]]="Potion de vigueur"
		inventory.potions[globals()["potionMagie"]]="Potion de magie"
		inventory.potions[globals()["potionSuicide"]]="Potion de suicide"
		inventory.potions[globals()["potionOubli"]]="Potion d'oubli"

	def load_enemies(self):
		# globals()["nom"]=Enemy("nom",health,maxhealth,stamina,maxstamina,mana,maxmana,atk,scost,pres,mres,blockvalue)
		globals()["guerrierTribal"]=Enemy("Guerrier tribal",75,75,50,50,50,50,20,10,7,7,5)
		globals()["colosseTribal"]=Enemy("Colosse tribal",100,100,80,80,15,15,25,12,15,-5,15)
		globals()["boss_khyrrikhu"]=Enemy("Khyrr Ikhu",150,150,60,60,80,80,30,25,15,30,8)

		globals()["soldatPelagique"]=Enemy("Soldat pélagique",100,100,85,85,55,55,45,20,20,20,15)
		globals()["mastodontePelagique"]=Enemy("Mastodonte pélagique",150,150,100,100,40,40,50,40,25,15,20)
		globals()["boss_grobbit"]=Enemy("Le Grobbit",180,180,120,120,50,50,45,35,30,10,25)

		globals()["gardeImperial"]=Enemy("Garde impérial",150,150,100,100,80,80,55,30,30,30,25)
		globals()["duellisteImperial"]=Enemy("Duelliste impérial",120,120,100,100,55,55,75,25,25,25,25)
		globals()["boss_limperathris"]=Enemy("Limper Athris",220,220,150,150,75,75,55,40,40,20,40)

		globals()["princeGelatineux"]=Enemy("Prince gélatineux",185,185,120,120,100,100,115,40,40,40,30)
		globals()["baronGelatineux"]=Enemy("Baron gélatineux",230,230,150,150,55,55,110,60,40,-5,50)
		globals()["boss_flanbit"]=Enemy("Le Flan-bit",300,300,200,200,150,150,120,50,50,50,25)

	def load_skills(self):
		# globals()["nom"]=Skill("nom","description",mcost,price)
		globals()["skill_soin"]=Skill("Soin","Soigne 25HP.",20,0)
		globals()["skill_rituel"]=Skill("Rituel","Transfère 25HP en 50MP.",25,0)
		globals()["skill_transcendance"]=Skill("Transcendance","Transfère 25SP en 25MP.",25,0)
		globals()["skill_bouledefeu"]=Skill("Boule de feu","Inflige 15 points de dégât.",20,0)
		globals()["skill_affaiblissement"]=Skill("Affaiblissement","Diminue la résistance magique de l'ennemi de -50 pour la prochaine compétence offensive lancée.",35,50)
		globals()["skill_renforcement"]=Skill("Renforcement","Augmente votre résistance magique de +25 pour la prochaine compétence offensive ennemie lancée.",55,50)
		globals()["skill_chatiment"]=Skill("Châtiment","Inflige 50% des HP max de l'ennemi en dégâts. Consomme 75% de vos MP.",100,150)
		globals()["skill_duel"]=Skill("Duel","Réduit vos MP et ceux de l'ennemi à 0. Augmente vos dégâts physiques et ceux de l'ennemi de 25% pour la prochaine attaque.",80,100)
		globals()["skill_foliesanguinaire"]=Skill("Folie sanguinaire","Vole 60HP à l'ennemi. Les dégâts de la prochaine attaque reçue sont multipliés par 2.",60,150)
		globals()["skill_protectiondivine"]=Skill("Protection divine","Les dégâts de la prochaine attaque reçue sont annulés.",80,200)
		globals()["skill_canalisation"]=Skill("Canalisation","La prochaine compétence offensive inflige 100% de dégâts supplémentaires.",90,250)
		globals()["skill_colere"]=Skill("Colère","La prochaine attaque physique inflige 75% de dégâts supplémentaires.",85,215) 
		player.skills[globals()["skill_soin"]]="Soin"
		player.skills[globals()["skill_rituel"]]="Rituel"
		player.skills[globals()["skill_transcendance"]]="Transcendance"
		player.skills[globals()["skill_bouledefeu"]]="Boule de feu"
		player.skills[globals()["skill_affaiblissement"]]="Affaiblissement"
		player.skills[globals()["skill_renforcement"]]="Renforcement"
		player.skills[globals()["skill_chatiment"]]="Châtiment"
		player.skills[globals()["skill_duel"]]="Duel"
		player.skills[globals()["skill_foliesanguinaire"]]="Folie sanguinaire"
		player.skills[globals()["skill_protectiondivine"]]="Protection divine"
		player.skills[globals()["skill_canalisation"]]="Canalisation"
		player.skills[globals()["skill_colere"]]="Colère"

	def load_powers(self):
		# globals()["nom"]=Power("nom","description",price)
		globals()["power_endurance"]=Power("Endurance","Vous regagnez +10SP et +5MP par tour.",0)
		globals()["power_sangancien"]=Power("Sang ancien","Vos compétences offensives infligent +10% de dégâts supplémentaires.",0)
		globals()["power_regeneration"]=Power("Régénération","Vous regénérez +15 à vos HP, MP et SP entre chaque combat.",50)
		globals()["power_boucliermagique"]=Power("Bouclier magique","Lorsque vous subissez la première attaque de l'ennemi, la moitié de vos MP sont consommés et vos HP restent intacts.",100)
		globals()["power_fluxtenebreux"]=Power("Flux ténébreux","-10HP et +10MP par tour.",100) 
		globals()["power_renaissance"]=Power("Renaissance","Une fois par combat, lorsque vos HP tombent à 50%, vous regagnez 25% de vos SP.",120) 
		globals()["power_derniersouffle"]=Power("Dernier souffle","Lorsque vos HP tombent à 25%, vos attaques physiques infligent 15% de dégâts supplémentaires.",350)
		player.powers[globals()["power_endurance"]]="Endurance"
		player.powers[globals()["power_sangancien"]]="Sang ancien"
		player.powers[globals()["power_regeneration"]]="Régénération"
		player.powers[globals()["power_boucliermagique"]]="Bouclier magique"
		player.powers[globals()["power_fluxtenebreux"]]="Flux ténébreux"
		player.powers[globals()["power_renaissance"]]="Renaissance"
		player.powers[globals()["power_derniersouffle"]]="Dernier souffle"

	def reset_stats(self):
		for weapon in inventory.weapons:
			weapon.amount=0
		for weapon in list(inventory.weapons):
			del inventory.weapons[weapon]

		for armor in inventory.armors:
			armor.amount=0
		for armor in list(inventory.armors):
			del inventory.armors[armor]

		for potion in inventory.potions:
			potion.amount=0
		for potion in list(inventory.potions):
			del inventory.potions[potion]

		for skill in player.skills:
			skill.unlocked=False
		for skill in list(player.skills):
			del player.skills[skill]

		for power in player.powers:
			power.unlocked=False
		for power in list(player.powers):
			del player.powers[power]

	def save_inventory(self,filename):
		filename="{}_inventorystats.arws".format(filename)
		inventory_data_general={"weapons":inventory.weapons,
								"potions":inventory.potions,
								"armors":inventory.armors,
								"gold":inventory.gold}
		inventory_data_weapons={}
		inventory_data_armors={}
		inventory_data_potions={}

		for weapon in inventory.weapons:
			savename="{}_amnt".format(weapon.name)
			inventory_data_weapons[savename]=weapon.amount
		for armor in inventory.armors:
			savename="{}_amnt".format(armor.name)
			inventory_data_armors[savename]=armor.amount
		for potion in inventory.potions:
			savename="{}_amnt".format(potion.name)
			inventory_data_potions[savename]=potion.amount
		try:
			with open(filename,"wb") as file:
				pickle.dump(inventory_data_general,file)
				pickle.dump(inventory_data_weapons,file)
				pickle.dump(inventory_data_armors,file)
				pickle.dump(inventory_data_potions,file)
			successfulsave_inventory=True
			return successfulsave_inventory
		except IOError:
			successfulsave_inventory=False
			return successfulsave_inventory

	def load_inventory(self,filename):
		filename="{}_inventorystats.arws".format(filename)
		try:
			with open(filename,"rb") as file:
				inventory_data_general=pickle.load(file)
				inventory_data_weapons=pickle.load(file)
				inventory_data_armors=pickle.load(file)
				inventory_data_potions=pickle.load(file)
			inventory.weapons=inventory_data_general["weapons"]
			inventory.armors=inventory_data_general["armors"]
			inventory.potions=inventory_data_general["potions"]
			inventory.gold=inventory_data_general["gold"]
			for weapon in inventory.weapons:
				weapon.amount=inventory_data_weapons["{}_amnt".format(weapon.name)]
			for armor in inventory.armors:
				armor.amount=inventory_data_armors["{}_amnt".format(armor.name)]
			for potion in inventory.potions:
				potion.amount=inventory_data_potions["{}_amnt".format(potion.name)]
			successfulload_inventory=True
			return successfulload_inventory
		except IOError:
			successfulload_inventory=False
			return successfulload_inventory

	def save_player(self,filename):
		filename="{}_playerstats.arws".format(filename)
		player_data={"name":player.name,
					 "skills":player.skills,
					 "powers":player.powers,
					 "maxhealth":player.maxhealth,
					 "maxstamina":player.maxstamina,
					 "maxmana":player.maxmana,
					 "health":player.health,
					 "stamina":player.stamina,
					 "mana":player.mana,
					 "equipped_weapon":player.equipped_weapon,
					 "equipped_armor":player.equipped_armor,
					 "location":player.location,
					 "khyrrikhu":player.khyrrikhu,
					 "grobbit":player.grobbit,
					 "limperathris":player.limperathris,
					 "flanbit":player.flanbit,
					 "khyrrikhuDefeated":player.khyrrikhuDefeated,
					 "grobbitDefeated":player.grobbitDefeated,
					 "limperathrisDefeated":player.limperathrisDefeated,
					 "flanbitDefeated":player.flanbitDefeated}
		player_data_skills={}
		player_data_powers={}

		for skill in player.skills:
			savename="{}_unlckd".format(skill.name)
			player_data_skills[savename]=skill.unlocked
		for power in player.powers:
			savename="{}_unlckd".format(power.name)
			player_data_powers[savename]=power.unlocked
		try:
			with open(filename,"wb") as file:
				pickle.dump(player_data,file)
				pickle.dump(player_data_skills,file)
				pickle.dump(player_data_powers,file)
			successfulsave_player=True
			return successfulsave_player
		except IOError:
			successfulsave_player=False
			return successfulsave_player

	def load_player(self,filename):
		filename="{}_playerstats.arws".format(filename)
		try:
			with open(filename,"rb") as file:
				player_data=pickle.load(file)
				player_data_skills=pickle.load(file)
				player_data_powers=pickle.load(file)
			player.name=player_data["name"]
			player.maxhealth=player_data["maxhealth"]
			player.maxstamina=player_data["maxstamina"]
			player.maxmana=player_data["maxmana"]
			player.health=player_data["health"]
			player.stamina=player_data["stamina"]
			player.mana=player_data["mana"]
			player.equipped_weapon=player_data["equipped_weapon"]
			player.equipped_armor=player_data["equipped_armor"]
			player.location=player_data["location"]
			player.khyrrikhu=player_data["khyrrikhu"]
			player.grobbit=player_data["grobbit"]
			player.limperathris=player_data["limperathris"]
			player.flanbit=player_data["flanbit"]
			player.khyrrikhuDefeated=player_data["khyrrikhuDefeated"]
			player.grobbitDefeated=player_data["grobbitDefeated"]
			player.limperathrisDefeated=player_data["limperathrisDefeated"]
			player.flanbitDefeated=player_data["flanbitDefeated"]
			for skill in player.skills:
				skill.unlocked=player_data_skills["{}_unlckd".format(skill.name)]
			for power in player.powers:
				power.unlocked=player_data_powers["{}_unlckd".format(power.name)]
			successfulload_player=True
			return successfulload_player
		except IOError:
			successfulload_player=False
			return successfulload_player

	def save_game(self):
		engine.clear()
		print("Entrez le nom de votre fichier de sauvegarde ou entrez \"annuler\" pour partir.")
		filename=input(" > ")
		if filename=="annuler":
			return
		else:
			engine.clear()
			print("Sauvegarde ...")
			successfulsave_player=game.save_player(filename)
			if successfulsave_player is False:
				engine.displayError("invalidfilename")
				game.save_game()
			else:
				successfulsave_inventory=game.save_inventory(filename)
				if successfulsave_inventory is False:
					engine.displayError("invalidfilename")
					game.save_game()
				else:
					print("Partie sauvegardée.")
					engine.pause()

	def load_game(self):
		engine.clear()
		print("Entrez le nom de votre fichier à charger ou entrez \"annuler\" pour partir.")
		filename=input(" > ")
		if filename=="annuler":
			return
		else:
			engine.clear()
			print("Chargement ...")
			successfulload_player=game.load_player(filename)
			if successfulload_player is False:
				engine.displayError("invalidfilename")
				game.load_game()
			else:
				successfulload_inventory=game.load_inventory(filename)
				if successfulload_inventory is False:
					engine.displayError("invalidfilename")
					game.load_game()
				else:
					print("Partie chargée.")
					engine.pause()

	def shop(self):
		inShop=True
		while inShop is True:
			engine.clear()
			print("Bienvenue au marché noir,",player.name,"!")
			engine.displayGold()
			engine.print_separator(40)
			print("1. Acheter")
			print("2. Vendre")
			print("3. Sortir")
			choice=input(" > ")
			if choice=="1":
				while True:
					engine.clear()
					print("Acheter")
					engine.displayGold()
					print("(entrez le nom d'une catégorie pour voir son contenu.)")
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(25)
					print(" - Armes")
					print(" - Armures")
					print(" - Potions")
					print(" - Pouvoirs")
					print(" - Compétences")

					choice=input(" > ")
					if choice.lower()=="armes":
						while True:
							engine.clear()
							print("Acheter des armes")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in (sorted(inventory.weapons, key=operator.attrgetter('price'))):
								if item.name.lower()!="aucune arme" and item.name.lower()!=fouetDeKhyrrIkhu.name.lower() and item.name.lower()!=massueDuGrobbit.name.lower() and item.name.lower()!=rapiereDeLimperAthris.name.lower() and item.name.lower()!=sceptreDuFlanBit.name.lower():
										print("[",item.price,"]"," -",item.name)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for weapon in inventory.weapons:
									if choice.lower()==weapon.name.lower():
										if weapon.name.lower()!="aucune arme" and weapon.name.lower()!=fouetDeKhyrrIkhu.name.lower() and weapon.name.lower()!=massueDuGrobbit.name.lower() and weapon.name.lower()!=rapiereDeLimperAthris.name.lower() and weapon.name.lower()!=sceptreDuFlanBit.name.lower():
											game.buy_item(weapon,"weapon")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="armures":
						while True:
							engine.clear()
							print("Acheter des armures")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in (sorted(inventory.armors, key=operator.attrgetter('price'))):
								if item.name.lower()!="aucune armure" and item.name.lower()!=armureVegetale.name.lower() and item.name.lower()!=armureRocailleuse.name.lower() and item.name.lower()!=armureImperiale.name.lower() and item.name.lower()!=armureGelatineuse.name.lower():
									print("[",item.price,"]"," -",item.name)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for armor in inventory.armors:
									if choice.lower()==armor.name.lower():
										if armor.name.lower()!="aucune armure" and armor.name.lower()!=armureVegetale.name.lower() and armor.name.lower()!=armureRocailleuse.name.lower() and armor.name.lower()!=armureImperiale.name.lower() and armor.name.lower()!=armureGelatineuse.name.lower():
											game.buy_item(armor,"armor")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="potions":
						while True:
							engine.clear()
							print("Acheter des potions")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in (sorted(inventory.potions, key=operator.attrgetter('price'))):
								print("[",item.price,"]"," -",item.name)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for potion in inventory.potions:
									if choice.lower()==potion.name.lower():
										game.buy_item(potion,"potion")
					elif choice.lower()=="pouvoirs":
						while True:
							engine.clear()
							print("Acheter des pouvoirs")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for power in (sorted(player.powers, key=operator.attrgetter('price'))):
								if power.unlocked is False:
									print("[",power.price,"]"," -",power.name)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for power in player.powers:
									if choice.lower()==power.name.lower():
										if power.unlocked is False:
											game.buy_item(power,"power")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="compétences":
						while True:
							engine.clear()
							print("Acheter des compétences")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for skill in (sorted(player.skills, key=operator.attrgetter('price'))):
								if skill.unlocked is False:
									print("[",skill.price,"]"," -",skill.name)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for skill in player.skills:
									if choice.lower()==skill.name.lower():
										if skill.unlocked is False:
											game.buy_item(skill,"skill")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="annuler":
						break
			elif choice=="2":
				while True:
					engine.clear()
					print("Vendre")
					engine.displayGold()
					print("(entrez le nom d'une catégorie pour voir son contenu.)")
					engine.print_separator(25)
					print(" - Armes")
					print(" - Armures")
					print(" - Potions")
					choice=input(" > ")
					if choice.lower()=="armes":
						while True:
							engine.clear()
							print("Vendre des armes")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in inventory.weapons:
								if item.name.lower()!="aucune arme":
									if item.amount>0:
										print(" -",item.name,"x",item.amount)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for weapon in inventory.weapons:
									if choice.lower()==weapon.name.lower():
										if weapon.amount>0 and weapon.name.lower()!="aucune arme":
											game.sell_item(weapon,"weapon")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="armures":
						while True:
							engine.clear()
							print("Vendre des armures")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in inventory.armors:
								if item.name.lower()!="aucune armure":
									if item.amount>0:
										print(" -",item.name,"x",item.amount)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for armor in inventory.armors:
									if choice.lower()==armor.name.lower():
										if armor.amount>0 and armor.name.lower()!="aucune armure":
											game.sell_item(armor,"armor")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="potions":
						while True:
							engine.clear()
							print("Vendre des potions")
							engine.displayGold()
							print("(entrez \'annuler\' pour partir.)")
							engine.print_separator(20)
							for item in inventory.potions:
								if item.amount>0:
									print(" -",item.name,"x",item.amount)
							choice=input(" > ")
							if choice.lower()=="annuler":
								break
							else:
								for potion in inventory.potions:
									if choice.lower()==potion.name.lower():
										if potion.amount>0:
											game.sell_item(potion,"potion")
										else:
											engine.displayError("invalidchoice")
					elif choice.lower()=="annuler":
						break
			elif choice=="3":
				inShop=False

	def buy_item(self,item,type):
		while True:
			engine.clear()
			print("Acheter :",item.name)
			print(item.desc)
			engine.displayGold()
			if type=="weapon":
				engine.print_separator(20)
				print("Arme équipée (",player.equipped_weapon.name,") -->",item.name)
				print("DMG :",player.equipped_weapon.dmg,"-->",item.dmg)
				print("VIG :",player.equipped_weapon.scost,"-->",item.scost)
				print("DEF :",player.equipped_weapon.blockvalue,"-->",item.blockvalue)
			if type=="armor":
				engine.print_separator(20)
				print("Armure équipée (",player.equipped_armor.name,") -->",item.name)
				print("PHR :",player.equipped_armor.pres,"-->",item.pres)
				print("MGR :",player.equipped_armor.mres,"-->",item.mres)
			engine.print_separator(20)
			if type=="weapon" or type=="armor" or type=="potion":
				print("Possédé(e) :",item.amount)
			print("Prix :",item.price)
			try:
				if type=="power" or type=="skill":
					if type=="power":
						print("Apprendre le pouvoir ? Répondez par oui ou non.")
					if type=="skill":
						print("Apprendre la compétence ? Répondez par oui ou non.")
					choice=input(" > ")
					if choice.lower()=="oui":
						if inventory.gold>=item.price:
							inventory.gold-=item.price
							item.unlocked=True
							engine.clear()
							if type=="power":
								print("Le pouvoir",item.name,"a été appris (",item.price,"or dépensé ).")
							if type=="skill":
								print("La compétence",item.name,"a été apprise (",item.price,"or dépensé ).")
							engine.pause()
							break
						else:
							engine.displayError("notenoughgold")
					elif choice.lower()=="non":
						break
				elif type=="armor" or type=="weapon" or type=="potion":
					amountToBuy=int(input("Quantité à acheter : "))
					if amountToBuy*item.price<=inventory.gold and amountToBuy>0:
						removedGold=item.price*amountToBuy
						inventory.gold-=removedGold
						inventory.add_item(item,amountToBuy)
						engine.clear()
						print(amountToBuy,item.name,"acheté (",removedGold,"or dépensé ).")
						engine.pause()
						break
					elif amountToBuy==0:
						break
					elif amountToBuy*item.price>inventory.gold:
						engine.displayError("notenoughgold")
				else:
					engine.displayError("incorrectvalue")
			except ValueError:
				engine.displayError("mustenternumbers")

	def sell_item(self,item,type):
		while True:
			engine.clear()
			print("Vendre :",item.name)
			engine.displayGold()
			engine.print_separator(20)
			print("Possédé :",item.amount)
			print("Prix :",item.price)
			try:
				amountToSell=int(input("Quantité à vendre : "))
				if amountToSell<=item.amount and amountToSell>0:
					acquiredGold=item.price*amountToSell
					inventory.gold+=acquiredGold
					inventory.remove_item(item,amountToSell)
					if type.lower()=="weapon":
						if item.name==player.equipped_weapon.name:
							if item.amount==0:
								player.equipped_weapon=weaponNone
					elif type.lower()=="armor":
						if item.name==player.equipped_armor.name:
							if item.amount==0:
								player.equipped_armor=armorNone
					elif type.lower()=="potion":
						pass
					engine.clear()
					print(amountToSell,item.name,"vendu(s) (",acquiredGold," or acquis).")
					engine.pause()
					break
				elif amountToSell==0:
					break
				else:
					engine.displayError("incorrectvalue")
			except ValueError:
				engine.displayError("mustenternumbers")

			
class Inventory(object):

	def __init__(self):
		self.potions={}
		self.weapons={}
		self.armors={}
		self.books={}
		self.items={}
		self.gold=0

	def add_item(self,item,amount):
		for target in inventory.weapons:
			if item.name==target.name:
				target.amount+=amount
		for target in inventory.armors:
			if item.name==target.name:
				target.amount+=amount
		for target in inventory.potions:
			if item.name==target.name:
				target.amount+=amount

	def remove_item(self,item,amount):
		item.amount-=amount
		if item.amount<0:
			item.amount=0

	def display_items(self):
		inInventory=True
		while inInventory is True:
			engine.clear()
			print("Inventaire")
			print("(entrez le nom d'une catégorie pour voir ses objets.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(20)
			print(" - Armes")
			print(" - Armures")
			print(" - Potions")
			engine.print_separator(20)
			print("Or possédé :",self.gold)
			choice=input(" > ")
			if choice.lower()=="armes":
				inventory.display_weapons()
			elif choice.lower()=="armures":
				inventory.display_armors()
			elif choice.lower()=="potions":
				inventory.display_potions()
			elif choice.lower()=="annuler":
				inInventory=False
			else:
				engine.displayError("invalidChoice")

	def display_weapons(self):
		inWeaponsInventory=True
		while inWeaponsInventory is True:
			engine.clear()
			print("Inventaire des armes")
			print("(entrez le nom d'une arme pour voir ses caractéristiques.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(20)
			for item in inventory.weapons:
				if item.name.lower()!="aucune arme":
					if item.amount>0:
						print(" -",item.name,"x",item.amount)
			choice=input(" > ")
			if choice.lower()=="annuler":
				inWeaponsInventory=False
			else:
				for weapon in self.weapons:
					if choice.lower()==weapon.name.lower():
						if weapon.amount>0 and weapon.name.lower()!="aucune arme":
							inventory.display_weaponStats(weapon)
						else:
							engine.displayError("invalidchoice")

	def display_armors(self):
		inArmorsInventory=True
		while inArmorsInventory is True:
			engine.clear()
			print("Inventaire des armures")
			print("(entrez le nom d'une armure pour voir ses caractéristiques.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(20)
			for item in inventory.armors:
				if item.name.lower()!="aucune armure":
					if item.amount>0:
						print(" -",item.name,"x",item.amount)
			choice=input(" > ")
			if choice.lower()=="annuler":
				inArmorsInventory=False
			else:
				for armor in inventory.armors:
					if choice.lower()==armor.name.lower():
						if armor.amount>0 and armor.name.lower()!="aucune armure":
							inventory.display_armorStats(armor)
						else:
							engine.displayError("invalidchoice")

	def display_potions(self):
		inPotionsInventory=True
		while inPotionsInventory is True:
			engine.clear()
			print("Inventaire des potions")
			print("(entrez le nom d'une potion pour voir ses caractéristiques.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(20)
			for item in inventory.potions:
				if item.amount>0:
					print(" -",item.name,"x",item.amount)
			choice=input(" > ")
			if choice.lower()=="annuler":
				inPotionsInventory=False
			else:
				for potion in inventory.potions:
					if choice.lower()==potion.name.lower():
						if potion.amount>0:
							inventory.display_potionStats(potion)
						else:
							engine.displayError("invalidchoice")
			
	def display_weaponStats(self,weapon):
		engine.clear()
		print(weapon.name)
		engine.print_separator(15)                                      
		print("\"",weapon.desc,"\"")
		print("DEG :",weapon.dmg)
		print("VIG :",weapon.scost)
		print("DEF :",weapon.blockvalue)
		print("PRX :",weapon.price)
		print("QTN :",weapon.amount)
		engine.pause()

	def display_armorStats(self,armor):
		engine.clear()
		print(armor.name)
		engine.print_separator(15)
		print("\"",armor.desc,"\"")
		print("PHR :",armor.pres)
		print("MGR :",armor.mres)
		print("PRX :",armor.price)
		print("QTN :",armor.amount)
		engine.pause()

	def display_potionStats(self,potion):
		engine.clear()
		print(potion.name)
		engine.print_separator(15)
		print("\"",potion.desc,"\"")
		print("PRX :",potion.price)
		print("QTN :",potion.amount)
		engine.pause()

class Player(object):

	def __init__(self,name,inventory,equipped_weapon,equipped_armor):
		self.skills={}
		self.powers={}
		self.name=name
		self.maxhealth=100
		self.health=self.maxhealth
		self.maxstamina=100
		self.stamina=self.maxstamina
		self.maxmana=100
		self.mana=self.maxmana
		self.inventory=inventory
		self.equipped_weapon=equipped_weapon
		self.equipped_armor=equipped_armor
		self.location="Repaire"
		self.khyrrikhu=False
		self.grobbit=False
		self.limperathris=False
		self.flanbit=False
		self.khyrrikhuDefeated=False
		self.grobbitDefeated=False
		self.limperathrisDefeated=False
		self.flanbitDefeated=False

	def unlock_skllpwr(self,skllpwr):
		skllpwr.unlocked=True

	def use_potion(self,potion):
		if potion.amount>0:
			if potion.name.lower()=="potion de soin":
				self.health+=potion.varamount
				potiontype="HP"
			elif potion.name.lower()=="potion de vigueur":
				self.stamina+=potion.varamount
				potiontype="SP"
			elif potion.name.lower()=="potion de magie":
				self.mana+=potion.varamount
				potiontype="MP"
			elif potion.name.lower()=="potion de suicide":
				self.health=0
			elif potion.name.lower()=="potion d'oubli":
				forgottenPower=False
				inForgetPower=True
				while inForgetPower is True:
					engine.clear()
					print("Entrez le nom d'un pouvoir pour le désapprendre. Cette action est irréversible !")
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(30)
					for power in player.powers:
						if power.unlocked is True:
							print(" -",power.name,":",power.desc)
					choice=input(" > ")
					if choice.lower()=="annuler":
						inForgetPower=False
					else:
						for power in player.powers:
							if choice.lower()==power.name.lower():
								if power.unlocked is True:
									power.unlocked=False
									forgottenPower=True
									engine.clear()
									print("Le pouvoir",power.name,"a été désappris.")
									engine.pause()
									inForgetPower=False
								else:
									engine.displayError("invalidchoice")
				player.checkStats()
				if forgottenPower is False:
					return
			self.inventory.remove_item(potion,1)
			engine.clear()
			if potion.name.lower()==potionSoin.name.lower() or potion.name.lower()==potionVigueur.name.lower() or potion.name.lower()==potionMagie.name.lower():
				print(potion.name,"utilisée, 25",potiontype,"regagnés.")
			else:
				print(potion.name,"utilisée.")
			engine.pause()
			player.checkStats()
		else:
			engine.displayError("notEnoughPotions")

	def use_skill(self,skill,enemy_mres,enemy_health,enemy_stamina,enemy_mana,enemy_maxhealth,enemy_maxstamina,enemy_maxmana):
		if self.mana>=skill.mcost:
			if skill.name==skill_soin.name:
				self.health+=25
				self.mana-=skill.mcost
			elif skill.name==skill_rituel.name:
				self.health-=25
				self.mana+=50
			elif skill.name==skill_transcendance.name:
				self.stamina-=25
				self.mana+=25
			elif skill.name==skill_bouledefeu.name:
				self.mana-=skill.mcost
				atkformula=15-enemy_mres
				if power_sangancien.unlocked is True:
					atkformula+=atkformula*1/10
				if atkformula<0:
					atkformula=0
				return atkformula
			elif skill.name==skill_chatiment.name:
				self.mana-=self.mana*75/100
				atkformula=enemy_maxhealth*50/100
				if power_sangancien.unlocked is True:
					atkformula+=atkformula*1/10
				if atkformula<0:
					atkformula=0
				return atkformula
			elif skill.name==skill_duel.name:
				return 0
			elif skill.name==skill_foliesanguinaire.name:
				self.mana-=skill.mcost
				self.health+=60
			elif skill.name==skill_protectiondivine.name:
				self.mana-=skill.mcost
			elif skill.name==skill_canalisation.name:
				self.mana-=skill.mcost
			elif skill.name==skill_colere.name:
				self.mana-=skill.mcost
			elif skill.name==skill_affaiblissement.name:
				self.mana-=skill.mcost
			elif skill.name==skill_renforcement.name:
				self.mana-=skill.mcost
			else:
				print("Erreur ! La compétence spécifiée est introuvable")
				engine.pause()
		elif skill.name==skill_rituel.name:
			self.health-=25
			self.mana+=50
			player.checkStats()
		elif skill.name==skill_transcendance.name:
			self.stamina-=25
			self.mana+=25
			player.checkStats()
		else:
			engine.displayError("notenoughmana")
			return False
		player.checkStats()
		return 0

	def checkStats(self):
		if self.health>self.maxhealth:
			self.health=self.maxhealth
		elif self.health<0:
			self.health=0
		if self.stamina>self.maxstamina:
			self.stamina=self.maxstamina
		elif self.stamina<0:
			self.stamina=0
		if self.mana>self.maxmana:
			self.mana=self.maxmana
		elif self.mana<0:
			self.mana=0


	def display_status(self):
		inStatus=True
		while inStatus is True:
			engine.clear()
			print("Statut")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(25)
			print("HP :",self.health,"/",self.maxhealth)
			print("SP :",self.stamina,"/",self.maxstamina)
			print("MP :",self.mana,"/",self.maxmana)
			engine.print_separator(25)
			print("1. Voir les compétences")
			print("2. Voir les pouvoirs")
			engine.print_separator(25)
			print("3. Utiliser une potion")
			engine.print_separator(25)
			choice=input(" > ")
			if choice=="1":
				player.display_skills()
			elif choice=="2":
				player.display_powers()
			elif choice=="3":
				player.display_usePotion()
			elif choice=="0":
				player.display_DetailedStats()
			elif choice.lower()=="annuler":
				inStatus=False
			else:
				engine.displayError("invalidChoice")

	def display_usePotion(self):
		while True:
			engine.clear()
			print("Entrez le nom d'une potion pour l'utiliser.")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(20)
			for item in inventory.potions:
				if item.amount>0:
					print(" -",item.name,"x",item.amount)
			choice=input(" > ")
			if choice.lower()=="annuler":
				break
			else:
				for potion in inventory.potions:
					if choice.lower()==potion.name.lower():
						if potion.amount>0:
							self.use_potion(potion)
						else:
							engine.displayError("invalidchoice")

	def display_skills(self):
		inSkills=True
		while inSkills is True:
			engine.clear()
			print("Compétences")
			print("(entrez le nom d'une compétence pour voir ses détails.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(25)
			for item in player.skills:
				if item.unlocked==True:
					print(" -",item.name)
			choice=input(" > ")
			if choice.lower()=="annuler":
				inSkills=False
			else:
				for skill in player.skills:
					if choice.lower()==skill.name.lower():
						if skill.unlocked is True:
							player.display_skillStats(skill)
						else:
							engine.displayError("invalidchoice")

	def display_powers(self):
		inPowers=True
		while inPowers is True:
			engine.clear()
			print("Pouvoirs")
			print("(entrez le nom d'un pouvoir pour voir ses détails.)")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(25)
			for power in player.powers:
				if power.unlocked==True:
					print(" -",power.name)
			choice=input(" > ")
			if choice.lower()=="annuler":
				inPowers=False
			else:
				for power in player.powers:
					if choice.lower()==power.name.lower():
						if power.unlocked is True:
							player.display_powerStats(power)
						else:
							engine.displayError("invalidchoice")

	def display_powerStats(self,power):
		engine.clear()
		print(power.name)
		engine.print_separator(15)
		print("\"",power.desc,"\"")
		engine.pause()
			
	def display_skillStats(self,skill):
		engine.clear()
		print(skill.name)
		engine.print_separator(15)
		print("\"",skill.desc,"\"")
		print("MCO :",skill.mcost)
		engine.pause()

	def display_equipment(self):
		while True:
			engine.clear()
			print("Équipement")
			print("(entrez \'annuler\' pour partir.)")
			engine.print_separator(25)
			print("Arme équipée :",self.equipped_weapon.name)
			print("Armure équipée :",self.equipped_armor.name)
			engine.print_separator(25)
			print("DEG :",self.equipped_weapon.dmg)
			print("VIG :",self.equipped_weapon.scost)
			print("DEF :",self.equipped_weapon.blockvalue)
			print("PHR :",self.equipped_armor.pres)
			print("MHR :",self.equipped_armor.mres)
			engine.print_separator(25)
			print("1. Changer d'arme")
			print("2. Changer d'armure")
			choice=input(" > ")
			if choice=="1":
				while True:
					engine.clear()
					print("Entrez le nom d'une arme pour l'équiper à la place de",self.equipped_weapon.name)
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(25)
					for item in inventory.weapons:
						if item.amount>0:
							print(" -",item.name,"x",item.amount)
					choice=input(" > ")
					if choice.lower()=="annuler":
						break
					else:
						for weapon in inventory.weapons:
							if choice.lower()==weapon.name.lower():
								if weapon.amount>0:
									if weapon.name!=player.equipped_weapon.name:
										self.equipped_weapon=player.display_comparestats_weapon(self.equipped_weapon,weapon)
										break
									else:
										engine.displayError("alreadyequippedweapon")
								else:
									engine.displayError("invalidchoice")
			elif choice=="2":
				while True:
					engine.clear()
					print("Entrez le nom d'une armure pour l'équiper à la place de",self.equipped_armor.name)
					print("(entrez \'annuler\' pour partir.)")
					engine.print_separator(25)
					for item in inventory.armors:
						if item.amount>0:
							print(" -",item.name,"x",item.amount)
					choice=input(" > ")
					if choice.lower()=="annuler":
						break
					else:
						for armor in inventory.armors:
							if choice.lower()==armor.name.lower():
								if armor.amount>0:
									if armor.name!=player.equipped_armor.name:
										self.equipped_armor=player.display_comparestats_armor(self.equipped_armor,armor)
										break
									else:
										engine.displayError("alreadyequippedarmor")
								else:
									engine.displayError("invalidchoice")
			elif choice.lower()=="annuler":
				break
			else:
				engine.displayError("invalidchoice")

	def display_comparestats_weapon(self,oldweapon,newweapon):
		while True:
			engine.clear()
			print("Voulez-vous vraiment équiper",newweapon.name,"à la place de",oldweapon.name,"?")
			print("(répondez par 'oui' ou 'non'.)")
			engine.print_separator(30)
			print("Statistiques :",oldweapon.name,"-->",newweapon.name)
			print("DMG :",oldweapon.dmg,"-->",newweapon.dmg)
			print("VIG :",oldweapon.scost,"-->",newweapon.scost)
			print("DEF :",oldweapon.blockvalue,"-->",newweapon.blockvalue)
			choice=input(" > ")
			if choice.lower()=="oui":
				equipped_weapon=newweapon
				engine.clear()
				print(newweapon.name,"est maintenant équipé(e) en tant qu'arme.")
				engine.pause()
				break
			elif choice.lower()=="non":
				equipped_weapon=oldweapon
				break
			else:
				engine.displayError("invalidchoice")
		return equipped_weapon

	def display_comparestats_armor(self,oldarmor,newarmor):
		while True:
			engine.clear()
			print("Voulez-vous vraiment équiper",newarmor.name,"à la place de",oldarmor.name,"?")
			print("(répondez par 'oui' ou 'non'.)")
			engine.print_separator(30)
			print("Statistiques :",oldarmor.name,"-->",newarmor.name)
			print("PHR :",oldarmor.pres,"-->",newarmor.pres)
			print("MHR :",oldarmor.mres,"-->",newarmor.mres)
			choice=input(" > ")
			if choice.lower()=="oui":
				equipped_armor=newarmor
				engine.clear()
				print(newarmor.name,"est maintenant équipé(e) en tant qu'armure.")
				engine.pause()
				break
			elif choice.lower()=="non":
				equipped_armor=oldarmor
				break
			else:
				engine.displayError("invalidchoice")
		return equipped_armor

class Weapon(object):

	def __init__(self,name,desc,dmg,scost,blockvalue,price,amount):
		self.name=name
		self.desc=desc
		self.dmg=dmg
		self.scost=scost
		self.blockvalue=blockvalue
		self.price=price
		self.amount=amount

class Armor(object):

	def __init__(self,name,desc,pres,mres,price,amount):
		self.name=name
		self.desc=desc
		self.pres=pres
		self.mres=mres
		self.price=price
		self.amount=amount

class Potion(object):

	def __init__(self,name,desc,varamount,price,amount):
		self.name=name
		self.desc=desc
		self.varamount=varamount
		self.price=price
		self.amount=amount

class Skill(object):

	def __init__(self,name,desc,mcost,price):
		self.name=name
		self.desc=desc
		self.mcost=mcost
		self.unlocked=False
		self.price=price

class Power(object):

	def __init__(self,name,desc,price):
		self.name=name
		self.desc=desc
		self.unlocked=False
		self.price=price

class Enemy(object):

	def __init__(self,name,health,maxhealth,stamina,maxstamina,mana,maxmana,atk,scost,pres,mres,blockvalue):
		self.name=name
		self.type=type
		self.health=health
		self.maxhealth=maxhealth
		self.stamina=stamina
		self.maxstamina=maxstamina
		self.mana=mana
		self.maxmana=maxmana
		self.atk=atk
		self.scost=scost
		self.pres=pres
		self.mres=mres
		self.blockvalue=blockvalue

	def use_skill(self,skill):
		if self.mana>0:
			if skill.name==skill_soin.name:
				self.health+=25
				self.mana-=50
			elif skill.name==skill_rituel.name:
				self.health-=25
				self.mana+=50
			elif skill.name==skill_transcendance.name:
				self.stamina+=25
				self.mana-=25
			else:
				print("Erreur ! La compétence spécifiée est introuvable")
				engine.pause()
		else:
			engine.displayError("notenoughmana")
		self.checkStats()

	def checkStats(self):
		if self.health>self.maxhealth:
			self.health=self.maxhealth
		elif self.health<0:
			self.health=0
		if self.stamina>self.maxstamina:
			self.stamina=self.maxstamina
		elif self.stamina<0:
			self.stamina=0
		if self.mana>self.maxmana:
			self.mana=self.maxmana
		elif self.mana<0:
			self.mana=0

def main_menu():
	while True:
		inMainMenu=True
		engine.clear()
		print('Arwen - v.1.0.')
		engine.print_separator(15)
		print('1. Jouer')
		print('2. Crédits')
		print('3. Quitter')
		choice=input(' > ')
		if choice=='1':
			engine.clear()
			inMainMenu=False
			break
		elif choice=='2':
			engine.clear()
			print('Arwen - Un RPG de combat textuel')
			print('Développé par :')
			print(" — Nicolas \"Nitroxone\" Prévôt (conception générale, code, design, tests)")
			print(" — Erwan \"Cryptoiencli\" Vautier (tests, équilibrage)")
			print(" — Aristide \"Bangvolt\" Marion (il est là)")
			engine.print_separator(20)
			print('Version 1.0.')
			print('Écrit en Python.')
			engine.pause()
		elif choice=='3':
			exit()
		else:
			engine.displayError("invalidChoice")

def game_over():
	while True:
		engine.clear()
		print("Vous êtes mort. Game Over !")
		engine.print_separator(22)
		print("1. Quitter le jeu")
		print("2. Charger une sauvegarde")
		choice=input(" > ")
		if choice=="1":
			game.reset_stats()
			main_menu()
			break
		elif choice=="2":
			game.load_game()
			break
		else:
			engine.displayError("invalidchoice")

def askSaveBeforeQuit():
	while True:
		engine.clear()
		print("Voulez-vous sauvegarder votre progression avant de quitter ? Répondez par 'oui' ou 'non'.")
		choice=input(" > ")
		if choice.lower()=="oui":
			game.save_game()
			game.reset_stats()
			break
		elif choice.lower()=="non":
			game.reset_stats()
			break
		else:
			engine.displayError("invalidchoice")

while True:
	engine=Engine()
	inventory=Inventory()
	game=Game()
	game.load_weapons()
	game.load_armors()
	game.load_potions()
	game.load_enemies()
	main_menu()
	username=input("Entrez votre nom : ")
	# INTRODUCTION
	engine.clear()
	print("Vos recherches ont été fructueuses. Vous avez enfin mis à jour un secret enfoui depuis des millénaires ...")
	time.sleep(1)
	engine.pause()
	engine.clear()
	print("Les quatre gemmes de pouvoir, qui confèreraient à ceux qui les porte des pouvoirs allant au-delà de l'imagination,")
	time.sleep(0.5)
	print("ont été dispersées à travers le monde. Sans plus tarder, vous établissez votre repaire et partez à leur recherche.")
	engine.pause()
	engine.clear()
	print("Votre quête sera longue. À travers les labyrinthes dans la jungle de Khyrr Ikhu, l'obscurité et la puanteur des cavernes pélagiques du Grobbit,")
	print("en passant par le palais flamboyant de Limper Athris et l'antichambre enchantée du Flan-bit, vous vous battrez sans relâche")
	print("pour retrouver les quatre gemmes de pouvoir ...")
	engine.pause()
	#-------------
	player=Player(username,inventory,epeeRouillee,armureDeCuir)
	game.load_skills()
	game.load_powers()
	for weapon in inventory.weapons:
		if weapon.name==epeeRouillee.name or weapon.name==hacheUsee.name:
			inventory.add_item(weapon,1)
	for armor in inventory.armors:
		if armor.name==armureDeCuir.name or armor.name==plastronEnFer.name:
			inventory.add_item(armor,1)
	for potion in inventory.potions:
		if potion.name!=potionOubli.name and potion.name!=potionSuicide.name:
			inventory.add_item(potion,5)
	for skill in player.skills:
		if skill.name==skill_soin.name or skill.name==skill_rituel.name or skill.name==skill_transcendance.name or skill.name==skill_bouledefeu.name:
			player.unlock_skllpwr(skill)
	for power in player.powers:
		if power.name==power_endurance.name or power.name==power_sangancien.name:
			player.unlock_skllpwr(power)
	inventory.gold=100
	player.khyrrikhu=True
	player.grobbit=False
	player.flanbit=False
	player.limperathris=False
	game.run()
