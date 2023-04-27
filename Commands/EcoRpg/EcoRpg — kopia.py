from ast import alias
import asyncio
from cmath import cos
from email.message import Message
from pyexpat.errors import messages
from time import time
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

path = 'C:/Users/Kamil/Desktop/OTAKI/Windows-ver/Otaki-Chan/commands/Ekonomia'
#  /home/otaki/Otaki/Otaki-Chan/commands/Ekonomia
#  commands/Ekonomia
os.chdir(path)

dictionary_j = {}
dictionary_j_spr = {}
dictionary_chop = {}
dictionary_chop_spr = {}
dictionary_mine = {}
dictionary_mine_spr = {}
dictionary_fish_number = {}
dictionary_fish = {}
dictionary_fish_spr = {}

class CustomCommands:
	def get_commands(tree,client):

		@client.event
		async def on_command_error(ctx, error):
			if isinstance(error, commands.CommandOnCooldown):
				remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))

				embed = discord.Embed(title=":clock1: Zwolnij Ciutkę", description=f'{ctx.author.mention}, Spróbuj za ' + str(remaining_time), color=0xff0000)
				await ctx.send(embed=embed)

		@client.command(aliases=['profil','PROFIL','p','P'])
		@commands.cooldown(2, 30, commands.BucketType.user)
		async def _profil(ctx,member:discord.Member=None):
			if member == None:
				await open_account(ctx.author)
				user = ctx.author
				users = await get_bank_date()

				wallet = users[str(user.id)]["wallet"]
				bank = users[str(user.id)]["bank"]
				level = users[str(user.id)]["level"]
				
				embed=discord.Embed(title="Konto użytkownika:",description=f"{ctx.author}", color=0xfceade)
				embed.set_thumbnail(url=f"{ctx.author.avatar}")
				embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
				embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
				embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
				await ctx.send(embed=embed)
			else:
				await open_account(member)
				user = member
				users = await get_bank_date()

				wallet = users[str(user.id)]["wallet"]
				bank = users[str(user.id)]["bank"]
				level = users[str(user.id)]["level"]
				
				embed=discord.Embed(title="Konto użytkownika:",description=f"{member.display_name}", color=0xfceade)
				embed.set_thumbnail(url=f"{member.avatar}")
				embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=False)
				embed.add_field(name="Otaki-coiny:", value=f":coin: {wallet}", inline=True)
				embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
				await ctx.send(embed=embed)

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
					users[str(user.id)]["stone"] = 0

				with open("materials.json","w") as f:
					json.dump(users,f)
				return True
		
		async def open_inventory(user):
			with open("inventory.json","r") as f:
				users = await get_inventory_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}

				with open("materials.json","w") as f:
					json.dump(users,f)
				return True

		async def get_inventory_date():
			with open("inventory.json","r") as f:
				users = json.load(f)
			return users

		async def get_materials_date():
			with open("materials.json","r") as f:
				users = json.load(f)
			return users

		async def get_bank_date():
			with open("mainbank.json","r") as f:
				users = json.load(f)
			return users

		async def update_bank(user,change = 0,mode ="wallet"):
			users = await get_bank_date()

			users[str(user.id)][mode] += change

			with open("mainbank.json","w") as f:
				json.dump(users,f)

			bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
			return bal

		@client.command(aliases=['withdraw','Withdraw','WITHDRAW','wit','Wit','WIT'])
		@commands.cooldown(2, 30, commands.BucketType.user)
		async def _withdraw(ctx,amount = None):
			await open_account(ctx.author)

			if amount == None:
				await ctx.send("Proszę podać też kwotę do wypłacenia.")
				return		
			bal = await update_bank(ctx.author)
			if amount == "all" or amount == "All" or amount == "ALL":
				amount = bal[1]
			amount = int(amount)
			if amount>bal[1]:
				await ctx.send("Nie posiadasz tyle pieniędzy na koncie bankowym.")
				return
			if amount<0:
				await ctx.send("Kwota musi być dodatnia")
				return
			await update_bank(ctx.author,amount)
			await update_bank(ctx.author,-1*amount,"bank")
			await ctx.send(f"Wypłaciłeś {amount} Otaki-coinów")

		@client.command(aliases=['deposit','Deposit','DEPOSIT','dep','Dep','DEP'])
		@commands.cooldown(2, 30, commands.BucketType.user)
		async def _deposit(ctx,amount = None):
			await open_account(ctx.author)

			if amount == None:
				await ctx.send("Proszę podać też kwotę do wpłacenia.")		
				return
			bal = await update_bank(ctx.author)
			if amount == "all" or amount == "All" or amount == "ALL":
				amount = bal[0]
			amount = int(amount)
			if amount>bal[0]:
				await ctx.send("Nie posiadasz tyle pieniędzy.")
				return
			if amount<0:
				await ctx.send("Kwota musi być dodatnia")
				return

			await update_bank(ctx.author,-1*amount)
			await update_bank(ctx.author,amount,"bank")
			await ctx.send(f"Wpłaciłeś {amount} Otaki-coinów.")

		@client.command(aliases=['send24','Send24','SEND24','Przelew24','przelew24','PRZELEW24'])
		@commands.cooldown(1, 60*60*24, commands.BucketType.user)
		async def _send24(ctx,member:discord.Member,amount = None):
			await open_account(ctx.author)
			await open_account(member)
			
			if amount == None:
				await ctx.send("Proszę podać też kwotę do wysłania.")		
				return
			bal = await update_bank(ctx.author)
			if amount == "all" or amount == "All" or amount == "ALL":
				amount = bal[1]
			amount = int(amount)
			if amount>bal[1]:
				await ctx.send("Nie posiadasz tyle pieniędzy.")
				return
			if amount<0:
				await ctx.send("Kwota musi być dodatnia")
				return

			await update_bank(ctx.author,-1*amount,"bank")
			await update_bank(member,amount,"bank")
			await ctx.send(f"Przelałeś {amount} Otaki-coinów.")

		@client.command(aliases=['sendn','Sendn','SENDN','sendN','SendN','Przelewn','PrzelewN','przelewn','przelewN','PRZELEWn','PRZELEWN','PRZELEWNATYCHMIATOWY','Przelewnatychmiastowy','PrzelewNatychmiastowy'])
		@commands.cooldown(2, 30, commands.BucketType.user)
		async def _sendn(ctx,member:discord.Member,amount = None):
			await open_account(ctx.author)
			await open_account(member)
			if amount == None:
				await ctx.send("Proszę podać też kwotę do wysłania.")		
				return
			bal = await update_bank(ctx.author)
			procent = int(3000)
			if amount == "all" or amount == "All" or amount == "ALL":
				amount = bal[1]
			amount = int(amount)
			finalna_kwota = amount + procent
			if finalna_kwota>bal[1]:
				await ctx.send("Nie posiadasz tyle pieniędzy.")
				return
			if amount<0:
				await ctx.send("Kwota musi być dodatnia")
				return

			await update_bank(ctx.author,-1*finalna_kwota,"bank")
			await update_bank(member,amount,"bank")
			await ctx.send(f"Przelałeś {amount} Otaki-coinów.")

		@client.command(aliases=['job','JOB','j','J','Praca','PRACA','Job'])
		async def _job(ctx):

			if dictionary_j_spr.get(ctx.author.id) and dictionary_j_spr[ctx.author.id]["wyslane"] == True:
				await ctx.send(f"Dokończ swoją poprzednią pracę {ctx.author.mention}")
				return

			if dictionary_j.get(ctx.author.id):
				time_end = dictionary_j[ctx.author.id]["time_end"] 
				if time.time()>time_end:
					dictionary_j.pop(ctx.author.id)
				else:
					remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
					await ctx.send(f"Zostało ci {remaining_time}")
					return

			dictionary_j_spr[ctx.author.id] = {"wyslane":True}

			class MySelectView(View):
						@discord.ui.select(
							placeholder="Kliknij Tu i Wybierz Prace.",
								options=[

									discord.SelectOption(
										label="Szybka Praca",
										description="Zbieranie Grzybów 1h",
										value="1x0",
										emoji="<:mushroom_smb:979128655403962389>",
									),

									discord.SelectOption(
										label="Średnia Praca",
										description="Pilnowanie Owiec 3h",
										value="2x0",
										emoji="🐑",
									),

									discord.SelectOption(
										label="Długa Praca",
										description="Pomaganie na Farmie 6h",
										value="3x0",
										emoji="🧑‍🌾",
									),	
								],)
				
						async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
							select.disabled = True
							if select.values[0] == "1x0":
									await interaction.response.edit_message(content="Wybrałeś Szybką Prace",view=None)

									dictionary_j[ctx.author.id] = {"time_end":time.time()+60*15}

									await open_account(ctx.author)
									users = await get_bank_date()
									user = ctx.author

									reward = 55
									reward_xp = 15

									users[str(user.id)]["wallet"] += reward
									users[str(user.id)]["xp"] += reward_xp

									with open("mainbank.json","w") as f:
										json.dump(users,f)
									
									dictionary_j_spr[ctx.author.id]["wyslane"] = False

									embed=discord.Embed(title="Za Zbieranie Grzybów",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa" , color=0xfceade)
									embed.set_thumbnail(url=f"https://i.postimg.cc/3N8TkQ3N/depositphotos-62799645-stock-illustration-mushrooms-in-a-wicker-basket.webp")
									await ctx.author.send(embed=embed)


							if select.values[0] == "2x0":
								await interaction.response.edit_message(content="Wybrałeś Średnią Prace",view=None)

								dictionary_j[ctx.author.id] = {"time_end":time.time()+60*30}

								await open_account(ctx.author)
								users = await get_bank_date()
								user = ctx.author							

								reward = 185
								reward_xp = 51

								users[str(user.id)]["wallet"] += reward
								users[str(user.id)]["xp"] += reward_xp

								with open("mainbank.json","w") as f:
									json.dump(users,f)

								dictionary_j_spr[ctx.author.id]["wyslane"] = False

								embed=discord.Embed(title="Za Pilnowanie Owiec",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa", color=0xfceade)
								embed.set_thumbnail(url=f"https://i.postimg.cc/y6jKwxTZ/1560202783-otakuap-wooloo.jpg")
								await ctx.author.send(embed=embed)

							if select.values[0] == "3x0":
								await interaction.response.edit_message(content="Wybrałeś Długą Prace",view=None)

								dictionary_j[ctx.author.id] = {"time_end":time.time()+60*60}

								await open_account(ctx.author)
								users = await get_bank_date()
								user = ctx.author									

								reward = 450 #Nagroda za 6 h
								reward_xp = 173

								users[str(user.id)]["wallet"] += reward
								users[str(user.id)]["xp"] += reward_xp

								with open("mainbank.json","w") as f:
									json.dump(users,f)

								dictionary_j_spr[ctx.author.id]["wyslane"] = False

								embed=discord.Embed(title="Za Pomoc Na Farmie",description=f"Otrzymujesz \n-{reward} Otaki-coinów\n-{reward_xp} XPa", color=0xfceade)
								embed.set_thumbnail(url=f"https://i.postimg.cc/jdjTKT8k/87e9225272bd536997e1652d0d41f935.jpg")
								await ctx.author.send(embed=embed)

			view = MySelectView()
			await  ctx.author.send(f"Wybierz prace spośród podanych:",view=view)

		@client.command(aliases=['materials','MATERIALS','MAT','mat','Mat','Materials'])
		@commands.cooldown(2, 30, commands.BucketType.user)
		async def _materials(ctx,member:discord.Member=None):
			if member == None:
				await open_account_materials(ctx.author)

				user = ctx.author
				users = await get_materials_date()

				wood = users[str(user.id)]["wood"]
				stone = users[str(user.id)]["stone"]

				embed=discord.Embed(title="Materiały użytkownika:",description=f"{ctx.author}", color=0xfceade)
				embed.set_thumbnail(url=f"{ctx.author.avatar}")
				embed.add_field(name="Drewno:", value=f"<:diywoodnormalinventarioassetsacn:979761455291318302> {wood}", inline=True)
				embed.add_field(name="Kamienie:",value=f"<:27794907:979764802232651856> {stone}", inline=True)
				await ctx.send(embed=embed)
			else:
				await open_account_materials(member)

				user = member
				users = await get_materials_date()

				wood = users[str(user.id)]["wood"]
				stone = users[str(user.id)]["stone"]

				embed=discord.Embed(title="Materiały użytkownika:",description=f"{member.display_name}", color=0xfceade)
				embed.set_thumbnail(url=f"{member.avatar}")
				embed.add_field(name="Drewno:", value=f"<:diywoodnormalinventarioassetsacn:979761455291318302> {wood}", inline=True)
				embed.add_field(name="Kamienie:",value=f"<:27794907:979764802232651856> {stone}", inline=True)
				await ctx.send(embed=embed)

		@client.command(aliases=['chop','CHOP','Chop'])
		async def _chop(ctx):
			channel = discord.utils.get(ctx.guild.channels, name="🌲las🌲")
			channel = discord.utils.get(ctx.guild.channels, id = 978982604097347664)

			if  ctx.channel == channel:

				if dictionary_chop_spr.get(ctx.author.id) and dictionary_chop_spr[ctx.author.id]["wyslane"] == True:
					await ctx.send(f"Dokończ swoje poprzednie drzewo {ctx.author.mention}")
					return

				if dictionary_chop.get(ctx.author.id):
					time_end = dictionary_chop[ctx.author.id]["time_end"] 
					if time.time()>time_end:
						dictionary_chop.pop(ctx.author.id)
					else:
						remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
						await ctx.send(f"Zostało ci {remaining_time}")
						return

				dictionary_chop_spr[ctx.author.id] = {"wyslane":True}
				dictionary_chop[ctx.author.id] = {"time_end":time.time()+60*60}

			

				class MyView5(View):
					@discord.ui.button(label="Chop 4/5", style=discord.ButtonStyle.grey, emoji="🪓")
					async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						await open_account_materials(ctx.author)
						users = await get_materials_date()
						user = ctx.author

						random_wood = int(random.uniform(2,5))
						users[str(user.id)]["wood"] += random_wood

						with open("materials.json","w") as f:
							json.dump(users,f)
						
						await open_account(ctx.author)
						users = await get_bank_date()
						user = ctx.author

						reward_xp = 5
						users[str(user.id)]["xp"] += reward_xp

						with open("mainbank.json","w") as f:
							json.dump(users,f)


						dictionary_chop_spr[ctx.author.id]["wyslane"] = False

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
				await ctx.author.send(embed=embed, view=view)

			else:
				await ctx.send(f"Nye jesteś w lesie :evergreen_tree:{ctx.author.mention}:evergreen_tree:")

		@client.command(aliases=['mine','MINE','Mine'])
		async def _mine(ctx):

			if dictionary_mine_spr.get(ctx.author.id) and dictionary_mine_spr[ctx.author.id]["wyslane"] == True:
				await ctx.send(f"Dokończ swój kamień {ctx.author.mention}")
				return
			
			if dictionary_mine.get(ctx.author.id):
				time_end = dictionary_mine[ctx.author.id]["time_end"] 
				if time.time()>time_end:
					dictionary_mine.pop(ctx.author.id)
				else:
					remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
					await ctx.send(f"Zostało ci {remaining_time}")
					return

			dictionary_mine_spr[ctx.author.id] = {"wyslane":True}
			dictionary_mine[ctx.author.id] = {"time_end":time.time()+60*60}

			class MyView5(View):
				@discord.ui.button(label="Mine 4/5", style=discord.ButtonStyle.grey, emoji="⛏️")
				async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
					button.disabled = True

					await open_account_materials(ctx.author)
					users = await get_materials_date()
					user = ctx.author

					random_stone = int(random.uniform(2,5))
					users[str(user.id)]["stone"] += random_stone

					with open("materials.json","w") as f:
						json.dump(users,f)
					
					await open_account(ctx.author)
					users = await get_bank_date()
					user = ctx.author

					reward_xp = 5
					users[str(user.id)]["xp"] += reward_xp

					with open("mainbank.json","w") as f:
						json.dump(users,f)

					dictionary_mine_spr[ctx.author.id]["wyslane"] = False

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
			await ctx.author.send(embed=embed, view=view)

		@client.command(aliases=['xp','Xp','XP','xP'])
		async def _xp(ctx):
			await open_account(ctx.author)



















		@client.command(aliases=['fish','FISH','Fish'])
		async def _fish(ctx):

			if dictionary_fish_spr.get(ctx.author.id) and dictionary_fish_spr[ctx.author.id]["wyslane"] == True:
				await ctx.send(f"Dokończ swój połów {ctx.author.mention}")
				return

			if dictionary_fish.get(ctx.author.id):
				time_end = dictionary_fish[ctx.author.id]["time_end"] 
				if time.time()>time_end:
					dictionary_fish.pop(ctx.author.id)
				else:
					remaining_time = time.strftime("%M:%S", time.localtime(time_end-time.time()))
					await ctx.send(f"Zostało ci {remaining_time}")
					return

			dictionary_fish_spr[ctx.author.id] = {"wyslane":True}
			dictionary_fish[ctx.author.id] = {"time_end":time.time()+5}

			class MyView2(View):
				@discord.ui.select(
				placeholder="Kliknij Tu i Wybierz Liczbę.",
					options=[
						discord.SelectOption(
							label="1",
							value="1",
						),

						discord.SelectOption(
							label="2",
							value="2",
						),

						discord.SelectOption(
							label="3",
							value="3",
						),	
					],)

				async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
					select.disabled = True
					if select.values[0] == dictionary_fish_number[ctx.author.id]["odp"]:

						dictionary_fish_spr[ctx.author.id] = {"wyslane":False}
						embed=discord.Embed(title="Udało Ci Się Złowić Rybkę",description=f"bla bla bla blaaa", color=0x00f8ff)
						embed.set_image(url="https://i.postimg.cc/5yTWjzsw/maple-anime.gif")
						await interaction.response.edit_message(embed=embed,view=None)
					elif select.values[0] == dictionary_fish_number[ctx.author.id]["odp"]:
						
						dictionary_fish_spr[ctx.author.id] = {"wyslane":False}
						embed=discord.Embed(title="Udało Ci Się Złowić Rybkę",description=f"bla bla bla blaaa", color=0x00f8ff)
						embed.set_image(url="https://i.postimg.cc/5yTWjzsw/maple-anime.gif")
						await interaction.response.edit_message(embed=embed,view=None)
					else:
						dictionary_fish_spr[ctx.author.id] = {"wyslane":False}
						embed=discord.Embed(title="Nie Udało Ci Się Złowić Rybki",description=f"Może, może następnym razem uda mi się ją złowić", color=0x00f8ff)
						embed.set_image(url="https://i.postimg.cc/L62gB88f/pain-sad.gif")
						await interaction.response.edit_message(embed=embed,view=None)

			class MyView(View):
				@discord.ui.button(label="Prosty Zarzut", style=discord.ButtonStyle.green)
				async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
					button.disabled = True
					one_random_number = randint(1,3)
					dictionary_fish_number[ctx.author.id] = {"odp":str(one_random_number)}
					if (one_random_number == 1):
						jeden = ["https://i.postimg.cc/mD0fbZX0/1x1.png",
						"https://i.postimg.cc/9fQjbnwN/1x2.png",
						"https://i.postimg.cc/PxLnsv4W/1x3.png",
						"https://i.postimg.cc/pdcM6JDV/1x4.png",
						"https://i.postimg.cc/XY8bwbqC/1x5.png"]

						embed.set_image(url=f"{random.choice(jeden)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(1)
						embed.set_image(url="https://i.postimg.cc/B6yLL72f/patern.png")
						await interaction.response.edit_message(embed=embed,view=MyView2())

					elif (one_random_number == 2):
						dwa = ["https://i.postimg.cc/J4DPsBvn/2x1.png",
						"https://i.postimg.cc/RFgXH1v3/2x2.png",
						"https://i.postimg.cc/Vv54BSNK/2x3.png",
						"https://i.postimg.cc/0j3nt8MP/2x4.png",
						"https://i.postimg.cc/qRJ1qDHV/2x5.png"]
						
						embed.set_image(url=f"{random.choice(dwa)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(1)
						embed.set_image(url="https://i.postimg.cc/B6yLL72f/patern.png")
						await interaction.response.edit_message(embed=embed,view=MyView2())

					elif (one_random_number == 3):
						trzy = ["https://i.postimg.cc/Fs7RL0j2/3x1.png",
						"https://i.postimg.cc/VvNN4C20/3x2.png",
						"https://i.postimg.cc/MHrpLG8P/3x3.png",
						"https://i.postimg.cc/pV0rrsnf/3x4.png",
						"https://i.postimg.cc/ydjdFPpz/3x5.png"]

						embed.set_image(url=f"{random.choice(trzy)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(1)
						embed.set_image(url="https://i.postimg.cc/B6yLL72f/patern.png")
						await interaction.response.edit_message(embed=embed,view=MyView2())

					else:
						await ctx.send("Error")

				@discord.ui.button(label="Trudny Zarzut", style=discord.ButtonStyle.danger)
				async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
					button.disabled = True
					two_random_number = randint(1,3)
					dictionary_fish_number[ctx.author.id] = {"odp":str(two_random_number)}

					if (two_random_number == 1):
						jeden = ["https://i.postimg.cc/h4bB7xhP/1x1.png",
						"https://i.postimg.cc/fTCD1Xhg/1x1x1.png",
						"https://i.postimg.cc/6Q2K7m4D/1x1x2.png",
						"https://i.postimg.cc/jdxr65J6/1x1x3.png",
						"https://i.postimg.cc/Z50tgMHC/1x1x5.png",
						"https://i.postimg.cc/d0bYGj8D/1x2.png",
						"https://i.postimg.cc/W14TV3Np/1x3.png",
						"https://i.postimg.cc/WpM26CYV/1x4.png",
						"https://i.postimg.cc/zX8qd74g/1x5.png",
						"https://i.postimg.cc/52k12VyB/1x6.png",
						"https://i.postimg.cc/1tDZBVHB/1x7.png",
						"https://i.postimg.cc/ZKwzwSrG/1x1x4.png"]

						embed.set_image(url=f"{random.choice(jeden)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(5)
						embed.set_image(url="https://i.postimg.cc/Y2PwxjXF/pexels-photo-932638.png")
						await interaction.response.edit_message(embed=embed,view=None)

					elif (two_random_number == 2):
						dwa = ["https://i.postimg.cc/90scPLLn/2x1.png",
						"https://i.postimg.cc/C5RFf3s8/2x2.png",
						"https://i.postimg.cc/Xvg7Mcvr/2x3.png",
						"https://i.postimg.cc/NMJsFsmY/2x4.png",
						"https://i.postimg.cc/sfLfR234/2x5.png",
						"https://i.postimg.cc/7L4YQQqv/2x6.png",
						"https://i.postimg.cc/PxrfdpL2/2x7.png",
						"https://i.postimg.cc/sDZjfRXd/2x2x1.png",
						"https://i.postimg.cc/hjjnHkwY/2x2x2.png",
						"https://i.postimg.cc/BvNs7ShD/2x2x3.png",
						"https://i.postimg.cc/SKmkG2Gk/2x2x4.png",
						"https://i.postimg.cc/GmFbYJGX/2x2x5.png"]
						
						embed.set_image(url=f"{random.choice(dwa)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(5)
						embed.set_image(url="https://i.postimg.cc/Y2PwxjXF/pexels-photo-932638.png")
						await interaction.response.edit_message(embed=embed,view=None)

					elif (two_random_number == 3):
						trzy = ["https://i.postimg.cc/Z5SJwZBL/3x1.png",
						"https://i.postimg.cc/sDSVP1XX/3x2.png",
						"https://i.postimg.cc/BZRS12Jk/3x3.png",
						"https://i.postimg.cc/prhSH97n/3x4.png",
						"https://i.postimg.cc/Dwqt0Xzr/3x5.png",
						"https://i.postimg.cc/2ysK8kR9/3x6.png",
						"https://i.postimg.cc/nL2gYfBM/3x7.png",
						"https://i.postimg.cc/3RbqVjLT/3x3x1.png",
						"https://i.postimg.cc/bvp4twGK/3x3x2.png",
						"https://i.postimg.cc/0ygT9f95/3x3x3.png",
						"https://i.postimg.cc/63QSMbfc/3x3x4.png",
						"https://i.postimg.cc/gJQW8Pb8/3x3x5.png"]

						embed.set_image(url=f"{random.choice(trzy)}")
						await interaction.message.edit(embed=embed,view=None)
						await asyncio.sleep(5)
						embed.set_image(url="https://i.postimg.cc/Y2PwxjXF/pexels-photo-932638.png")
						await interaction.response.edit_message(embed=embed,view=None)

			view = MyView()
			embed=discord.Embed(title="Zwyczajny Połów",description=f"", color=0x00f8ff)
			embed.set_image(url="https://i.postimg.cc/qRnxqQrZ/breakwater-hina-tsurugi.gif")
			await ctx.send(embed=embed, view=view)

		@client.command(aliases=['Start','START','start'])
		async def _Start(ctx):
			await open_account(ctx.author)
			embed = discord.Embed(title="Otaki-Chan", description="", color=0xfceade)
			embed.set_thumbnail(url="https://i.postimg.cc/9fwTJ735/Untitled373-2.png")
			embed.add_field(name="Informacje:", value="Relacja-???\nPoziom-???", inline=False)
			embed.add_field(name="Okno dialogowe:", value="TEKSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT", inline=False)


			await ctx.send(embed=embed)
			await ctx.author.send(f"")









