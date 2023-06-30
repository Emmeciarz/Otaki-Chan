import asyncio
from cmath import cos
from email.message import Message
from pyexpat.errors import messages
from time import sleep, time
from unicodedata import name
from unittest import result
import discord
import random
import time
import os
import json
import datetime
from discord import channel
from discord import message
from discord.client import Client
from discord.ext.commands.bot import Bot
from discord.ext.commands import cooldown, BucketType
from discord.ui import Button, View
from discord.ext import commands, tasks
from random import randint

from Commands import Role

dictionary_j = {}
dictionary_j_spr = {}
dictionary_bank_transfer = {}
dictionary_chop = {}
dictionary_chop_spr = {}
dictionary_mine = {}
dictionary_mine_spr = {}
class CustomCommands:
	def get_commands(tree,client):

		path1 = './Commands/EcoRpg' #Windows/ubuntu
		path2 =  '/home/otaki/Otaki/Otaki-Chan/Commands/EcoRpg' #ubuntu jeśli ma okres
		os.chdir(path1)

		@tree.command(name = "profile", description= "Pokazuję twój serwerowy profil.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,member:discord.Member=None):
			if Role.traveler(interaction) in interaction.user.roles:
				if member == None:
					
					await open_account(interaction.user)
					user = interaction.user
					users = await get_bank_date()

					wallet = users[str(user.id)]["wallet"]
					bank = users[str(user.id)]["bank"]
					level = users[str(user.id)]["level"]
					xp = users[str(user.id)]["xp"]
					villager = users[str(user.id)]["villager"]
					happiness = users[str(user.id)]["happiness"]
					color = users[str(user.id)]["color"]
					if happiness <= 0:
						state = "Makabryczne"
					elif happiness <= 5:
						state = "Złe"
					elif happiness <= 10:
						state = "Neutralne"
					elif happiness <= 15:
						state = "Dobre"
					elif happiness <= 20:
						state = "Wspaniałe"
		
					embed=discord.Embed(title="Konto użytkownika:",description=f"{interaction.user}", color=color)
					embed.set_thumbnail(url=f"{interaction.user.avatar}")
					embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
					embed.add_field(name="Punkty doświadczenia:",value=f"🧶 {xp}", inline=False)
					embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
					embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
					embed.add_field(name="Mieszkańcy wioski:",value=f"🏘️ {villager}", inline=False)
					embed.add_field(name="Zadowolenie:",value=f"🎭 {happiness} | {state}", inline=True)
					await interaction.response.send_message(embed=embed)

				else:
					await open_account(member)
					user = member
					users = await get_bank_date()

					wallet = users[str(user.id)]["wallet"]
					bank = users[str(user.id)]["bank"]
					level = users[str(user.id)]["level"]
					xp = users[str(user.id)]["xp"]
					villager = users[str(user.id)]["villager"]
					happiness = users[str(user.id)]["happiness"]
					color = users[str(user.id)]["color"]
					if happiness <= 0:
						state = "Makabryczne"
					elif happiness <= 5:
						state = "Złe"
					elif happiness <= 10:
						state = "Neutralne"
					elif happiness <= 15:
						state = "Dobre"
					elif happiness <= 20:
						state = "Wspaniałe"
					
					embed=discord.Embed(title="Konto użytkownika:",description=f"{member.display_name}", color=color)
					embed.set_thumbnail(url=f"{member.avatar}")
					embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
					embed.add_field(name="Punkty doświadczenia:",value=f"🧶 {xp}", inline=False)
					embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
					embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
					embed.add_field(name="Mieszkańcy wioski:",value=f"🏘️ {villager}", inline=False)
					embed.add_field(name="Zadowolenie:",value=f"🎭 {happiness} | {state}", inline=False)
					await interaction.response.send_message(embed=embed)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "materials", description= "Pokazuję twoje konto z materiałami.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,member:discord.Member=None):
			if Role.traveler(interaction) in interaction.user.roles:
				if member == None:
					await open_account_materials(interaction.user)
					user = interaction.user
					users = await get_materials_date()

					wood = users[str(user.id)]["wood"]
					hardwood = users[str(user.id)]["hardwood"]
					stone = users[str(user.id)]["stone"]
					iron = users[str(user.id)]["iron"]
					gold = users[str(user.id)]["gold"]
					mushroom = users[str(user.id)]["mushroom"]
					fish = users[str(user.id)]["fish"]

					await open_account(interaction.user)
					user = interaction.user
					users = await get_bank_date()
					color = users[str(user.id)]["color"]

					embed=discord.Embed(title="Materiały użytkownika:",description=f"{interaction.user}", color=color)
					embed.set_thumbnail(url=f"{interaction.user.avatar}")
					embed.add_field(name="Drewno:",value=f"<:wood:979761455291318302> {wood}", inline=False)
					embed.add_field(name="Twarde drewno:",value=f"<:hardwood:979760814712049674> {hardwood}", inline=False)
					embed.add_field(name="Kamień:", value=f"<:rock:979764802232651856> {stone}", inline=False)
					embed.add_field(name="Żelazo:",value=f"<:iron:1066544833449185280> {iron}", inline=False)
					embed.add_field(name="Złoto:",value=f"<:gold:1066545203160293456> {gold}", inline=True)
					embed.add_field(name="Grzyby:",value=f"<:mushroom:979128655403962389> {mushroom}", inline=True)
					embed.add_field(name="Ryby:",value=f"🐟 {fish}", inline=True)
					await interaction.response.send_message(embed=embed)
				else:
					await open_account_materials(member)
					user = member
					users = await get_materials_date()

					wood = users[str(user.id)]["wood"]
					hardwood = users[str(user.id)]["hardwood"]
					stone = users[str(user.id)]["stone"]
					iron = users[str(user.id)]["iron"]
					gold = users[str(user.id)]["gold"]
					mushroom = users[str(user.id)]["mushroom"]
					fish = users[str(user.id)]["fish"]

					await open_account(member)
					user = member
					users = await get_bank_date()
					color = users[str(user.id)]["color"]

					embed=discord.Embed(title="Materiały użytkownika:",description=f"{member.display_name}", color=color)
					embed.set_thumbnail(url=f"{member.avatar}")
					embed.add_field(name="Drewno:",value=f"<:wood:979761455291318302> {wood}", inline=False)
					embed.add_field(name="Twarde drewno:",value=f"<:hardwood:979760814712049674> {hardwood}", inline=False)
					embed.add_field(name="Kamień:", value=f"<:rock:979764802232651856> {stone}", inline=False)
					embed.add_field(name="Żelazo:",value=f"<:iron:1066544833449185280> {iron}", inline=False)
					embed.add_field(name="Złoto:",value=f"<:gold:1066545203160293456> {gold}", inline=True)
					embed.add_field(name="Grzyby:",value=f"<:mushroom:979128655403962389> {mushroom}", inline=True)
					embed.add_field(name="Ryby:",value=f"🐟 {fish}", inline=True)
					await interaction.response.send_message(embed=embed)
			
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		async def open_account(user):
			with open("mainbank.json","r") as f:
				users = await get_bank_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}
					users[str(user.id)]["wallet"] = 0
					users[str(user.id)]["bank"] = 0
					users[str(user.id)]["level"] = 1
					users[str(user.id)]["xp"] = 0
					users[str(user.id)]["villager"] = 3
					users[str(user.id)]["happiness"] = 10
					users[str(user.id)]["color"] = 0xfceade

				with open("mainbank.json","w") as f:
					json.dump(users,f)
				return True

		async def open_account_materials(user):
			with open("materials.json","r") as f:
				users = await get_materials_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}
					users[str(user.id)]["wood"] = 0
					users[str(user.id)]["hardwood"] = 0
					users[str(user.id)]["stone"] = 0
					users[str(user.id)]["iron"] = 0
					users[str(user.id)]["gold"] = 0
					users[str(user.id)]["mushroom"] = 0
					users[str(user.id)]["fish"] = 0

				with open("materials.json","w") as f:
					json.dump(users,f)
				return True

		async def get_bank_date():
			with open("mainbank.json","r") as f:
				users = json.load(f)
			return users
		
		async def get_materials_date():
			with open("materials.json","r") as f:
				users = json.load(f)
			return users

		async def update_bank(user,change = 0,mode ="wallet"):
			users = await get_bank_date()

			users[str(user.id)][mode] += change

			with open("mainbank.json","w") as f:
				json.dump(users,f)

			bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
			return bal

		@tree.command(name = "guidebook", description= "Magiczna książka która pomaga jak i objaśnia rzeczy.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.traveler(interaction) in interaction.user.roles:
				await open_account(interaction.user)
				user = interaction.user
				users = await get_bank_date()
				level = users[str(user.id)]["level"]

				if level == 1:
					embed = discord.Embed(title="GuideBook", description="Poziom Jakości **1**:", color=0xfceade)
					embed.set_thumbnail(url="https://i.postimg.cc/BZyBFHQL/garde-art-777.jpg")
					embed.add_field(name="/profile", value="Pozw?la ci zobaczyć ?? jak i innych ??? serwer?wy.", inline=False)
					embed.add_field(name="/deposit", value="Po#$^la ci wpł@cić pieniądz) do b@nku.", inline=False)
					embed.add_field(name="/withdraw", value="P:::ozw:ala ci wypła?ić pieni,dze z bankuuu.", inline=False)
					embed.add_field(name="/bank_transfer", value="Pozw#la ci dokon%ć przelewu z t#oj#ego b@nkuwu na kont!a innych uc<estn<ików ser=er-a.", inline=False)
					embed.add_field(name="/instantbank_transfer", value="Dział@@ tak sim^o jak z>yk{y bank_transfer z dw[]ma r&żnic&,mi: nie musisz {}dczek*iwać dnia na k@lejny przel][ew, bank pobi,era prowizje w wysokości 3000>??>< Otaki-coin\ó/w.", inline=False)
					embed.add_field(name="/materials", value="|>|***ję ci twój p?%^ z m@t^eri@łam{i.", inline=False)
					embed.add_field(name="/job", value="Pozwala ci !?>^&4 pieniądze jak i :81$@! doświadczenia.", inline=False)
					embed.add_field(name="/chop", value="/.zwala ci ścinać drz##a dzięki czemu ozym3#ujesz drewno oraz punkty doświadczenia.", inline=False)
					embed.add_field(name="/mine", value=f"Po%ala ci kopa_ć kamienie dzięki ,;as5% otrzymujesz kamień oraz _+Asd.#!@.", inline=False)
					embed.add_field(name="/guidebook", value="_%@#!$?>?<?%!@ jest b@rdzo pomocny ^%3*.>", inline=False)
					embed.add_field(name="/levelup", value=f"D/z$ejk& niej b124<; mógł zwi13ę?>ksz|ć swój p@zi[]m.", inline=False)
					await interaction.response.send_message(embed=embed,ephemeral = True)
				
				if level == 2:
					embed = discord.Embed(title="GuideBook", description="Poziom Jakości **1**:", color=0xfceade)
					embed.set_thumbnail(url="https://i.postimg.cc/BZyBFHQL/garde-art-777.jpg")
					embed.add_field(name="/profile", value="Pozw?la ci zobaczyć ?? jak i innych ??? serwer?wy.", inline=False)
					embed.add_field(name="/deposit", value="Po#$^la ci wpł@cić pieniądz) do b@nku.", inline=False)
					embed.add_field(name="/withdraw", value="P:::ozw:ala ci wypła?ić pieni,dze z bankuuu.", inline=False)
					embed.add_field(name="/bank_transfer", value="Pozw#la ci dokon%ć przelewu z t#oj#ego b@nkuwu na kont!a innych uc<estn<ików ser=er-a.", inline=False)
					embed.add_field(name="/instantbank_transfer", value="Dział@@ tak sim^o jak z>yk{y bank_transfer z dw[]ma r&żnic&,mi: nie musisz {}dczek*iwać dnia na k@lejny przel][ew, bank pobi,era prowizje w wysokości 3000>??>< Otaki-coin\ó/w.", inline=False)
					embed.add_field(name="/materials", value="|>|***ję ci twój p?%^ z m@t^eri@łam{i.", inline=False)
					embed.add_field(name="/job", value="Pozwala ci !?>^&4 pieniądze jak i :81$@! doświadczenia.", inline=False)
					embed.add_field(name="/chop", value="/.zwala ci ścinać drz##a dzięki czemu ozym3#ujesz drewno oraz punkty doświadczenia.", inline=False)
					embed.add_field(name="/mine", value=f"Po%ala ci kopa_ć kamienie dzięki ,;as5% otrzymujesz kamień oraz _+Asd.#!@.", inline=False)
					embed.add_field(name="/guidebook", value="_%@#!$?>?<?%!@ jest b@rdzo pomocny ^%3*.>", inline=False)
					embed.add_field(name="/levelup", value=f"D/z$ejk& niej b124<; mógł zwi13ę?>ksz|ć swój p@zi[]m.", inline=False)
					await interaction.response.send_message(embed=embed,ephemeral = True)
				
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "withdraw", description= "Pozwala ci wypłacić pieniądze z banku.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int):
			if Role.traveler(interaction) in interaction.user.roles:
				await open_account(interaction.user)

				if amount == None:
					await interaction.response.send_message("Proszę podać też kwotę do wypłacenia.", ephemeral = True)
					return		
				bal = await update_bank(interaction.user)
				if amount == "all" or amount == "All" or amount == "ALL":
					amount = bal[1]
				amount = int(amount)
				if amount>bal[1]:
					await interaction.response.send_message("Nie posiadasz tyle pieniędzy na koncie bankowym.", ephemeral = True)
					return
				if amount<0:
					await interaction.response.send_message("Kwota musi być dodatnia.", ephemeral = True)
					return
				
				await update_bank(interaction.user,amount)
				await update_bank(interaction.user,-1*amount,"bank")
				await interaction.response.send_message(f"Wypłaciłeś {amount} Otaki-coinów.", ephemeral = False)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "deposit", description= "Pozwala ci wpłacić pieniądze do banku.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int):
			if Role.traveler(interaction) in interaction.user.roles:
				await open_account(interaction.user)

				if amount == None:
					await interaction.response.send_message("Proszę podać też kwotę do wpłacenia.", ephemeral = True)	
					return
				bal = await update_bank(interaction.user)
				if amount == "all" or amount == "All" or amount == "ALL":
					amount = bal[0]
				amount = int(amount)
				if amount>bal[0]:
					await interaction.response.send_message("Nie posiadasz tyle pieniędzy.", ephemeral = True)	
					return
				if amount<0:
					await interaction.response.send_message("Kwota musi być dodatnia", ephemeral = True)	
					return

				await update_bank(interaction.user,-1*amount)
				await update_bank(interaction.user,amount,"bank")
				await interaction.response.send_message(f"Wpłaciłeś {amount} Otaki-coinów.", ephemeral = False)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "job", description= "Pozwala ci wykonywać prace za którą dostajesz pieniądze i punkty doświadczenia.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.traveler(interaction) in interaction.user.roles:
				if dictionary_j_spr.get(interaction.user.id) and dictionary_j_spr[interaction.user.id]["wyslane"] == True:
					await interaction.response.send_message(f"Dokończ swoją poprzednią pracę {interaction.user.mention}", ephemeral = True)
					return

				if dictionary_j.get(interaction.user.id):
					time_end = dictionary_j[interaction.user.id]["time_end"] 
					if time.time()>time_end:
						dictionary_j.pop(interaction.user.id)
					else:
						remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
						await interaction.response.send_message(f"Musisz odczekać jeszcze {remaining_time} {interaction.user.mention}.", ephemeral = True)
						return

				dictionary_j_spr[interaction.user.id] = {"wyslane":True}

				class MySelectView(View):
						@discord.ui.select(
							placeholder="Kliknij Tu i Wybierz Prace.",
								options=[

									discord.SelectOption(
										label="Szybka Praca",
										description="Zbieranie Grzybów 15 min",
										value="1x0",
										emoji="<:mushroom_smb:979128655403962389>",
									),

									discord.SelectOption(
										label="Średnia Praca",
										description="Pilnowanie Owiec 30 min",
										value="2x0",
										emoji="🐑",
									),

									discord.SelectOption(
										label="Długa Praca",
										description="Pomaganie na Farmie 1h",
										value="3x0",
										emoji="🧑‍🌾",
									),	
								],)
					
						async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
							select.disabled = True
							if select.values[0] == "1x0":
								dictionary_j[interaction.user.id] = {"time_end":time.time()+60*15}

								await open_account(interaction.user)
								users = await get_bank_date()
								user = interaction.user

								reward = 55
								reward_xp = 15

								users[str(user.id)]["wallet"] += reward
								users[str(user.id)]["xp"] += reward_xp

								with open("mainbank.json","w") as f:
									json.dump(users,f)
								
								dictionary_j_spr[interaction.user.id]["wyslane"] = False

								embed=discord.Embed(title="Za Zbieranie Grzybów",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa" , color=0xfceade)
								embed.set_thumbnail(url=f"https://i.postimg.cc/3N8TkQ3N/depositphotos-62799645-stock-illustration-mushrooms-in-a-wicker-basket.webp")
								await interaction.response.edit_message(content=None,embed=embed,view=None)

							if select.values[0] == "2x0":
								dictionary_j[interaction.user.id] = {"time_end":time.time()+60*30}

								await open_account(interaction.user)
								users = await get_bank_date()
								user = interaction.user							

								reward = 185
								reward_xp = 51

								users[str(user.id)]["wallet"] += reward
								users[str(user.id)]["xp"] += reward_xp

								with open("mainbank.json","w") as f:
									json.dump(users,f)

								dictionary_j_spr[interaction.user.id]["wyslane"] = False

								embed=discord.Embed(title="Za Pilnowanie Owiec",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa", color=0xfceade)
								embed.set_thumbnail(url=f"https://i.postimg.cc/y6jKwxTZ/1560202783-otakuap-wooloo.jpg")
								await interaction.response.edit_message(content=None,embed=embed,view=None)

							if select.values[0] == "3x0":
								dictionary_j[interaction.user.id] = {"time_end":time.time()+60*60}

								await open_account(interaction.user)
								users = await get_bank_date()
								user = interaction.user									

								reward = 450 #Nagroda za 6 h
								reward_xp = 173

								users[str(user.id)]["wallet"] += reward
								users[str(user.id)]["xp"] += reward_xp

								with open("mainbank.json","w") as f:
									json.dump(users,f)

								dictionary_j_spr[interaction.user.id]["wyslane"] = False

								embed=discord.Embed(title="Za Pomoc Na Farmie",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa", color=0xfceade)
								embed.set_thumbnail(url=f"https://i.postimg.cc/jdjTKT8k/87e9225272bd536997e1652d0d41f935.jpg")
								await interaction.response.edit_message(content=None,embed=embed,view=None)

				view = MySelectView()
				await interaction.response.send_message(f"Wybierz prace spośród podanych:",view=view, ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "instantbank_transfer", description= "Działa tak samo jak zwykły bank_transfer ale nie musisz odczekiwać dnia na kolejny przelew.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int , member:discord.Member):
			if Role.traveler(interaction) in interaction.user.roles:
				await open_account(interaction.user)
				await open_account(member)

				if amount == None:
					await interaction.response.send_message("Proszę podaj też kwotę do wysłania.",ephemeral = True)	
					return
				bal = await update_bank(interaction.user)
				procent = int(3000)
				amount = int(amount)
				finalna_kwota = amount + procent
				if finalna_kwota>bal[1]:
					await interaction.response.send_message("Nie posiadasz tyle pieniędzy do wysłania.\nPamiętaj że prowizja banku wynosi 3000 Otaki-coinów.",ephemeral = True)	
					return
				if amount<0:
					await interaction.response.send_message("Kwota do wysłania musi być dodatnia.",ephemeral = True)
					return

				await update_bank(interaction.user,-1*finalna_kwota,"bank")
				await update_bank(member,amount,"bank")
				await interaction.response.send_message(f"Dokonałeś przelewu o wartości {amount} Otaki-coinów na konto użytkownika {member.mention}.",ephemeral = False)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "bank_transfer", description= "Pozwala na przelewanie pieniędzy z banku do banków innych uczestników serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int , member:discord.Member):
			if Role.traveler(interaction) in interaction.user.roles:
				if dictionary_bank_transfer.get(interaction.user.id):
					time_end = dictionary_bank_transfer[interaction.user.id]["time_end"] 
					if time.time()>time_end:
						dictionary_bank_transfer.pop(interaction.user.id)
					else:
						remaining_time = time.strftime("%T", time.localtime(time_end-time.time()))
						await interaction.response.send_message(f"Musisz odczekać jeszcze {remaining_time} {interaction.user.mention}.", ephemeral = True)
						return
				
				await open_account(interaction.user)
				await open_account(member)
				
				if amount == None:
					await interaction.response.send_message("Proszę podaj też kwotę do wysłania.",ephemeral = True)		
					return
				bal = await update_bank(interaction.user)
				amount = int(amount)
				if amount>bal[1]:
					await interaction.response.send_message("Nie posiadasz tyle pieniędzy do wysłania.",ephemeral = True)	
					return
				if amount<0:
					await interaction.response.send_message("Kwota do wysłania musi być dodatnia.",ephemeral = True)
					return

				dictionary_bank_transfer[interaction.user.id] = {"time_end":time.time()+23*60*60}
				await update_bank(interaction.user,-1*amount,"bank")
				await update_bank(member,amount,"bank")
				await interaction.response.send_message(f"Dokonałeś przelewu o wartości {amount} Otaki-coinów na konto użytkownika {member.mention}.",ephemeral = False)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "chop", description= "Pozwala ci ścinać drewno w lesie.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.traveler(interaction) in interaction.user.roles:

				channel = discord.utils.get(interaction.guild.channels, id = 1064994944609165442)

				if  interaction.channel == channel:

					if dictionary_chop_spr.get(interaction.user.id) and dictionary_chop_spr[interaction.user.id]["wyslane"] == True:
						await interaction.response.send_message(f"Dokończ swoje poprzednie drzewo {interaction.user.mention}", ephemeral = True)
						return

					if dictionary_chop.get(interaction.user.id):
						time_end = dictionary_chop[interaction.user.id]["time_end"] 
						if time.time()>time_end:
							dictionary_chop.pop(interaction.user.id)
						else:
							remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
							await interaction.response.send_message(f"Musisz odczekać jeszcze {remaining_time} {interaction.user.mention}.", ephemeral = True)
							return

					dictionary_chop_spr[interaction.user.id] = {"wyslane":True}
					dictionary_chop[interaction.user.id] = {"time_end":time.time()+60*60}

					class MyView5(View):
						@discord.ui.button(label="Chop 4/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							await open_account_materials(interaction.user)
							user = interaction.user
							users = await get_materials_date()

							random_wood = int(random.uniform(2,5))
							users[str(user.id)]["wood"] += random_wood

							with open("materials.json","w") as f:
								json.dump(users,f)
							
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()

							reward_xp = 5
							users[str(user.id)]["xp"] += reward_xp

							with open("mainbank.json","w") as f:
								json.dump(users,f)


							dictionary_chop_spr[interaction.user.id]["wyslane"] = False

							embed=discord.Embed(title="Ściąłeś Pospolite Drzewo",description=f"", color=0xe9732b)
							embed.set_image(url="https://i.postimg.cc/c4j4vPY4/pien.png")
							embed.add_field(name="Zdobywasz", value=f"{random_wood} Sztuk Drewna\n{reward_xp} XPa", inline=False)
							await interaction.response.edit_message(embed=embed,view=None)

					class MyView4(View):
						@discord.ui.button(label="Chop 3/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)

							embed.set_image(url="https://i.postimg.cc/pXWLcSsd/Untitled432-20220601185505.jpg")
							await interaction.response.edit_message(embed=embed,view=MyView5())

					class MyView3(View):
						@discord.ui.button(label="Chop 2/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/bwdNptcc/Untitled432-20220601185513.jpg")
							await interaction.response.edit_message(embed=embed,view=MyView4())

					class MyView2(View):
						@discord.ui.button(label="Chop 1/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/bwdNptcc/Untitled432-20220601185513.jpg")
							await interaction.response.edit_message(embed=embed,view=MyView3())

					class MyView(View):
						@discord.ui.button(label="Chop 0/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await interaction.response.edit_message(view=MyView2())

					view = MyView()
					embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)
					embed.set_image(url="https://i.postimg.cc/Wb5bB7yw/bc883370d44e8f633a7b7f6e6e1626d0.jpg")
					await interaction.response.send_message(embed=embed, view=view,ephemeral = True)

				else:
					await interaction.response.send_message(f"Nye jesteś w lesie :evergreen_tree:{interaction.user.mention}:evergreen_tree:",ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "mine", description= "Pozwala ci wydobywać skały w kopalni.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.traveler(interaction) in interaction.user.roles:

				channel = discord.utils.get(interaction.guild.channels, id = 1066742766882803722)

				if  interaction.channel == channel:

					if dictionary_mine_spr.get(interaction.user.id) and dictionary_mine_spr[interaction.user.id]["wyslane"] == True:
						await interaction.response.send_message(f"Dokończ swój poprzedni kamień {interaction.user.mention}.",ephemeral = True)
						return
					
					if dictionary_mine.get(interaction.user.id):
						time_end = dictionary_mine[interaction.user.id]["time_end"] 
						if time.time()>time_end:
							dictionary_mine.pop(interaction.user.id)
						else:
							remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
							await interaction.response.send_message(f"Musisz odczekać jeszcze {remaining_time} {interaction.user.mention}.", ephemeral = True)
							return

					dictionary_mine_spr[interaction.user.id] = {"wyslane":True}
					dictionary_mine[interaction.user.id] = {"time_end":time.time()+60*60}

					class MyView5(View):
						@discord.ui.button(label="Mine 4/5", style=discord.ButtonStyle.grey, emoji="⛏️")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							await open_account_materials(interaction.user)
							user = interaction.user
							users = await get_materials_date()

							random_stone = int(random.uniform(2,5))
							users[str(user.id)]["stone"] += random_stone

							with open("materials.json","w") as f:
								json.dump(users,f)
							
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()

							reward_xp = 5
							users[str(user.id)]["xp"] += reward_xp

							with open("mainbank.json","w") as f:
								json.dump(users,f)

							dictionary_mine_spr[interaction.user.id]["wyslane"] = False

							embed=discord.Embed(title="Wykopałeś Pospolity Kamień",description=f"", color=0x434a45)
							embed.set_image(url="https://i.postimg.cc/Dfqt4ydW/kp5.png")
							embed.add_field(name="Zdobywasz", value=f"{random_stone} Sztuk Kamienia\n{reward_xp} XPa", inline=False)
							await interaction.response.edit_message(embed=embed,view=None)

					class MyView4(View):
						@discord.ui.button(label="Mine 3/5", style=discord.ButtonStyle.grey, emoji="⛏️")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/L5B7cN6k/kp3.png")
							await interaction.response.edit_message(embed=embed,view=MyView5())

					class MyView3(View):
						@discord.ui.button(label="Mine 2/5", style=discord.ButtonStyle.grey, emoji="⛏️")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/NFwSCWYf/kp2.png")
							await interaction.response.edit_message(embed=embed,view=MyView4())

					class MyView2(View):
						@discord.ui.button(label="Mine 1/5", style=discord.ButtonStyle.grey, emoji="⛏️")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/Qt7vbj2y/kp1.png")
							await interaction.response.edit_message(embed=embed,view=MyView3())

					class MyView(View):
						@discord.ui.button(label="Mine 0/5", style=discord.ButtonStyle.grey, emoji="⛏️")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							embed.set_image(url="https://i.postimg.cc/Zq21pWMN/kp.png")
							await interaction.response.edit_message(embed=embed,view=MyView2())

					view = MyView()
					embed=discord.Embed(title="Pospolity Kamień",description=f"", color=0xa28e8e)
					embed.set_image(url="https://i.postimg.cc/Zq21pWMN/kp.png")
					await interaction.response.send_message(embed=embed, view=view,ephemeral = True)

				else:
					await interaction.response.send_message(f"Nye jesteś w kopalni 🚧{interaction.user.mention}🚧",ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		@tree.command(name = "levelup", description= "Dziejki niej będziesz mógł zwiększyć swój poziom.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.traveler(interaction) in interaction.user.roles:
				await open_account(interaction.user)
				user = interaction.user
				users = await get_bank_date()

				level = users[str(user.id)]["level"]
				xp = users[str(user.id)]["xp"]

				if level == 1:

					class MyLevelUp(View):
						@discord.ui.button(label="LevelUp", style=discord.ButtonStyle.success)
						async def success_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							if xp >= 1000:

								await open_account(interaction.user)
								user = interaction.user
								users = await get_bank_date()
								cost_xp = 1000
								users[str(user.id)]["xp"] -= cost_xp
								users[str(user.id)]["level"] = 2

								class MyColor(View):
									@discord.ui.button(label="1", style=discord.ButtonStyle.primary)
									async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0x0909ff
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927889321929875467>.",embed=None,view=None)
									
									@discord.ui.button(label="2", style=discord.ButtonStyle.primary)
									async def primary2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0x66cdaa
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927890415334596628>.",embed=None,view=None)

									@discord.ui.button(label="3", style=discord.ButtonStyle.primary)
									async def primary3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0x228b22
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927890916738478120>.",embed=None,view=None)
									
									@discord.ui.button(label="4", style=discord.ButtonStyle.primary)
									async def primary4_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0x4cc417
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927891029661720606>.",embed=None,view=None)

									@discord.ui.button(label="5", style=discord.ButtonStyle.primary)
									async def primary5_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xffff00
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927891257139802193>.",embed=None,view=None)
									
									@discord.ui.button(label="6", style=discord.ButtonStyle.primary)
									async def primary6_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xfbb117
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927891380980830238>.",embed=None,view=None)
									
									@discord.ui.button(label="7", style=discord.ButtonStyle.primary)
									async def primary7_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xe2a76f
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927891465454096395>.",embed=None,view=None)
									
									@discord.ui.button(label="8", style=discord.ButtonStyle.primary)
									async def primary8_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xff6700
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927892009140768798>.",embed=None,view=None)

									@discord.ui.button(label="9", style=discord.ButtonStyle.primary)
									async def primary9_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xff0000
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927892168750796810>.",embed=None,view=None)

									@discord.ui.button(label="10", style=discord.ButtonStyle.primary)
									async def primary10_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xdb1646
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927894148164517929>.",embed=None,view=None)

									@discord.ui.button(label="11", style=discord.ButtonStyle.primary)
									async def primary11_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0x7d0552
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927892425920364564>.",embed=None,view=None)
									
									@discord.ui.button(label="12", style=discord.ButtonStyle.primary)
									async def primary12_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xf535aa
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927892737733324811>.",embed=None,view=None)
									
									@discord.ui.button(label="13", style=discord.ButtonStyle.primary)
									async def primary13_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xfea3aa
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927892571370438707>.",embed=None,view=None)
									
									@discord.ui.button(label="14", style=discord.ButtonStyle.primary)
									async def primary14_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										users[str(user.id)]["color"] = 0xffffff
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na <@&927893071423754310>.",embed=None,view=None)
									
									@discord.ui.button(label="R", style=discord.ButtonStyle.danger)
									async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
										button.disabled = True
										RandomColor = [0x0909ff,
											0x66cdaa,
											0x228b22,
											0x4cc417,
											0xffff00,
											0xfbb117,
											0xe2a76f,
											0xff6700,
											0xff0000,
											0xdb1646,
											0x7d0552,
											0xf535aa,
											0xfea3aa,
											0xffffff]
										users[str(user.id)]["color"] = random.choice(RandomColor)
										with open("mainbank.json","w") as f:
											json.dump(users,f)
										await interaction.response.edit_message(content=f"Pomyślnie ustawiono kolor nici na ???, Przekonaj się sam.",embed=None,view=None)

									

								embed = discord.Embed(title="Gratulacje!", description="Za to że udało ci się awansować na poziom drugi możesz wybrać kolor nici z której będzie uszyty twój profil jak i materiały.", color=0xfceade)
								embed.add_field(name="Wybierz kolor swojej nici:", value="**1.<@&927889321929875467>**\n**2.<@&927890415334596628>**\n**3.<@&927890916738478120>**\n**4.<@&927891029661720606>**\n**5.<@&927891257139802193>**\n**6.<@&927891380980830238>**\n**7.<@&927891465454096395>**\n**8.<@&927892009140768798>**\n**9.<@&927892168750796810>**\n**10.<@&927894148164517929>**\n**11.<@&927892425920364564>**\n**12.<@&927892737733324811>**\n**13.<@&927892571370438707>**\n**14.<@&927893071423754310>**\n**R.__Losuję kolor nici.__**",inline=False)
								embed.set_thumbnail(url="https://i.postimg.cc/qM04tNDN/yarn-1f9f6.png")
								await interaction.response.edit_message(embed=embed,view=MyColor())
							else:
								await interaction.response.edit_message(content=f"Niestety brakuję ci jeszcze punktów punktów doświadczenia {interaction.user.mention}",embed=None,view=None)

					embed=discord.Embed(title="Czy chcesz podnieść swój obecny poziom: 1 <a:greenheart:972100111368851486> 2",description=f"", color=0xa28e8e)
					embed.add_field(name="Potrzebna ilość punktów doświadczenia:", value=f"🧶1000", inline=False)
					embed.add_field(name="Ilość obecnie zebranych punktów doświadczenia:", value=f"🧶{xp}", inline=False)
					await interaction.response.send_message(embed=embed, view=MyLevelUp(),ephemeral = True)

				else:
					await interaction.response.send_message(f"Posiadasz obecnie największy poziom do zdobycia {interaction.user.mention} <a:hype2:921392905598435358>")

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention} ponieważ jeszcze nie wyruszyłeś w podróż na co czekasz /adventure <:conflict:921394533449744394>", ephemeral = True)

		# @tree.command(name = "village", description= "Pozwala ci robić interakcje z twoją wioską.", guild = discord.Object(id = 698522294414344232))
		# async def self(interaction: discord.Integration):

		# 	await interaction.response.send_message(f"Posiadasz obecnie największy poziom do zdobycia {interaction.user.mention} <a:hype2:921392905598435358>")








		@tree.command(name = "adventure", description= "Pozwala ci rozpocząć twoją przygodę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			# Przyznajemy ci też rangę <@&1018206772869222410>

			if Role.traveler(interaction) in interaction.user.roles:
				await interaction.response.send_message(f"Hej twoja historia już się zaczęła, nye możesz przeżyć jej jeszcze raz {interaction.user.mention}.", ephemeral = True)

			else:
				if Role.administrator(interaction) in interaction.user.roles:



					class MyConversationTwo(View):
						@discord.ui.button(label="1", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="a", description="a", color=0xfceade)

							await interaction.response.edit_message(embed=embed,view=MyConversationOne())
						
						@discord.ui.button(label="2", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="a", description="a", color=0xfceade)

							await interaction.response.edit_message(embed=embed,view=MyConversationOne())
						
						@discord.ui.button(label="1", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="a", description="a", color=0xfceade)

							await interaction.response.edit_message(embed=embed,view=MyConversationOne())

					class MyConversationTwo(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Kiriu", description="Dobrze wiec wyjaśnicie mi co teraz usiłujecie zrobić ?", color=0xfceade)
							embed.add_field(name=f"{interaction.user.name}", value="Hym", inline=False)
							embed.add_field(name=f"Kiriu", value="?", inline=False)
							embed.add_field(name=f"Kiriu", value="Czy w naprawdę teraz będziecie zgrywać niedostępnych ?", inline=False)
							embed.add_field(name="---------------",value=f"", inline=False)
							embed.add_field(name=f"|1|", value="To nie tak jak myślisz", inline=False)
							embed.add_field(name=f"|2|", value="To ty przecież jesteś nie dostępny ", inline=False)
							embed.add_field(name=f"|3|", value="Tak", inline=False)
							embed.add_field(name=f"|4|", value="Nie", inline=False)


							await interaction.response.edit_message(embed=embed,view=MyConversationOne())

					class MyConversationOne(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description="Nyanho Kiriu, chciałbyś może dołączyć do naszej nowo powstającej wioski w dodatkowym uniwersum podległym do obecnego które znajduję się w naj niższej warstwie naszego świata ?", color=0xfceade)
							embed.add_field(name=f"Kiriu", value="Tak, Chętnie", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="...", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="spodziewałam się jakiegoś ale albo no zgrywanie nie dostępnego", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Tyle obmyślonych argumentów do przekonania cię nooo", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Wiem w takim razie skoro ty nie chciałeś zgrywać niedostępnego to by będziemy", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Teraz będziesz musiał ty nas przekonać", inline=False)
							embed.add_field(name=f"Otaki-Chan", value=f"pamiętaj {interaction.user.name} zgrywaj nie dostępnego nie daj mu się", inline=False)
							embed.add_field(name=f"Mani-Chan", value=f"Dobieraj rozważnie słowa {interaction.user.name} żeby nas nie podszedł", inline=False)

							await interaction.response.edit_message(embed=embed,view=MyConversationOne())


					class MyVillageEleven(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description="A teraz przejdźmy do sedna czyli do tematu naszej wioski.", color=0xfceade)
							embed.add_field(name=f"Otaki-Chan", value="Musimy pozyskać mieszkańców !", inline=False)
							embed.add_field(name=f"Mani-Chan", value="Może zaczniemy od właściciela serwera ?", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Niegłupi pomysł, mam za wiele argumentów żeby się zgodził.", inline=False)
							embed.add_field(name=f"{interaction.user.name}", value="na przykład jakich ?", inline=False)
							embed.add_field(name=f"Otaki-Chan", value=f"Musi być miły dla uczestników, odmówimy dalszej pracy na serwerze i co najważniejsze nie może odmówić dwóm ślicznotkom i tobie {interaction.user.name}.", inline=False)
							embed.add_field(name=f"{interaction.user.name}", value="Sądzę że trzeci argument ma najmniejszą szanse powodzenia.", inline=False)
							embed.add_field(name=f"Mani-Chan", value="masz rację, dlatego użyjmy go na samym końcu.", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Dobra w takim razie idziemy go zaprosić", inline=False)

							await interaction.response.edit_message(embed=embed,view=MyConversationOne())

					class MyVillageTen(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title=f"{interaction.user.name}", description="Otaki ale on jest całkowicie nie czytelny jak ja mam z niego korzystać ?", color=0xfceade)
							embed.add_field(name=f"Otaki-Chan", value="Ah Eeeee, no ale będziesz mieć motywację do szybszego rozwoju żeby był czytelny.", inline=False)
							embed.add_field(name="Mani-Chan", value="Siostro, ale z tego co pamiętam na kolejnym poziomie jest napisany Nyanifontem.", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Patrzcie na plusy będzie czytelny i zrozumiały w większym stopniu niż był.", inline=False)
							embed.add_field(name=f"{interaction.user.name}", value="Mam wrażenie że przede mną jeszcze daleka droga.", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="No, tak daleka do póki będą nowe treści.", inline=False)
							embed.add_field(name=f"{interaction.user.name}", value="?", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Nyeważne.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageEleven())

					class MyVillageNine(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description="Proszę weź też to.", color=0xfceade)
							embed.add_field(name=f"{interaction.user.name}", value="Co to za poniszczona książka ?", inline=False)
							embed.add_field(name="Mani-Chan", value=f"To guidebook, magiczna książka która rozwija się wraz z twoim poziomem.", inline=False)
							embed.add_field(name="Mani-Chan", value="Możesz przeczytać w niej przydatne informacje oraz będzie ci przypominać o twoich celach, a dlaczego jest poniszczona to bardzo proste masz pierwszy poziom wiec dlatego tak beznadziejnie wygląda.", inline=False)
							embed.add_field(name=f"Otaki-Chan", value="Wywołujesz ją komendo /guidebook tam doczytasz resztę podstawowych rzeczy tylko nie spodziewaj się że opisy na pierwszym poziomie będą dobre.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageTen())

					class MyVillageEight(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description="Zadowolenie sumuję twoje zadowolenie jak i wioski którą prowadzisz dla przykładu jeśli twój kowal jest niezadowolony obniży ci to poziom.", color=0xfceade)
							embed.add_field(name="Otaki-Chan", value=f"Pamiętaj że bycie nie miłym w stosunku do innych też obniża Zadowolenie.", inline=False)
							embed.add_field(name="Mani-Chan", value=f"A na co wpływa ten poziom ?", inline=False)
							embed.add_field(name="Otaki-Chan", value="Na wszystkie aspekty zaczynając od zdobywania surowców po możliwość wybierania lepszych wyborów.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageNine())

					class MyVillageSeven(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()

							wallet = users[str(user.id)]["wallet"]
							bank = users[str(user.id)]["bank"]
							level = users[str(user.id)]["level"]
							xp = users[str(user.id)]["xp"]
							villager = users[str(user.id)]["villager"]
							happiness = users[str(user.id)]["happiness"]
							color = users[str(user.id)]["color"]
							if happiness <= 0:
								state = "Makabryczne"
							elif happiness <= 5:
								state = "Złe"
							elif happiness <= 10:
								state = "Neutralne"
							elif happiness <= 15:
								state = "Dobre"
							elif happiness <= 20:
								state = "Wspaniałe"
							
							embed=discord.Embed(title="Konto użytkownika:",description=f"{interaction.user}", color=color)
							embed.set_thumbnail(url=f"{interaction.user.avatar}")
							embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
							embed.add_field(name="Punkty doświadczenia:",value=f"🧶 {xp}", inline=False)
							embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
							embed.add_field(name="Mieszkańcy wioski:",value=f"🏘️ {villager}", inline=False)
							embed.add_field(name="Zadowolenie:",value=f"🎭 {happiness} | {state}", inline=True)

							embed.add_field(name="---------------",value=f"", inline=False)

							embed.add_field(name="Otaki-Chan", value=f"Teraz objaśnię ci statystyki znajdujące się na niej", inline=False)
							embed.add_field(name="Otaki-Chan", value=f"Poziom: Ukazuję jak bardzo jesteś uzdolniony i jak złożone rzeczy możesz wykonywać.", inline=False)
							embed.add_field(name="Mani-Chan", value="Punkty doświadczenia: To przyznawana ci punkty doświadczenia za wykonywanie różnych czynności jeśli nazbierasz ich wystarczająco dużo będziesz mógł z nich uszyć wyższy poziom.", inline=False)
							embed.add_field(name="Mani-Chan", value="Otaki-coiny: To waluta panująca w naszym świecie.", inline=False)
							embed.add_field(name="Otaki-Chan", value="Bank: W banku możesz przechowywać swoje zdobyte Otaki-coiny jak i wysyłać je innym.", inline=False)
							embed.add_field(name="Otaki-Chan", value="Mieszkańcy wioski: Pozwala na zobaczyć ile mieszkańców mieszka w naszej wiosce obecnie jest tylko nasza trójka ale będzie rosnąć z czasem.", inline=False)
							embed.add_field(name="Otaki-Chan", value="Zadowolenie: To najbardziej dziwaczna statystyka spróbuję ci to wytłumaczyć najprościej jak tylko potrafię.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageEight())

					class MyVillageSix(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()

							wallet = users[str(user.id)]["wallet"]
							bank = users[str(user.id)]["bank"]
							level = users[str(user.id)]["level"]
							xp = users[str(user.id)]["xp"]
							villager = users[str(user.id)]["villager"]
							happiness = users[str(user.id)]["happiness"]
							color = users[str(user.id)]["color"]
							if happiness <= 0:
								state = "Makabryczne"
							elif happiness <= 5:
								state = "Złe"
							elif happiness <= 10:
								state = "Neutralne"
							elif happiness <= 15:
								state = "Dobre"
							elif happiness <= 20:
								state = "Wspaniałe"
							
							embed=discord.Embed(title="Konto użytkownika:",description=f"{interaction.user}", color=color)
							embed.set_thumbnail(url=f"{interaction.user.avatar}")
							embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
							embed.add_field(name="Punkty doświadczenia:",value=f"🧶 {xp}", inline=False)
							embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
							embed.add_field(name="Mieszkańcy wioski:",value=f"🏘️ {villager}", inline=False)
							embed.add_field(name="Zadowolenie:",value=f"🎭 {happiness} | {state}", inline=True)
							await interaction.response.edit_message(embed=embed,view=MyVillageSeven())

					class MyVillageFive(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Słuchaj uważnie {interaction.user.name} żebyś potem nie zadawał głupich pytań.", color=0xfceade)
							embed.add_field(name="Otaki-Chan", value=f"Proszę daję ci teraz twoją kartę Profilu, będziesz mógł ją wyświetlać kiedy tylko zechcesz jak skończymy ci objaśniać mechaniki panujące tutaj.", inline=False)
							embed.add_field(name="Mani-Chan", value="Możesz też spoglądać na karty innych uczestników jak byłbyś ciekawy jak im idzie.", inline=False)
							embed.add_field(name="Mani-Chan", value="Spójrz tak wygląda twoja.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageSix())

					class MyWoodWorkingFinish(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Narrator", description=f"Po tym jak zgraja naprawiła dom jak i w nim posprzątała zaczęli tłumaczyć {interaction.user.name} podstawowe informacje odnośnie świata i mechanik w nim panujących.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyVillageFive())

					class MyWoodWorkingFive(View):
						@discord.ui.button(label="Otaki-Chan", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description="Ała miało być na przemian, zacznijmy jeszcze raz.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())
							
						@discord.ui.button(label=f"{interaction.user.name}", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Uff, Świetnie się spisałeś {interaction.user.name}", color=0xfceade)
							embed.add_field(name="Mani-Chan", value="Pora wykorzystać przerobione drewno do naprawy naszego domu.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingFinish())

					class MyWoodWorkingFour(View):
						@discord.ui.button(label="Otaki-Chan", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Postęp:", description="4/5", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingFive())
							
						@discord.ui.button(label=f"{interaction.user.name}", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description="Ała miało być na przemian, zacznijmy jeszcze raz.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())

					class MyWoodWorkingThree(View):
						@discord.ui.button(label="Otaki-Chan", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description="Ała miało być na przemian, zacznijmy jeszcze raz.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())
							
						@discord.ui.button(label=f"{interaction.user.name}", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Postęp:", description="3/5", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingFour())

					class MyWoodWorkingTwo(View):
						@discord.ui.button(label="Otaki-Chan", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Postęp:", description="2/5", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingThree())
							
						@discord.ui.button(label=f"{interaction.user.name}", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description="Ała miało być na przemian, zacznijmy jeszcze raz.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())

					class MyWoodWorkingOne(View):
						@discord.ui.button(label="Otaki-Chan", style=discord.ButtonStyle.gray)
						async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description="Ała miało być na przemian, zacznijmy jeszcze raz.", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())
							
						@discord.ui.button(label=f"{interaction.user.name}", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Postęp:", description="1/5", color=0xfceade)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingTwo())

					class MyVillageFour(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Dlatego będziemy używać piły dla dwóch osób.", color=0xfceade)
							embed.add_field(name="Otaki-Chan", value=f"A i pamiętaj że ciągniemy ją naprzemiennie zaczynając od ciebie.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyWoodWorkingOne())

					class MyVillageThree(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Mam nadzieje że dobrze wam się spało ale teraz pora wziąć się za prace.", color=0xfceade)
							embed.add_field(name=f"Mani-chan/{interaction.user.name}", value=f"Dobrze.", inline=False)
							embed.add_field(name="Otaki-Chan", value=f"Najpierw musimy przerobić nasze drewno na deski.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageFour())

					class MyVillageTwo(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Pójdźmy teraz spać a rano zacznijmy już naprawiać nasz dom skoro udało wam się zdobyć drewno.", color=0xfceade)
							embed.add_field(name="Mani-chan", value=f"W takim razie życzę wam Dobranoc.", inline=False)
							embed.add_field(name=f"{interaction.user.name}", value=f"Dobranoc.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageThree())

					class MyChoiceTwo(View):
						@discord.ui.button(label="No", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()
							users[str(user.id)]["happiness"] -= 1

							with open("mainbank.json","w") as f:
								json.dump(users,f)

							embed = discord.Embed(title="Otaki-chan", description=f"To nic nie zmienia, ale jest mi smutno że nie potraficie tego zaakceptować,Hpff", color=0xfceade)
							embed.add_field(name="Narrator", value=f"Mani wraz z {interaction.user.name} zaczęli przepraszać Otaki.", inline=False)
							embed.add_field(name="Narrator", value=f"Pogodzili się i zaakceptowali jej nazewnictwo.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageTwo())

						@discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
						async def success_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()
							users[str(user.id)]["happiness"] += 1

							with open("mainbank.json","w") as f:
								json.dump(users,f)

							embed = discord.Embed(title="Otaki-chan", description=f"Ha, podoba mu się.", color=0xfceade)
							embed.add_field(name="Narrator", value=f"Otaki szeroko się uśmiecha przy czym tańczy dziwny taniec zwycięstwa.", inline=False)
							embed.add_field(name="Mani-Chan", value=f"Przepraszam nie będę miała nic już do twojego nazewnictwa.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyVillageTwo())

					class MyVillage(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-Chan", description=f"Nareszcie jesteście, trochę wam to zajęło.", color=0xfceade)
							embed.add_field(name="Mani-chan", value=f"Siostro {interaction.user.name} nie jest jeszcze tak dobry w ścinaniu drzew.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Do tego wspominał coś o jakieś strzale w kolano.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"To tak jak by byśmy nigdy nie dostali strzałą w kolano. Pfff", inline=False)
							embed.add_field(name="Mani-chan", value=f"Masz rację, Ułożyłaś już plan działania ?", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Tak, Plan jest całkiem prosty:", inline=False)
							embed.add_field(name="Punkt 1.", value=f"Naprawić nasz dom po czym wioskę.", inline=False)
							embed.add_field(name="Punkt 2.", value=f"Zdobyć kilku mieszkańców i sprawić żeby tu zostali.", inline=False)
							embed.add_field(name="Punkt 3.", value=f"Zdobyć fundusze na ulepszenie wioski i takie tam.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Na razie to tyle jest całkiem ogólny ale nadaje mu to tajemniczości.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Siostro naprawdę chciała bym wiedzieć w jakim aspekcie ten plan jest tajemniczy ?", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Nazwałam go Planem Nynsterious.", inline=False)
							embed.add_field(name="Mani-chan", value=f"...", inline=False)
							embed.add_field(name="Mani-chan", value=f"Brak mi słów na twoje nazewnictwo.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"A czy tobie {interaction.user.name} podoba się moje nyazewnictwo ?", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyChoiceTwo())

					class MyForest2(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Mani-Chan", description=f"Ah, tyle drewna nam wystarczy.", color=0xfceade)
							embed.add_field(name="Mani-chan", value=f"Powinniśmy wracać zaczyna się ściemniać.", inline=False)
							embed.set_image(url="https://i.postimg.cc/GmkLzhTn/79b70c4ab1828bf8a189c1a9e8f4dc44.jpg")
							await interaction.response.edit_message(embed=embed,view=MyVillage())

					class MyChop6(View):
							@discord.ui.button(label="Chop 4/5", style=discord.ButtonStyle.grey, emoji="🪓")
							async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
								button.disabled = True
								embed=discord.Embed(title="Mani-Chan",description=f"Udało ci się ściąć pospolite drzewo.", color=0xe9732b)
								embed.set_image(url="https://i.postimg.cc/c4j4vPY4/pien.png")
								await interaction.response.edit_message(embed=embed,view=MyForest2())

					class MyChop5(View):
						@discord.ui.button(label="Chop 3/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)

							embed.set_image(url="https://i.postimg.cc/pXWLcSsd/Untitled432-20220601185505.jpg")
							await interaction.response.edit_message(embed=embed,view=MyChop6())

					class MyChop4(View):
						@discord.ui.button(label="Chop 2/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)
							embed.set_image(url="https://i.postimg.cc/bwdNptcc/Untitled432-20220601185513.jpg")
							await interaction.response.edit_message(embed=embed,view=MyChop5())

					class MyChop3(View):
						@discord.ui.button(label="Chop 1/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)
							embed.set_image(url="https://i.postimg.cc/bwdNptcc/Untitled432-20220601185513.jpg")
							await interaction.response.edit_message(embed=embed,view=MyChop4())

					class MyChop2(View):
						@discord.ui.button(label="Chop 0/5", style=discord.ButtonStyle.grey, emoji="🪓")
						async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Pospolite Drzewo",description=f"", color=0xe9732b)
							embed.set_image(url="https://i.postimg.cc/Wb5bB7yw/bc883370d44e8f633a7b7f6e6e1626d0.jpg")
							await interaction.response.edit_message(embed=embed,view=MyChop3())

					class MyChop(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed=discord.Embed(title="Mani-Chan",description=f"Proszę o to siekierka dla ciebie do ścinania drzew.", color=0xe9732b)
							embed.add_field(name="Mani-Chan", value=f"Niestety ta siekierka jest bardzo słaba wiec trochę zamachów będziesz musiał wykonać.", inline=False)
							embed.set_image(url="https://i.postimg.cc/Wb5bB7yw/bc883370d44e8f633a7b7f6e6e1626d0.jpg")
							await interaction.response.edit_message(embed=embed,view=MyChop2())

					class MyForest(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Mani-Chan", description=f"Spójrz, już widać przed nami las.", color=0xfceade)
							embed.set_image(url="https://i.postimg.cc/L6yMkBjz/anime-art-style-natura-srodowisko-c.png")
							await interaction.response.edit_message(embed=embed,view=MyChop())

					class MyTaskOne(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description=f"Dobrze więc wypadałoby ci wytłumaczyć gdzie jesteśmy.", color=0xfceade)
							embed.add_field(name="Otaki-chan", value=f"Obecnie znajdujemy się w zgliszczach opustoszałej wioski którą chcemy przemienić w cudowne królestwo w którym będzie żyło się szczęśliwie.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Dlatego zacznijmy od Naprawy i posprzątania naszego domu.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Stanie się on naszą bazą z której będziemy wyznaczać sobie cele do zrealizowania.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Dobrze więc ja zajmę się konstruowaniem planu co będziemy musieli po kolei zrobić a ty wraz z Mani udajcie się do pobliskiego lasu zdobyć trochę drewna.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Dobrze w takim razie wyruszamy widzimy się niebawem.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyForest())

					class MyChoiceOne(View):
						@discord.ui.button(label="No", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()
							users[str(user.id)]["happiness"] -= 1

							with open("mainbank.json","w") as f:
								json.dump(users,f)

							embed = discord.Embed(title="Otaki-chan", description=f"Nie takiej odpowiedzi się spodziewałem.", color=0xfceade)
							embed.add_field(name="Narrator", value=f"Otaki-Chan chwyta za miecz pozwalający wymazać kogoś z istnienie na zawsze.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Kiedy moja siostra nie pozostawiła wyboru {interaction.user.name}, zgodził się.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyTaskOne())

						@discord.ui.button(label="Yes", style=discord.ButtonStyle.success)
						async def success_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							await open_account(interaction.user)
							user = interaction.user
							users = await get_bank_date()
							users[str(user.id)]["happiness"] += 1

							with open("mainbank.json","w") as f:
								json.dump(users,f)

							embed = discord.Embed(title="Otaki-chan", description=f"Ooo nareszcie się ktoś ośmielił.", color=0xfceade)
							embed.add_field(name="Narrator", value=f"Otaki się uśmiecha.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Miło mi że zgodziłeś się tego podjąć {interaction.user.name}.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyTaskOne())

					class MyIntroduction(View):
						@discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
						async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							embed = discord.Embed(title="Otaki-chan", description=" Hej Mani skoro prowadzimy już serwer od dłuższego czasu wypadało by coś zrobić co zaciekawiło by naszych uczestników i zwiększyło ich aktywność.", color=0xfceade)
							embed.add_field(name="Otaki-chan", value=f"co o tym sądzisz ?", inline=False)
							embed.add_field(name="Mani-chan", value=f"Masz na to jakiś pomysł siostro ?", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Otóż mam, wykreujemy świat i umieścimy tam każdego uczestnika.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"I nazwiemy To projektem EcoRpg.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Dość niecodzienna ta nazwa, czemu akurat tak ?", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Bo to będzie taka trochę ekonomia a trochę rpg wiec po prostu połączyłam nazwy.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Eh wiesz chyba wolałam nie wiedzieć.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Dobra a ich opowieść będzie zaczynać się tak.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Kiedy w świecie zawitał kurz, kiedy nie było żadnej żywej duszy, pojawił się on przykładny uczestnik i postanowił ożywić ten pozbawiony kolorów świat.", inline=False)
							embed.add_field(name="Mani-chan", value=f"Lecz pozbawiony pomysłu jak tego dokonać poszedł spać i zapomniał o tym miejscu.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Ale na jego miejscu zaczęli pojawiać się inni i oni tak łatwo się nie podadzą.", inline=False)
							embed.add_field(name="Otaki-chan", value=f"Prawda {interaction.user.name} ?", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyChoiceOne())

					embed = discord.Embed(title="Na wstępie:", description=f"Uczestniku chce cię poinformować że EcoRpg jest w bardzo wstępnym etapie tworzenia i mogą zdarzać się błędy. Dlatego bądź wyrozumiały, jeśli zobaczysz jakieś błędy zgłoś je do mnie Kiriu#5567.", color=0xfceade)
					embed.add_field(name="Informacji odnośnie Projektu EcoRpg:", value=f"Projekt jest tworzony tylko przez jedną osobę dlatego w dialogach będzie forma męska zamiast wybrania formy. Dlaczego akurat forma męska ? Ponieważ łatwiej będzie mi ją implementować ze względu bycia przeze mnie mężczyzną.", inline=False)
					embed.set_thumbnail(url="https://i.postimg.cc/bNbTLz11/Gp9-DENh-K-400x400.jpg")
					embed.add_field(name="Zalecenia:", value=f"Upewnij się ze posiadasz najnowszą wersje discorda żeby wszystko działało poprawnie, jak również staraj się nie zwlekać z naciskaniem przycisków bo discord po czasie wyłącza ich odpowiadanie.", inline=False)

					# view = MyWoodWorkingFinish()
					view = MyIntroduction()#Początek
					await interaction.response.send_message(embed=embed,view=view,ephemeral = True)
				
				else:
					await interaction.response.send_message("Ha ha ha zabezpieczyłem się <:madness:981262325174657074>",ephemeral = True)










