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

dictionary_bank_transfer = {}

with open("./config.json") as f:
	config = json.load(f)

class CustomCommands:
	def get_commands(tree,client):

		os.chdir('./Commands/Arkwardiz')

		@tree.command(name = "profile", description= "Pokazuję twój serwerowy profil.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,member:discord.Member=None):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
			if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
				if member == None:
					
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()

					await open_flag_profile(interaction.user)
					userf = interaction.user
					usersf = await get_profile_flag_date()
					flag11 = usersf[str(userf.id)]["flag11"]
					flag12 = usersf[str(userf.id)]["flag12"]

					wallet = users[str(user.id)]["wallet"]
					bank = users[str(user.id)]["bank"]
					level = users[str(user.id)]["level"]
					text = users[str(user.id)]["text"]
					nav = users[str(user.id)]["nav"]
					footer = users[str(user.id)]["footer"]
					banner = users[str(user.id)]["banner"]
					emoji = users[str(user.id)]["emoji"]
					color = users[str(user.id)]["color"]
					history = users[str(user.id)]["history"]
					badge = ""
					if Role.administrator(interaction) in interaction.user.roles:
						badge += "<:0A14_Megumin:1095438874945269841>"
					if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
						badge += " <:H12conflict:921394533449744394>"
					if Role.server_booster(interaction) in interaction.user.roles:
						badge += " <:0A41_love:1063248751889743968>"
					if Role.uczestnicy_plus(interaction) in interaction.user.roles:
						badge += " 💎"
					if Role.plus(interaction) in interaction.user.roles:
						badge += " <:D1_plus1:981257475078639676>"
					if flag11 == 1:
						badge += " <:0A17_wow:1063241073121562634>"
					if flag12 == 1:
						badge += " 📝"

		
					my_color = discord.Color.from_str(color)
					embed=discord.Embed(title="Konto użytkownika:",description=f"{interaction.user.name}", color=my_color)
					embed.set_thumbnail(url=f"{interaction.user.avatar}")
					embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=True)
					embed.add_field(name="Odznaki:",value=f"{badge}", inline=True)
					embed.add_field(name="Historie:",value=f"📚 {history}/5", inline=True)
					embed.add_field(name="Otimi-coiny:", value=f":coin: {wallet}", inline=True)
					embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
					embed.add_field(name=f"",value=f"", inline=False)
					embed.add_field(name=f"{emoji} {nav}",value=f"{text}", inline=False)
					embed.set_image(url=f"{banner}")
					embed.set_footer(text=f"{footer}")
					await interaction.response.send_message(embed=embed,ephemeral = True)

				else:
					await open_profile(member)
					user = member
					users = await get_profile_date()

					await open_flag_profile(member)
					userf = member
					usersf = await get_profile_flag_date()
					flag11 = usersf[str(userf.id)]["flag11"]
					flag12 = usersf[str(userf.id)]["flag12"]

					wallet = users[str(user.id)]["wallet"]
					bank = users[str(user.id)]["bank"]
					level = users[str(user.id)]["level"]
					text = users[str(user.id)]["text"]
					nav = users[str(user.id)]["nav"]
					footer = users[str(user.id)]["footer"]
					banner = users[str(user.id)]["banner"]
					emoji = users[str(user.id)]["emoji"]
					color = users[str(user.id)]["color"]
					history = users[str(user.id)]["history"]
					badge = ""
					if Role.administrator_m(member) in member.roles:
						badge += "<:0A14_Megumin:1095438874945269841>"
					if Role.moderatorzy_m(member) in member.roles or Role.administrator_m(member) in member.roles:
						badge += " <:H12conflict:921394533449744394>"
					if Role.server_booster_m(member) in member.roles:
						badge += " <:0A41_love:1063248751889743968>"
					if Role.uczestnicy_plus_m(member) in member.roles:
						badge += " 💎"
					if Role.plus_m(member) in member.roles:
						badge += " <:D1_plus1:981257475078639676>"
					if flag11 == 1:
						badge += " <:0A17_wow:1063241073121562634>"
					if flag12 == 1:
						badge += " 📝"

		
					my_color = discord.Color.from_str(color)
					embed=discord.Embed(title="Konto użytkownika:",description=f"{member.display_name}", color=my_color)
					embed.set_thumbnail(url=f"{member.avatar}")
					embed.add_field(name="Poziom:",value=f"<:7219arrowup:972095071115689985> {level}", inline=True)
					embed.add_field(name="Odznaki:",value=f"{badge}", inline=True)
					embed.add_field(name="Historie:",value=f"📚 {history}/5", inline=True)
					embed.add_field(name="Otimi-coiny:", value=f":coin: {wallet}", inline=True)
					embed.add_field(name="Bank:",value=f":bank: {bank}", inline=True)
					embed.add_field(name=f"",value=f"", inline=False)
					embed.add_field(name=f"{emoji} {nav}",value=f"{text}", inline=False)
					embed.set_image(url=f"{banner}")
					embed.set_footer(text=f"{footer}")
					await interaction.response.send_message(embed=embed)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
		
		async def open_profile(user):
			with open("userprofile.json","r") as f:
				users = await get_profile_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}
					users[str(user.id)]["wallet"] = 0
					users[str(user.id)]["bank"] = 0
					users[str(user.id)]["level"] = 1
					users[str(user.id)]["text"] = ""
					users[str(user.id)]["nav"] = ""
					users[str(user.id)]["footer"] = ""
					users[str(user.id)]["banner"] = ""
					users[str(user.id)]["emoji"] = ""
					users[str(user.id)]["color"] = "#fceade"
					users[str(user.id)]["history"] = 0

				with open("userprofile.json","w") as f:
					json.dump(users,f)
				return True

		async def get_profile_date():
			with open("userprofile.json","r") as f:
				users = json.load(f)
			return users
		
		async def update_bank(user,change = 0,mode ="wallet"):
			users = await get_profile_date()

			users[str(user.id)][mode] += change

			with open("userprofile.json","w") as f:
				json.dump(users,f)

			bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
			return bal

		async def open_flag_profile(user):
			with open("userprofile.json","r") as f:
				users = await get_profile_flag_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}
					users[str(user.id)]["flag1"] = 0
					users[str(user.id)]["flag2"] = 0
					users[str(user.id)]["flag3"] = 0
					users[str(user.id)]["flag4"] = 0
					users[str(user.id)]["flag5"] = 0
					users[str(user.id)]["flag6"] = 0
					users[str(user.id)]["flag7"] = 0
					users[str(user.id)]["flag8"] = 0
					users[str(user.id)]["flag9"] = 0
					users[str(user.id)]["flag10"] = 0
					users[str(user.id)]["flag11"] = 0
					users[str(user.id)]["flag12"] = 0
					users[str(user.id)]["flag13"] = 0
					users[str(user.id)]["flag14"] = 0
					users[str(user.id)]["flag15"] = 0

				with open("userflag.json","w") as f:
					json.dump(users,f)
				return True

		async def get_profile_flag_date():
			with open("userflag.json","r") as f:
				users = json.load(f)
			return users

		@tree.command(name = "deposit", description= "Pozwala ci wpłacić Otimi-coiny do banku.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
			if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
				await open_profile(interaction.user)

				if amount == None:
					await interaction.response.send_message("Proszę podać też kwotę do wpłacenia.", ephemeral = True)	
					return
				bal = await update_bank(interaction.user)
				if amount == 000:
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
				await interaction.response.send_message(f"Wpłaciłeś {amount} Otimi-coinów.", ephemeral = True)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "withdraw", description= "Pozwala ci wypłacić pieniądze z banku.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
			if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
				await open_profile(interaction.user)
				if amount == None:
					await interaction.response.send_message("Proszę podać też kwotę do wypłacenia.", ephemeral = True)
					return		
				bal = await update_bank(interaction.user)
				if amount == 000:
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
				await interaction.response.send_message(f"Wypłaciłeś {amount} Otimi-coinów.", ephemeral = True)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "bank_transfer", description= "Pozwala na przelewanie pieniędzy z banku do banków innych uczestników serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int , member:discord.Member):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag7 = usersf[str(userf.id)]["flag7"]
			if flag7 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					if dictionary_bank_transfer.get(interaction.user.id):
						time_end = dictionary_bank_transfer[interaction.user.id]["time_end"] 
						if time.time()>time_end:
							dictionary_bank_transfer.pop(interaction.user.id)
						else:
							remaining_time = time.strftime("%T", time.localtime(time_end-time.time()))
							await interaction.response.send_message(f"Musisz odczekać jeszcze {remaining_time} {interaction.user.mention}.", ephemeral = True)
							return
					
					await open_profile(interaction.user)
					await open_profile(member)
					
					if amount == None:
						await interaction.response.send_message("Proszę podaj też kwotę do wysłania.",ephemeral = True)		
						return
					bal = await update_bank(interaction.user)
					amount = int(amount)
					if amount>bal[1]:
						await interaction.response.send_message("Nie posiadasz tyle pieniędzy w banku do wysłania.",ephemeral = True)	
						return
					if amount<0:
						await interaction.response.send_message("Kwota do wysłania musi być dodatnia.",ephemeral = True)
						return

					dictionary_bank_transfer[interaction.user.id] = {"time_end":time.time()+23*60*60}
					await update_bank(interaction.user,-1*amount,"bank")
					await update_bank(member,amount,"bank")
					await interaction.response.send_message(f"Dokonałeś przelewu o wartości {amount} Otimi-coinów na konto użytkownika {member.mention}.",ephemeral = False)

				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye odblokowałeś jeszcze tej komendy {interaction.user.mention}", ephemeral = True)

		@tree.command(name = "instantbank_transfer", description= "Działa tak samo jak zwykły bank_transfer ale nie musisz odczekiwać dnia na kolejny przelew.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int , member:discord.Member):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag7 = usersf[str(userf.id)]["flag7"]
			if flag7 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					await open_profile(member)

					if amount == None:
						await interaction.response.send_message("Proszę podaj też kwotę do wysłania.",ephemeral = True)	
						return
					bal = await update_bank(interaction.user)
					procent = int(5)
					amount = int(amount)
					finalna_kwota = amount + procent
					if finalna_kwota>bal[1]:
						await interaction.response.send_message("Nie posiadasz tyle pieniędzy do wysłania.\nPamiętaj że prowizja banku wynosi 5 Otimi-coinów.",ephemeral = True)	
						return
					if amount<0:
						await interaction.response.send_message("Kwota do wysłania musi być dodatnia.",ephemeral = True)
						return

					await update_bank(interaction.user,-1*finalna_kwota,"bank")
					await update_bank(member,amount,"bank")
					await interaction.response.send_message(f"Dokonałeś przelewu o wartości {amount} Otimi-coinów na konto użytkownika {member.mention}.",ephemeral = False)
			
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye odblokowałeś jeszcze tej komendy {interaction.user.mention}", ephemeral = True)

		@tree.command(name = "give", description= "Dzięki tej komendzie administracja serwera przyznaje punkty uczestnikom serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				guild = client.get_guild(698522294414344232)
				point_channel = guild.get_channel(925191790284406805)
				class MySelectView(View):
					@discord.ui.select(
						placeholder="Wybierz kategorie punktów.",
							options=[

								discord.SelectOption(
									label="Zbumpowanie serwera",
									description="1 Otimi-coin.",
									value="1",
									emoji="<:A31_scared:921400267516280892>",
								),

								discord.SelectOption(
									label="Przywitanie nowej osoby",
									description="2 Otimi-coin.",
									value="2",
									emoji="<:C13_hello3:1063246723440455791>",
								),

								discord.SelectOption(
									label="Spora konwersacja z nową osobą",
									description="2 Otimi-coin.",
									value="3",
									emoji="<:B10_Sleepy:1098727239375388793>",
								),

								discord.SelectOption(
									label="Zachęcenie nowych do vc",
									description="2 Otimi-coin.",
									value="4",
									emoji="<a:A28_joinvc:921400267474358292>",
								),

								discord.SelectOption(
									label="Zapraszanie nowych osób",
									description="1 Otimi-coin.",
									value="5",
									emoji="<:H6ples:927237845410775070>",
								),

								discord.SelectOption(
									label="Wyłapywanie małych błędów na Otaki",
									description="3 Otimi-coin.",
									value="6",
									emoji="<:C16_think:981262325061419009>",
								),

								discord.SelectOption(
									label="Wyłapywanie poważnych błędów na Otaki",
									description="9 Otimi-coin.",
									value="7",
									emoji="<:0A21_mentalbreakdown:926276740437921843>",
								),

								discord.SelectOption(
									label="Uczestnicy których przywitałeś rozmawiają na tekstowym",
									description="10 Otimi-coin.",
									value="8",
									emoji="<:G13_whatsup:981260513197588550>",
								),

								discord.SelectOption(
									label="Uczestnicy których przywitałeś rozmawiają na głosowym",
									description="20 Otimi-coin.",
									value="9",
									emoji="<:0A41_love:1063248751889743968>",
								),

								discord.SelectOption(
									label="Uczestnicy którzy dużo pisali na kanałach tekstowych",
									description="Co miesięczne 5 Otimi-coin.",
									value="10",
									emoji="<:A29_triggered:921394505192734751>",
								),

								discord.SelectOption(
									label="Uczestnicy którzy dużo rozmawiali na kanałach głosowych",
									description="Co miesięczne 7 Otimi-coin.",
									value="11",
									emoji="<:C15_madness:981262325174657074>",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True
						if select.values[0] == "1":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 1

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za zbumpowanie serwera {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

						if select.values[0] == "2":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 2

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za przywitanie nowej osoby {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)
						
						if select.values[0] == "3":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 2

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za sporą konwersacje z nową osobą {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)
						
						if select.values[0] == "4":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 2

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za zachęcenie nowych do vc{member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)
						
						if select.values[0] == "5":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 1

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za zapraszanie nowych osób{member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)
						
						if select.values[0] == "6":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 3

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za wyłapywanie małych błędów na Otaki {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_image(url="https://i.postimg.cc/XJ7WbJtF/hanamaru-kindergarten-anime.gif")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

						if select.values[0] == "7":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 9

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za wyłapywanie poważnych błędów na Otaki {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_image(url="https://i.postimg.cc/bJChNPj5/yummy-anime.gif")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

						if select.values[0] == "8":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 10

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za uczestników których przywitałeś rozmawiają na tekstowym {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_image(url="https://i.postimg.cc/Qd17Hpqp/happy-anime.gif")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)
						
						if select.values[0] == "9":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 20

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za uczestników których przywitałeś rozmawiają na głosowym {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_image(url="https://i.postimg.cc/ZR7B1jTh/emilia-talking.gif")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

						if select.values[0] == "10":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 5

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za co miesięczne aktywność na kanałach tekstowych {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

						if select.values[0] == "11":
							await open_profile(member)
							user = member
							users = await get_profile_date()
							point = 7

							if Role.uczestnicy_plus_m(member) in member.roles:
								point = point + 2
							if Role.server_booster_m(member) in member.roles:
								point = point * 2

							users[str(user.id)]["wallet"] += point

							with open("userprofile.json","w") as f:
								json.dump(users,f)
							
							await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

							embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"Za co miesięczne aktywność na kanałach głosowych {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
							embed.set_thumbnail(url=f"{member.avatar}")
							embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
							await point_channel.send(embed=embed)

				view = MySelectView()
				await interaction.response.send_message(view=view, ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "give_extra", description= "Dzięki tej komendzie właściciel serwera przyznaje dodatkowe punkty uczestnikom serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member, point: int, text: str):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				guild = client.get_guild(698522294414344232)
				point_channel = guild.get_channel(925191790284406805)
				await open_profile(member)
				user = member
				users = await get_profile_date()

				users[str(user.id)]["wallet"] += point

				with open("userprofile.json","w") as f:
					json.dump(users,f)
				
				await interaction.response.edit_message(content=f"Pomyślnie przyznano punkty {member.mention}",embed=None,view=None)

				embed=discord.Embed(title="Przyznano Otimi-coin: <:D2_arrowup:972095071115689985>",description=f"{text} {member.mention} otrzymujesz:\n :coin: {point} Otimi-coinów." , color=0x56e455)
				embed.set_thumbnail(url=f"{member.avatar}")
				embed.set_image(url="https://i.postimg.cc/hvjMMnXw/woww-wow.gif")
				embed.set_footer(text=f"Punkty przyznał {interaction.user.name}.")
				await point_channel.send(embed=embed)


			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "profile_edit_footer", description= "Po wykupieniu tego w sklepie, będziesz w stanie edytować stopkę swojego profilu.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, footer: str):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag4 = usersf[str(userf.id)]["flag4"]
			if flag4 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()
					users[str(user.id)]["footer"] = footer

					with open("userprofile.json","w") as f:
						json.dump(users,f)

					await interaction.response.send_message("Pomyślnie zaktualizowano stopkę profilu.", ephemeral = True)
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

			else:
				await interaction.response.send_message(f"Jeszcze nye masz odblokowanej tej komendy {interaction.user.mention} żeby ją odblokować udaj się do sklepu '/shop'", ephemeral = True)

		@tree.command(name = "profile_edit_text", description= "Po wykupieniu tego w sklepie, będziesz w stanie edytować sekcję pisemną swojego profilu.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, title: str, text: str):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag5 = usersf[str(userf.id)]["flag5"]
			if flag5 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()
					users[str(user.id)]["text"] = text
					users[str(user.id)]["nav"] = title

					with open("userprofile.json","w") as f:
						json.dump(users,f)

					await interaction.response.send_message("Pomyślnie zaktualizowano sekcję pisemną profilu.", ephemeral = True)
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Jeszcze nye masz odblokowanej tej komendy {interaction.user.mention} żeby ją odblokować udaj się do sklepu '/shop'", ephemeral = True)

		@tree.command(name = "profile_edit_banner", description= "Po wykupieniu tego w sklepie, będziesz w stanie edytować banner swojego profilu.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, banner: str):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag8 = usersf[str(userf.id)]["flag8"]
			if flag8 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()
					users[str(user.id)]["banner"] = banner

					with open("userprofile.json","w") as f:
						json.dump(users,f)

					await interaction.response.send_message("Pomyślnie zaktualizowano banner profilu.", ephemeral = True)
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

			else:
				await interaction.response.send_message(f"Jeszcze nye masz odblokowanej tej komendy {interaction.user.mention} żeby ją odblokować udaj się do sklepu '/shop'", ephemeral = True)

		@tree.command(name = "profile_edit_icon", description= "Po wykupieniu tego w sklepie, będziesz w stanie dodać ikonkę do swojego profilu.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, icon: str):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag9 = usersf[str(userf.id)]["flag9"]
			if flag9 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()
					users[str(user.id)]["emoji"] = icon

					with open("userprofile.json","w") as f:
						json.dump(users,f)

					await interaction.response.send_message("Pomyślnie zaktualizowano ikonę profilu.", ephemeral = True)
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Jeszcze nye masz odblokowanej tej komendy {interaction.user.mention} żeby ją odblokować udaj się do sklepu '/shop'", ephemeral = True)

		@tree.command(name = "profile_edit_color", description= "Po wykupieniu tego w sklepie, będziesz w stanie ustalić kolorek swojego profilu.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, hex: str):
			await open_flag_profile(interaction.user)
			userf = interaction.user
			usersf = await get_profile_flag_date()
			flag10 = usersf[str(userf.id)]["flag10"]
			if flag10 == 1:
				mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
				channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
				tchannel = discord.utils.get(interaction.guild.channels, id = 1113788688011366481)
				if interaction.channel == channel or interaction.channel == mchannel or interaction.channel == tchannel:
					await open_profile(interaction.user)
					user = interaction.user
					users = await get_profile_date()
					users[str(user.id)]["color"] = hex

					with open("userprofile.json","w") as f:
						json.dump(users,f)

					await interaction.response.send_message("Pomyślnie zaktualizowano kolor profilu.", ephemeral = True)
				else:
					await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Jeszcze nye masz odblokowanej tej komendy {interaction.user.mention} żeby ją odblokować udaj się do sklepu '/shop'", ephemeral = True)

		@tree.command(name = "shop", description= "Otwiera sklep w którym możesz wydać swoje Otimi-coiny.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			lev1 = ["https://i.postimg.cc/Kj7HXgfT/L1-1.webp","https://i.postimg.cc/Dztj8cYs/L1-2.jpg","https://i.postimg.cc/3xHFN8WF/L1-3.jpg"]
			lev2 = ["https://i.postimg.cc/kGPphyQ9/L2-1.jpg","https://i.postimg.cc/pd9cWSkR/L2-2.jpg","https://i.postimg.cc/Kv3DYJBn/L2-3.jpg","https://i.postimg.cc/1tyvnwsy/L2-4.jpg","https://i.postimg.cc/g2RsgN0Y/L2-5.jpg","https://i.postimg.cc/FK5Wvw6d/L2-6.jpg","https://i.postimg.cc/5NzmfY9t/L2-7.jpg","https://i.postimg.cc/RZQQnkH5/L2-8.jpg","https://i.postimg.cc/MZvDr3hV/L2-9.jpg","https://i.postimg.cc/G3VQ0JCN/L2-10.jpg"]
			lev3 = ["https://i.postimg.cc/mrYdg8xd/L3-1.jpg","https://i.postimg.cc/T3NHXxVt/L3-2.jpg","https://i.postimg.cc/nLGkJr7g/L3-3.png","https://i.postimg.cc/JnKPb0zZ/L3-4.png","https://i.postimg.cc/PrC2wtsv/L3-5.jpg","https://i.postimg.cc/zXjc0KVZ/L3-6.jpg"]
			rozmowa = ["https://i.postimg.cc/GmHG7hKv/a1.jpg","https://i.postimg.cc/Jz2cMB0T/a2.jpg","https://i.postimg.cc/P5xzgMXp/a3.jpg","https://i.postimg.cc/pXVDjBnG/a4.jpg","https://i.postimg.cc/GhMvxsFc/a5.jpg","https://i.postimg.cc/3RMXD5gm/a6.webp","https://i.postimg.cc/3RMXD5gm/a6.webp","https://i.postimg.cc/sxm78Mb4/a7.jpg","https://i.postimg.cc/ZRrr87cg/a8.jpg","https://i.postimg.cc/SRkcD61K/a9.jpg","https://i.postimg.cc/tRN37c7n/a10.webp","https://i.postimg.cc/SRYb19nw/b1.jpg","https://i.postimg.cc/nhJM7F5H/b2.jpg","https://i.postimg.cc/mD5GSjgY/b3.jpg","https://i.postimg.cc/5tpJXbck/b4.jpg","https://i.postimg.cc/PxxjZ9Tf/b5.jpg","https://i.postimg.cc/ht1v0FWV/b6.jpg","https://i.postimg.cc/nVXsfwBt/b7.jpg","https://i.postimg.cc/66F8WLf4/b8.jpg","https://i.postimg.cc/6TsJkQRT/b9.jpg","https://i.postimg.cc/vmGM8DKV/b10.jpg"]
			guild = client.get_guild(698522294414344232)
			# point_channel = guild.get_channel(925191790284406805) poprawny
			point_channel = guild.get_channel(1113788688011366481)
			uczestnicy_plus = discord.utils.get(interaction.guild.roles, id=920081493110423592)
			plus = discord.utils.get(interaction.guild.roles, id=1124025539540295840)

			class MySelectRozmowa3(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								discord.SelectOption(
									label="Opowiedz mi coś o sobie.",
									description="Suwi-Chan wytłumaczy ci jak działa jej sklep.",
									value="1",
									emoji="<a:C33_happy:1099070182472831068>",
								),

								discord.SelectOption(
									label="Czemu nasza waluta nazywa się Otimi-coiny ?",
									description="Suwi-Chan wytłumaczy ci pochodzenie nazwy Otimi.",
									value="2",
									emoji="<:C17_money:979762269263126558>",
								),

								discord.SelectOption(
									label="Czy będziesz miała więcej asortymentu ?",
									description="Suwi-Chan wytłumaczy ci czy będzie więcej asortymentu.",
									value="3",
									emoji="<:0A9_PadoruMegumin:1098737265594880010>",
								),

								discord.SelectOption(
									label="Przyłącz się do oglądania.",
									description="Pozwala ci po patrzeć na zmieniające się niebo.",
									value="4",
									emoji="☁️",
								),

								discord.SelectOption(
									label="Zakończ rozmowę.",
									description="Przenosi się do asortymentu Suwi-chan.",
									value="5",
									emoji="❌",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							embed = discord.Embed(title="Suwi-Chan:", description="No dobrze, teraz nie mam wyjścia muszę uchylić skrawek informacji o mnie.\nO właśnie skosztuj herbatki jaką ci przygotowałam, mam nadzije że będzie ci smakować i przyjemniej się rozmawia przy filiżance herbaty.", color=0xfceade)
							embed.add_field(name="o mnie:", value=f"Mam na imię Suwi jestem czwartym konceptem postaci, i nie nie pomyliłam się czwartym mogą cię to zaskoczyć ale jest jeszcze jedna postać która się wam nie ukazała i nie będzie wam dane jej zobaczyć do puki nie powstanie jakaś gra w naszym uniwersum ponieważ ta postać będzie głównym antagonisto. Ale wróćmy do mnie jestem sklepikarką u mnie zawszę można zaopatrzeć się w wszelaki bajery.", inline=False)
							embed.add_field(name="Co z uniwersum:", value=f"Tu jest jeden znaczący problem brakuje w naszych szeregach grafika/graficzki bez tego ciężko jest cokolwiek zrobić mam wielką nadziej że uda mi się znaleźć tako osobę, dlatego wierzę że uda się nam wszystkim wyczekać do tego momentu.", inline=False)
							embed.add_field(name="", value=f"I tak tak wiem że moje tłumaczenie jest całkiem chaotyczne ale uważam że pomimo tego zostałam zrozumiana może nie w najlepszy sposób ale szczery, i chce wierzyć że rozmowa choć trochę ci się podobała.", inline=False)
							embed.set_image(url=f"https://i.postimg.cc/9QQNS074/anime-caf-aesthetic-coffee.gif")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa3())

						if select.values[0] == "2":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Wyglądało to mniej wiecej tak <:0A40_hello:921529355862171729>.", color=0xbef0fe)
							embed.set_image(url=f"https://i.postimg.cc/KvqrMP3Y/Zrzut-ekranu-2023-06-30-180333.jpg")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa3())

						if select.values[0] == "3":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Oczywiście że będzie więcej ale nie wiem kiedy do kładnie jak będę wiedzieć lub coś planować to dam wam znać <a:C31_love:1099070353680126062>.", color=0xbef0fe)
							embed.set_image(url=f"https://i.postimg.cc/Xvfmk1bW/wink-heart.gif")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa3())

						if select.values[0] == "4":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Patrzycie razem w niebo.", color=0xbef0fe)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa3())
						
						if select.values[0] == "5":
							await interaction.response.edit_message(embed=None,view=MySelectShop3())

			class MySelectRozmowa2(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								discord.SelectOption(
									label="Opowiedz mi coś o sobie.",
									description="Suwi-Chan opowie ci coś o sobie ?",
									value="1",
									emoji="<a:C33_happy:1099070182472831068>",
								),

								discord.SelectOption(
									label="Przyłącz się do oglądania.",
									description="Pozwala ci po patrzeć na zmieniające się niebo.",
									value="2",
									emoji="☁️",
								),

								discord.SelectOption(
									label="Zakończ rozmowę.",
									description="Przenosi się do asortymentu Suwi-chan.",
									value="3",
									emoji="❌",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							embed = discord.Embed(title="Suwi-Chan:", description="Opowiem dalej o sobie, jak dotrzesz do dalszych sklepów z wyższym poziomem, jeszcze nie jestem co do ciebie przekonana, a w ten sposób się trochę lepiej poznamy.", color=0xfceade)
							embed.set_image(url=f"{random.choice(lev2)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa2())
						
						if select.values[0] == "2":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Patrzycie razem w niebo.", color=0xbef0fe)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa2())
						
						if select.values[0] == "3":
							await interaction.response.edit_message(embed=None,view=MySelectShop2())

			class MySelectRozmowa(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								discord.SelectOption(
									label="Opowiedz mi o sklepie.",
									description="Suwi-Chan wytłumaczy ci jak działa jej sklep.",
									value="1",
									emoji="🛒",
								),

								discord.SelectOption(
									label="Przyłącz się do oglądania.",
									description="Pozwala ci po patrzeć na zmieniające się niebo.",
									value="2",
									emoji="☁️",
								),

								discord.SelectOption(
									label="Zakończ rozmowę.",
									description="Przenosi się do asortymentu Suwi-chan.",
									value="3",
									emoji="❌",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							embed = discord.Embed(title="Suwi-Chan:", description="", color=0xfceade)
							embed.add_field(name="Sklep:", value=f"Oczywiście, dobrze więc.\nNumerek obok zielonej strzałki :D2_arrowup: oznacza poziom sklepu w którym jesteś, aby go zwiększyć musisz zwiększyć poziom swojego profilu, a wykonasz to wykupując u mnie opcje level 2.", inline=False)
							embed.add_field(name="Asortyment:", value=f"Czerwony 'X' ❌ oznacza, że nie posiadasz wymienionego przywileja, a zielony '✓' ✅ że już go odblokowałeś.", inline=False)
							embed.add_field(name="Czemu ty prowadzisz sklepy ?", value=f"Ponieważ Otaki-chan dzielnie pracuje, a jej siostra, Mani-chan, testuje nowe pomysły.\nWieć sklepiki są moje, mam nadzieje że też mnie polubisz w jakiś sposób.", inline=False)
							embed.add_field(name="Czy jeszcze porozmawiamy ?", value=f"Tak, jeśli odwiedzisz moje sklepy z wyższym poziomem.", inline=False)
							embed.set_image(url=f"{random.choice(lev1)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa())

						if select.values[0] == "2":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Patrzycie razem w niebo.", color=0xbef0fe)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa())
						
						if select.values[0] == "3":
							await interaction.response.edit_message(embed=None,view=MySelectShop())

			class MySelectLevel3(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								# discord.SelectOption(
								# 	label="Przejdź do następnego sklepu",
								# 	description="Pozwala ci przejść do sklepu dwupoziomowego.",
								# 	value="1",
								# 	emoji="<:D2_arrowup:972095071115689985>",
								# ),

								discord.SelectOption(
									label="Przejdź do poprzedniego sklepu",
									description="Pozwala ci przejść do sklepu jednopoziomowego.",
									value="2",
									emoji="<:D3_arrowdown:972095071090507816>",
								),

								discord.SelectOption(
									label="Rozmowa",
									description="Pozwala ci chwilkę zemną porozmawiać.",
									value="3",
									emoji="💬",
								),

								discord.SelectOption(
									label="288 | Plus",
									description="To rola która jest ulepszeniem roli uczestników+.",
									value="4",
									emoji="<:D1_plus1:981257475078639676>",
								),

								discord.SelectOption(
									label="1 | Odznaka profilowicza",
									description="Odblokowuję odznakę za wykupienie wszystkich dodatków do profilu.",
									value="5",
									emoji="<:0A17_wow:1063241073121562634>",
								),

								discord.SelectOption(
									label="100 | Aplikacja na moderatora",
									description="Odblokowuję odznakę która pozwala ci na aplikowanie na moderatora.",
									value="6",
									emoji="📝",
								),

							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						# if select.values[0] == "1":
						# 	embed = discord.Embed(title="Suwi-Chan:", description="Rozwinięcie 3 sklepu wraz z 4 dojdzie w przyszłych aktualizacjach <:B6_OhMahGah:1098739422578618468>.", color=0xfceade)
						# 	await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop3())

						if select.values[0] == "2":
							await interaction.response.edit_message(content=None,embed=None,view=MySelectShop3())
						
						if select.values[0] == "3":
							embed = discord.Embed(title="Suwi-Chan:", description="Nie mogłam się doczekać by muc z tobą porozmawiać.", color=0xfceade)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(content=None,embed=embed,view=MySelectRozmowa3())

						if select.values[0] == "4":
							if Role.plus(interaction) in interaction.user.roles:
								await interaction.response.edit_message(content=f"{interaction.user.mention} Posiadasz już role {plus.mention}",view=MySelectLevel3())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 288
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 288 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)
									
									await interaction.user.add_roles(plus)
									embed=discord.Embed(title=f"Wspaniale !",description=f"{interaction.user.mention} rola została ci przyznana, w sklepie już zaznaczam że ją masz." , color=0x52dd9d)
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop3())
									embed=discord.Embed(title="Gratulacje !",description=f"{interaction.user.mention} właśnie otrzymał rolę {plus.mention}\n\nKtóra jest ulepszeniem roli {uczestnicy_plus.mention}" , color=0x52dd9d)
									embed.set_thumbnail(url=f"{interaction.user.avatar}")
									embed.set_image(url="https://i.postimg.cc/1RwBHJcT/stella-vermillion-power.gif")
									await point_channel.send(embed=embed)

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel3())

						if select.values[0] == "5":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag11 = usersf[str(userf.id)]["flag11"]
							flag10 = usersf[str(userf.id)]["flag10"]
							flag9 = usersf[str(userf.id)]["flag9"]
							flag8 = usersf[str(userf.id)]["flag8"]
							flag5 = usersf[str(userf.id)]["flag5"]
							flag4 = usersf[str(userf.id)]["flag4"]
							if flag11 == 1:
								await interaction.response.edit_message(content="Posiadasz już tą odznakę.",embed=None,view=MySelectShop3())
							else:
								if flag10 == 1 and flag9 == 1 and flag8 == 1 and flag5 == 1 and flag4 ==1:
									await open_profile(interaction.user)
									user = interaction.user
									users = await get_profile_date()
									cost = 1
									wallet = users[str(user.id)]["wallet"]
									if wallet >= 1 :
										users[str(user.id)]["wallet"] = wallet - cost
										with open("userprofile.json","w") as f:
											json.dump(users,f)


										usersf[str(userf.id)]["flag11"] = 1
										with open("userflag.json","w") as f:
											json.dump(usersf,f)
										
										await interaction.user.add_roles(plus)
										embed=discord.Embed(title=f"Wspaniale !",description=f"{interaction.user.mention} odznaka została ci przyznana, w sklepie już zaznaczam że ją masz." , color=0x56e455)
										await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop3())
										embed=discord.Embed(title="Gratulacje !",description=f"{interaction.user.mention} właśnie wykupił odznakę profilowicza\n\nKtóra jest potwierdzeniem zdobycia wszystkich ulepszeń do profilu" , color=0x56e455)
										embed.set_thumbnail(url=f"{interaction.user.avatar}")
										embed.set_image(url="https://i.postimg.cc/HWZ6nrKC/anime-shopping.gif")
										await point_channel.send(embed=embed)
									else:
										await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel3())

								else:
									await interaction.response.edit_message(content="Żeby kupić tą odznakę musisz posiadać wsztkie ulepszenia profilu.",embed=None,view=MySelectShop3())

						if select.values[0] == "6":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag12 = usersf[str(userf.id)]["flag12"]
							if flag12 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz możesz wysyłać swoją aplikację na moderatora.", color=0xfceade)
								embed.add_field(name="Jak ona będzie wyglądać:", value=f"Kiedy będziesz chciał spróbować swoich wpisz komendę /report podaj tytuł np: 'Aplikacja na moderatora' i w treści czemu uważasz że byś się nadawał.", inline=False)
								embed.add_field(name="FAQ", value=f"* Czy gwarantuje mi to zostanie moderatorem ?\n  - Nie\n\n* Czy będę mógł wysłać swoje podanie ponownie ?\n - Tak oczywiście tylko od poprzedniego odrzucenia odczekaj około miesiąc\n\n* Czy mogłem złożyć aplikacje na moderatora przed kupieniem odznaki ?\n - Tak ale została by odrzucona od razu i nie mógłbyś zostać moderatorem nawet po zdobyciu odznaki.\n\n* Kiedy mam największe szanse na zostanie moderatorem ?\n - Wraz z ustaleniami nowi moderatorzy będą pojawiać się wraz z zwiększeniem co około 100 osób na serwerze.\n - Więc największą szansę na zostanie będziesz mieć gdy ilość uczestników będzie dobijać do kolejnej setki.\n", inline=False)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/zDTCJcVj/yui-hirasawa-kon.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop3())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 100
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 100 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag12"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz możesz wysyłać swoją aplikację na moderatora.", color=0xfceade)
									embed.add_field(name="Jak ona będzie wyglądać:", value=f"Kiedy będziesz chciał spróbować swoich wpisz komendę /report podaj tytuł np: 'Aplikacja na moderatora' i w treści czemu uważasz że byś się nadawał.", inline=False)
									embed.add_field(name="FAQ", value=f"* Czy gwarantuje mi to zostanie moderatorem ?\n  - Nie\n\n* Czy będę mógł wysłać swoje podanie ponownie ?\n - Tak oczywiście tylko od poprzedniego odrzucenia odczekaj około miesiąc\n\n* Czy mogłem złożyć aplikacje na moderatora przed kupieniem odznaki ?\n - Tak ale została by odrzucona od razu i nie mógłbyś zostać moderatorem nawet po zdobyciu odznaki.\n\n* Kiedy mam największe szanse na zostanie moderatorem ?\n - Wraz z ustaleniami nowi moderatorzy będą pojawiać się wraz z zwiększeniem co około 100 osób na serwerze.\n - Więc największą szansę na zostanie będziesz mieć gdy ilość uczestników będzie dobijać do kolejnej setki.\n", inline=False)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/zDTCJcVj/yui-hirasawa-kon.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(embed=embed,view=MySelectShop3())
								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

			class MySelectLevel2(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								discord.SelectOption(
									label="Przejdź do następnego sklepu",
									description="Pozwala ci przejść do sklepu dwupoziomowego.",
									value="1",
									emoji="<:D2_arrowup:972095071115689985>",
								),

								discord.SelectOption(
									label="Przejdź do poprzedniego sklepu",
									description="Pozwala ci przejść do sklepu jednopoziomowego.",
									value="2",
									emoji="<:D3_arrowdown:972095071090507816>",
								),

								discord.SelectOption(
									label="Rozmowa",
									description="Pozwala ci chwilkę zemną porozmawiać.",
									value="3",
									emoji="💬",
								),

								discord.SelectOption(
									label="7 | Kolorek profilu",
									description="Odblokowuję komendę /profile_edit_color gdzie możesz ustalić kolor twojego profilu.",
									value="4",
									emoji="🎨",
								),

								discord.SelectOption(
									label="3 | Ikona profilu",
									description="Odblokowuję komendę /profile_edit_icon gdzie możesz dodać swoją własną ikonkę profilu.",
									value="5",
									emoji="💠",
								),

								discord.SelectOption(
									label="10 | Banner profilu",
									description="Odblokowuję komendę /profile_edit_banner gdzie możesz dodać swoją własny banner profilu.",
									value="6",
									emoji="🖼️",
								),

								discord.SelectOption(
									label="5 | Porada",
									description="Porada jak wpłacać, wypłacać wszystko.",
									value="7",
									emoji="<:A29_triggered:921394505192734751>",
								),

								discord.SelectOption(
									label="18 | Przelewy",
									description="Odblokowuję komendy /bank_transfer oraz /instantbank_transfer",
									value="8",
									emoji="💸",
								),

								discord.SelectOption(
									label="36 | Level up",
									description="Awansuje twój profil z 2 poziomu na 3.",
									value="9",
									emoji="<:D2_arrowup:972095071115689985>",
								),

							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							level = users[str(user.id)]["level"]
							if level >= 3:
								await interaction.response.edit_message(content=None,embed=None,view=MySelectShop3())
							else:
								await interaction.response.edit_message(content=f"{interaction.user.mention} żeby udać się do wyższo poziomowych sklepów musisz zwiększy swój poziom profilu.",view=MySelectLevel2())

						if select.values[0] == "2":
							await interaction.response.edit_message(content=None,embed=None,view=MySelectShop())
						
						if select.values[0] == "3":
							embed = discord.Embed(title="Suwi-Chan:", description="Uszczęśliwia mnie to że chcesz zemną znowu porozmawiać.\nChciałbyś się przyłączyć do oglądania ze mną nieba?\nByłabym bardzo wdzięczna.", color=0xfceade)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(content=None,embed=embed,view=MySelectRozmowa2())

						if select.values[0] == "4":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag10 = usersf[str(userf.id)]["flag10"]
							if flag10 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Możesz teraz używać komendy /profile_edit_color, która pozwala ci ustawić, bądź zmienić, kolorek swojego profilu.\n\nPodawaj kolorek w zapisie hexowym np: #7BAFD4, #9D37E6", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_thumbnail(url="https://i.postimg.cc/dDcc4S59/spray-paint.gif")
								await interaction.response.edit_message(embed=embed,view=MySelectShop2())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 7
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 7 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag10"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Możesz teraz używać komendy /profile_edit_color, która pozwala ci ustawić, bądź zmienić, kolorek swojego profilu.\n\nPodawaj kolorek w zapisie hexowym np: #7BAFD4, #9D37E6", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_thumbnail(url="https://i.postimg.cc/dDcc4S59/spray-paint.gif")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())
								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

						if select.values[0] == "5":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag9 = usersf[str(userf.id)]["flag9"]
							if flag9 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Możesz teraz używać komendy /profile_edit_icon, która umożliwia ustawić ikonkę (emotkę przy tytule) swojego profilu.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/vZMcmPG9/fio-piccolo-porco-rosso.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop2())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 3
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 3 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag9"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Możesz teraz używać komendy /profile_edit_icon, która umożliwia ustawić ikonkę (emotkę przy tytule) swojego profilu.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/vZMcmPG9/fio-piccolo-porco-rosso.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())
								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

						if select.values[0] == "6":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag8 = usersf[str(userf.id)]["flag8"]
							if flag8 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną komendę /profile_edit_banner która pozwala ci dodać banner do twojego profilu.", color=0xfceade)
								embed.add_field(name="Jak korzystać:", value=f"Aby wstawić banner w opisie należy wpisać komendę, a następnie wkleić **bezpośredni link** do obrazka/gifa którego chcesz użyć.\n Pamiętaj aby najpierw umieść go na jednych ze stron od przechowywania zdjęć/gifów np: [postimg](https://postimages.org/) lub [imgur](https://imgur.com/).", inline=False)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/dQk7NkW7/coloring-draw.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop2())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 10
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 10 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag8"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną komendę /profile_edit_banner która pozwala ci dodać banner do twojego profilu.", color=0xfceade)
									embed.add_field(name="Jak korzystać:", value=f"Aby wstawić banner w opisie należy wpisać komendę, a następnie wkleić **bezpośredni link** do obrazka/gifa którego chcesz użyć.\n Pamiętaj aby najpierw umieść go na jednych ze stron od przechowywania zdjęć/gifów np: [postimg](https://postimages.org/) lub [imgur](https://imgur.com/).", inline=False)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/dQk7NkW7/coloring-draw.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())
								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

						if select.values[0] == "7":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag6 = usersf[str(userf.id)]["flag6"]
							if flag6 == 1:
								embed = discord.Embed(title="Porady Suwi-Chan:", description=f"Żeby wypłacać i wpłacać wszystkie Otimi-coiny zamiast konkretnej ilości, wpisz trzy zera (000).\nZapamiętaj że w przypadku /instantbank_transfer, bank nie przesyła tyle ile mógłbyś wysyłać coinów.\nW tym oto transferze nie wysyła nic i pobiera też prowizje.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać poradę ponownie klikając ją w moim sklepiku. Spokojnie, opłata jest jednorazowa.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/R08FShHr/hi-hello.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop2())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 5
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 5 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag6"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Porady Suwi-Chan:", description=f"Żeby wypłacać i wpłacać wszystkie Otimi-coiny zamiast konkretnej ilości, wpisz trzy zera (000).\nZapamiętaj że w przypadku /instantbank_transfer, bank nie przesyła tyle ile mógłbyś wysyłać coinów.\nW tym oto transferze nie wysyła nic i pobiera też prowizje.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać poradę ponownie klikając ją w moim sklepiku. Spokojnie, opłata jest jednorazowa.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/R08FShHr/hi-hello.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

						if select.values[0] == "8":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag7 = usersf[str(userf.id)]["flag7"]
							if flag7 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowane przelewy!\nKomenda /bank_transfer pozwala ci raz na 24 godziny przesłać komuś Otimi-coiny z banku, natomiast /instantbank_transfer nie ma ograniczeń czasowych ale za to ma prowizje 5 Otimi-coinów.\n\nMiłych przelewów.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/cLFCzX1L/yuzuki-mizusaka-nonoka-komiya.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop2())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 18
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 18 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag7"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowane przelewy!\nKomenda /bank_transfer pozwala ci raz na 24 godziny przesłać komuś Otimi-coiny z banku, natomiast /instantbank_transfer nie ma ograniczeń czasowych ale za to ma prowizje 5 Otimi-coinów.\n\nMiłych przelewów.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/cLFCzX1L/yuzuki-mizusaka-nonoka-komiya.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())
								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel2())

						if select.values[0] == "9":
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							level = users[str(user.id)]["level"]
							wallet = users[str(user.id)]["wallet"]
							if level == 3:
								await interaction.response.edit_message(content=f"{interaction.user.mention} dokonałeś już ulepszenia.",view=MySelectLevel2())
							else:
								if wallet >= 36:
									cost = 36
									users[str(user.id)]["wallet"] = wallet - cost
									users[str(user.id)]["level"] = 3
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									embed=discord.Embed(title=f"Wspaniale !",description=f"{interaction.user.mention} awans został ci przyznany, w sklepie już zaznaczam że go zdobyłeś." , color=0xefa4b2)
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop2())
									embed=discord.Embed(title="Gratulacje !",description=f"{interaction.user.mention} właśnie awansował na poziom 3" , color=0xefa4b2)
									embed.set_thumbnail(url=f"{interaction.user.avatar}")
									embed.set_image(url="https://i.postimg.cc/m23TpXXv/akko-level-up.gif")
									await point_channel.send(embed=embed)

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

			class MySelectLevel1(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[

								discord.SelectOption(
									label="Przejdź do następnego sklepu",
									description="Pozwala ci przejść do sklepu dwupoziomowego.",
									value="1",
									emoji="<:D2_arrowup:972095071115689985>",
								),

								discord.SelectOption(
									label="Rozmowa.",
									description="Pozwala ci chwilkę zemną porozmawiać.",
									value="2",
									emoji="💬",
								),

								discord.SelectOption(
									label="28 | Uczestnicy+",
									description="To rola która otwiera nam dostęp do reszty serwera.",
									value="3",
									emoji="💎",
								),

								discord.SelectOption(
									label="3 | Sekcja pisemna profilu",
									description="Odblokowuję komendę /profile_edit_text gdzie możesz dodać swój własny tekst do profilu.",
									value="4",
									emoji="📝",
								),

								discord.SelectOption(
									label="2 | Sekcja stopki profilu",
									description="Odblokowuję komendę /profile_edit_foot gdzie możesz dodać swoją własną stopkę na profilu.",
									value="5",
									emoji="📃",
								),

								discord.SelectOption(
									label="1 | Kwiatek Idei",
									description="Wiedza o tym czym jest odznaka kwiatka Idei.",
									value="6",
									emoji="💮",
								),

								discord.SelectOption(
									label="1 | Reporter",
									description="Wiedza o tym czym jest odznaka reportera.",
									value="7",
									emoji="<:A11_report:921400267440791662>",
								),

								discord.SelectOption(
									label="5 | Porada",
									description="Porada jak mieć więcej Otimi-coinów.",
									value="8",
									emoji="<:A29_triggered:921394505192734751>",
								),

								discord.SelectOption(
									label="12 | Level up",
									description="Awansuje twój profil z 1 poziomu na 2.",
									value="9",
									emoji="<:D2_arrowup:972095071115689985>",
								),

							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							level = users[str(user.id)]["level"]
							if level >= 2:
								await interaction.response.edit_message(content=None,embed=None,view=MySelectShop2())
							else:
								await interaction.response.edit_message(content=f"{interaction.user.mention} żeby udać się do wyższo poziomowych sklepów musisz zwiększy swój poziom profilu.",view=MySelectLevel1())

						if select.values[0] == "2":
							embed = discord.Embed(title="Suwi-Chan:", description=f"Dobrze, porozmawiajmy na wybrany przez ciebie temat, a ja postaram się go podtrzymać.", color=0xfceade)
							embed.add_field(name="", value=f"Lubię rozmawiać patrząc się w niebo i to jak ono nieustanie zmienia się...", inline=True)
							embed.set_image(url=f"{random.choice(rozmowa)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectRozmowa())
						
						if select.values[0] == "3":
							if Role.uczestnicy_plus(interaction) in interaction.user.roles:
								await interaction.response.edit_message(content=f"{interaction.user.mention} Posiadasz już role {uczestnicy_plus.mention}",view=MySelectLevel1())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 28
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 28 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)
									
									await interaction.user.add_roles(uczestnicy_plus)
									embed=discord.Embed(title=f"Wspaniale !",description=f"{interaction.user.mention} rola została ci przyznana, w sklepie już zaznaczam że ją masz." , color=0xbef0fe)
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())
									embed=discord.Embed(title="Gratulacje !",description=f"{interaction.user.mention} właśnie otrzymał rolę {uczestnicy_plus.mention}" , color=0xbef0fe)
									embed.set_thumbnail(url=f"{interaction.user.avatar}")
									embed.set_image(url="https://i.postimg.cc/j2bq6Xc3/bakugan-power-up.gif")
									await point_channel.send(embed=embed)

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

						if select.values[0] == "4":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag5 = usersf[str(userf.id)]["flag5"]
							if flag5 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną sekcję pisemną profilu! \n Żeby ją dodać wpisz komendę /profile_edit_text.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/rsrLGLNm/drawing-sketching.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								cost = 3
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 3 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag5"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną sekcję pisemną profilu! \n Żeby ją dodać wpisz komendę /profile_edit_text.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/rsrLGLNm/drawing-sketching.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())

						if select.values[0] == "5":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag4 = usersf[str(userf.id)]["flag4"]
							if flag4 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną stopkę profilu! \n Żeby ją dodać wpisz komendę /profile_edit_footer.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/gk3xm9bm/art-drawing.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 2
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 2 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag4"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Od teraz masz odblokowaną stopkę profilu! \n Żeby ją dodać wpisz komendę /profile_edit_footer.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać tą informacje ponownie klikając ją w moim sklepiku, nie pobiorę coinów ponownie za tą wiadomość.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/gk3xm9bm/art-drawing.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

						if select.values[0] == "6":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag3 = usersf[str(userf.id)]["flag3"]
							if flag3 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Kwiatek idei jest odznaką przyznawaną uczestnikom którzy realizują główne założenia serwera.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać czym jest kwiatek idei ponownie klikając go w moim sklepiku.\nSpokojnie, za taką prostotę nie muszę pobierać ponownie coinów.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/wxQ3f5N3/anime-flowers.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 1
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 1 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag3"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Kwiatek idei jest odznaką przyznawaną uczestnikom którzy realizują główne założenia serwera.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać czym jest kwiatek idei ponownie klikając go w moim sklepiku.\nSpokojnie, za taką prostotę nie muszę pobierać ponownie coinów.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/wxQ3f5N3/anime-flowers.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

						if select.values[0] == "7":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag2 = usersf[str(userf.id)]["flag2"]
							if flag2 == 1:
								embed = discord.Embed(title="Suwi-Chan:", description=f"Odznaka reportera jest przyznawana uczestnikom którzy znajdują błędy w działaniu systemów serwerowych lub Otaki-chan.", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać kim jest reporter ponownie klikając na to w moim sklepiku.\nSpokojnie, za taką drobnostkę nie muszę pobierać ponownie coinów.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/L47nPQBK/mass-media-duo-mass-media-girls.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 1
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 1 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag2"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Suwi-Chan:", description=f"Odznaka reportera jest przyznawana uczestnikom którzy znajdują błędy w działaniu systemów serwerowych lub Otaki-chan.", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać kim jest reporter ponownie klikając na to w moim sklepiku.\nSpokojnie, za taką drobnostkę nie muszę pobierać ponownie coinów.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/L47nPQBK/mass-media-duo-mass-media-girls.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

						if select.values[0] == "8":
							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							flag1 = usersf[str(userf.id)]["flag1"]
							if flag1 == 1:
								embed = discord.Embed(title="Porady Suwi-Chan:", description=f"Żeby posiadać większą ilość Otimi-coinów kup na początku rangę Uczestnicy+ dzięki której będziesz otrzymywać dodatkowe 2 coiny za każdą aktywność, możesz też rozważyć wsparcie serwera które zapewni ci to mnożnik x2 do każdej aktywności. \n\n Zalecam zdobycie obydwu dodatkowych roli, a szczególnie roli server booster.\n\n A teraz ruszaj zdobywać Otimi-coiny !", color=0xfceade)
								embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać poradę ponownie klikając ją w moim sklepiku. Spokojnie, opłata jest jednorazowa.", inline=False)
								embed.set_image(url=f"https://i.postimg.cc/6qMkKK1T/wemove-monday.gif")
								embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
								await interaction.response.edit_message(embed=embed,view=MySelectShop())
							else:
								await open_profile(interaction.user)
								user = interaction.user
								users = await get_profile_date()
								wallet = 0
								cost = 5
								wallet = users[str(user.id)]["wallet"]
								if wallet >= 5 :
									users[str(user.id)]["wallet"] = wallet - cost
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									await open_flag_profile(interaction.user)
									userf = interaction.user
									usersf = await get_profile_flag_date()

									usersf[str(userf.id)]["flag1"] = 1
									with open("userflag.json","w") as f:
										json.dump(usersf,f)

									embed = discord.Embed(title="Porady Suwi-Chan:", description=f"Żeby posiadać większą ilość Otimi-coinów kup na początku rangę Uczestnicy+ dzięki której będziesz otrzymywać dodatkowe 2 coiny za każdą aktywność, możesz też rozważyć wsparcie serwera które zapewni ci to mnożnik x2 do każdej aktywności. \n\n Zalecam zdobycie obydwu dodatkowych roli, a szczególnie roli server booster.\n\n A teraz ruszaj zdobywać Otimi-coiny!", color=0xfceade)
									embed.add_field(name="Pamiętaj:", value=f"Możesz przeczytać poradę ponownie klikając ją w moim sklepiku. Spokojnie, opłata jest jednorazowa.", inline=False)
									embed.set_image(url=f"https://i.postimg.cc/6qMkKK1T/wemove-monday.gif")
									embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())
			
						if select.values[0] == "9":
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							level = users[str(user.id)]["level"]
							wallet = users[str(user.id)]["wallet"]
							if level == 2:
								await interaction.response.edit_message(content=f"{interaction.user.mention} dokonałeś już ulepszenia.",view=MySelectLevel1())
							else:
								if wallet >= 12:
									cost = 12
									users[str(user.id)]["wallet"] = wallet - cost
									users[str(user.id)]["level"] = 2
									with open("userprofile.json","w") as f:
										json.dump(users,f)

									embed=discord.Embed(title=f"Wspaniale !",description=f"{interaction.user.mention} awans został ci przyznany, w sklepie już zaznaczam że go zdobyłeś." , color=0xfc4ac8)
									await interaction.response.edit_message(content=None,embed=embed,view=MySelectShop())
									embed=discord.Embed(title="Gratulacje !",description=f"{interaction.user.mention} właśnie awansował na poziom 2" , color=0xfc4ac8)
									embed.set_thumbnail(url=f"{interaction.user.avatar}")
									embed.set_image(url="https://i.postimg.cc/jq7xPdzd/anime-chibi.gif")
									await point_channel.send(embed=embed)

								else:
									await interaction.response.edit_message(content=f"{interaction.user.mention} nye masz wystarczająco coinów.",view=MySelectLevel1())

			class MySelectShop3(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[
								discord.SelectOption(
									label="Wejdź do sklepu 3 poziomowego.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="1",
									emoji="<:D2_arrowup:972095071115689985>",
								),

								discord.SelectOption(
									label="Wejdź do sklepu 2 poziomowego.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="2",
									emoji="<:D3_arrowdown:972095071090507816>",
								),

								discord.SelectOption(
									label="Wejdź do sklepu 1 poziomowego.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="3",
									emoji="<:D3_arrowdown:972095071090507816>",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							check_plus = "❌"
							check_odznaka = "❌"
							check_modoretaor = "❌"

							if Role.plus(interaction) in interaction.user.roles:
								check_plus = "✅"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag11 = usersf[str(userf.id)]["flag11"]
							flag12 = usersf[str(userf.id)]["flag12"]

							if flag11 == 1:
								check_odznaka = "✅"
							if flag12 == 1:
								check_modoretaor = "✅"

							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 2", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho, WoW udało ci się dotrzeć aż tutaj, nie mogę się doczekać aż z tobą porozmawiam i musisz mi wybaczyć za mój dość ograniczony asortyment w przyszłości dodam nowe produkty.", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_plus}", value=f"Rola plus", inline=True)
							embed.add_field(name=f"{check_odznaka}", value=f"Odznaka profilowicza", inline=True)
							embed.add_field(name=f"{check_modoretaor}", value=f"Aplikacja na moderatora", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev3)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel3())

						if select.values[0] == "2":
							check_color = "❌"
							check_icon = "❌"
							check_banner = "❌"
							check_tip = "❌"
							check_bank = "❌"
							check_level2 = "❌"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag6 = usersf[str(userf.id)]["flag6"]
							flag7 = usersf[str(userf.id)]["flag7"]
							flag8 = usersf[str(userf.id)]["flag8"]
							flag9 = usersf[str(userf.id)]["flag9"]
							flag10 = usersf[str(userf.id)]["flag10"]
							if flag6 == 1:
								check_tip = "✅"
							if flag7 == 1:
								check_bank = "✅"
							if flag8 == 1:
								check_banner = "✅"
							if flag9 == 1:
								check_icon = "✅"
							if flag10 == 1:
								check_color = "✅"
							if level >= 3:
								check_level2 = "✅"


							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 2", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho, cieszę się że udało ci się tu dotrzeć mam dla ciebie przygotowane nowe dodatki do profilu ale nie tylko.\n\nA teraz zaopatruj się w nowości.", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_color}", value=f"Kolorek profilu", inline=True)
							embed.add_field(name=f"{check_icon}", value=f"Ikona profilu", inline=True)
							embed.add_field(name=f"{check_banner}", value=f"Banner profilu", inline=True)
							embed.add_field(name=f"{check_tip}", value=f"Porada", inline=True)
							embed.add_field(name=f"{check_bank}", value=f"Przelewy", inline=True)
							embed.add_field(name=f"{check_level2}", value=f"Level up", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev2)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel2())

						if select.values[0] == "3":
							check_uczestnicy_plus = "❌"
							check_porada = "❌"
							check_reporter = "❌"
							check_kwiatek_idei = "❌"
							check_stopka = "❌"
							check_pisemna = "❌"
							check_level = "❌"


							if Role.uczestnicy_plus(interaction) in interaction.user.roles:
								check_uczestnicy_plus = "✅"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag1 = usersf[str(userf.id)]["flag1"]
							flag2 = usersf[str(userf.id)]["flag2"]
							flag3 = usersf[str(userf.id)]["flag3"]
							flag4 = usersf[str(userf.id)]["flag4"]
							flag5 = usersf[str(userf.id)]["flag5"]
							if level >= 2:
								check_level = "✅"
							if flag1 == 1:
								check_porada = "✅"
							if flag2 == 1:
								check_reporter = "✅"
							if flag3 == 1:
								check_kwiatek_idei = "✅"
							if flag4 == 1:
								check_stopka = "✅"
							if flag5 == 1:
								check_pisemna = "✅"


							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 1", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho, miło mi że odwiedzasz mój sklep.\nKup coś co ci się spodoba, możemy też pogadać jak chcesz.", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_uczestnicy_plus}", value=f"Uczestnicy+", inline=True)
							embed.add_field(name=f"{check_pisemna}", value=f"Sekcja pisemna profilu", inline=True)
							embed.add_field(name=f"{check_stopka}", value=f"Sekcja stopki profilu", inline=True)
							embed.add_field(name=f"{check_kwiatek_idei}", value=f"Kwiatek Idei", inline=True)
							embed.add_field(name=f"{check_reporter}", value=f"Reporter", inline=True)
							embed.add_field(name=f"{check_porada}", value=f"Porada", inline=True)
							embed.add_field(name=f"{check_level}", value=f"Level up", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev1)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel1())

			class MySelectShop2(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[
								discord.SelectOption(
									label="Wejdź do sklepu 2 poziomowego.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="1",
									emoji="<:D2_arrowup:972095071115689985>",
								),
								discord.SelectOption(
									label="Wejdź do sklepu 1 poziomowego.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="2",
									emoji="<:D3_arrowdown:972095071090507816>",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							check_color = "❌"
							check_icon = "❌"
							check_banner = "❌"
							check_tip = "❌"
							check_bank = "❌"
							check_level2 = "❌"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag6 = usersf[str(userf.id)]["flag6"]
							flag7 = usersf[str(userf.id)]["flag7"]
							flag8 = usersf[str(userf.id)]["flag8"]
							flag9 = usersf[str(userf.id)]["flag9"]
							flag10 = usersf[str(userf.id)]["flag10"]
							if flag6 == 1:
								check_tip = "✅"
							if flag7 == 1:
								check_bank = "✅"
							if flag8 == 1:
								check_banner = "✅"
							if flag9 == 1:
								check_icon = "✅"
							if flag10 == 1:
								check_color = "✅"
							if level >= 3:
								check_level2 = "✅"


							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 2", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho!\nCieszę się że udało ci się dotrzeć do drugiego sklepu, mam dla ciebie nowe dodatki do profilu i nie tylko.\n\nA teraz zaopatruj się w nowości!", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_color}", value=f"Kolorek profilu", inline=True)
							embed.add_field(name=f"{check_icon}", value=f"Ikona profilu", inline=True)
							embed.add_field(name=f"{check_banner}", value=f"Banner profilu", inline=True)
							embed.add_field(name=f"{check_tip}", value=f"Porada", inline=True)
							embed.add_field(name=f"{check_bank}", value=f"Przelewy", inline=True)
							embed.add_field(name=f"{check_level2}", value=f"Level up", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev2)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel2())

						if select.values[0] == "2":
							check_uczestnicy_plus = "❌"
							check_porada = "❌"
							check_reporter = "❌"
							check_kwiatek_idei = "❌"
							check_stopka = "❌"
							check_pisemna = "❌"
							check_level = "❌"


							if Role.uczestnicy_plus(interaction) in interaction.user.roles:
								check_uczestnicy_plus = "✅"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag1 = usersf[str(userf.id)]["flag1"]
							flag2 = usersf[str(userf.id)]["flag2"]
							flag3 = usersf[str(userf.id)]["flag3"]
							flag4 = usersf[str(userf.id)]["flag4"]
							flag5 = usersf[str(userf.id)]["flag5"]
							if level >= 2:
								check_level = "✅"
							if flag1 == 1:
								check_porada = "✅"
							if flag2 == 1:
								check_reporter = "✅"
							if flag3 == 1:
								check_kwiatek_idei = "✅"
							if flag4 == 1:
								check_stopka = "✅"
							if flag5 == 1:
								check_pisemna = "✅"


							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 1", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho, miło mi że odwiedzasz mój sklep.\nKup coś co ci się spodoba, możemy też pogadać jak chcesz.", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_uczestnicy_plus}", value=f"Uczestnicy+", inline=True)
							embed.add_field(name=f"{check_pisemna}", value=f"Sekcja pisemna profilu", inline=True)
							embed.add_field(name=f"{check_stopka}", value=f"Sekcja stopki profilu", inline=True)
							embed.add_field(name=f"{check_kwiatek_idei}", value=f"Kwiatek Idei", inline=True)
							embed.add_field(name=f"{check_reporter}", value=f"Reporter", inline=True)
							embed.add_field(name=f"{check_porada}", value=f"Porada", inline=True)
							embed.add_field(name=f"{check_level}", value=f"Level up", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev1)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel1())

			class MySelectShop(View):
					@discord.ui.select(
						placeholder="Wybierz co chcesz zrobić.",
							options=[
								discord.SelectOption(
									label="Wejdź do sklepu.",
									description="Wchodzisz do sklepu Suwi-Chan.",
									value="1",
									emoji="🚪",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							check_uczestnicy_plus = "❌"
							check_porada = "❌"
							check_reporter = "❌"
							check_kwiatek_idei = "❌"
							check_stopka = "❌"
							check_pisemna = "❌"
							check_level = "❌"


							if Role.uczestnicy_plus(interaction) in interaction.user.roles:
								check_uczestnicy_plus = "✅"

							await open_flag_profile(interaction.user)
							userf = interaction.user
							usersf = await get_profile_flag_date()
							await open_profile(interaction.user)
							user = interaction.user
							users = await get_profile_date()
							wallet = users[str(user.id)]["wallet"]
							level = users[str(user.id)]["level"]
							bank = users[str(user.id)]["bank"]
							flag1 = usersf[str(userf.id)]["flag1"]
							flag2 = usersf[str(userf.id)]["flag2"]
							flag3 = usersf[str(userf.id)]["flag3"]
							flag4 = usersf[str(userf.id)]["flag4"]
							flag5 = usersf[str(userf.id)]["flag5"]
							if level >= 2:
								check_level = "✅"
							if flag1 == 1:
								check_porada = "✅"
							if flag2 == 1:
								check_reporter = "✅"
							if flag3 == 1:
								check_kwiatek_idei = "✅"
							if flag4 == 1:
								check_stopka = "✅"
							if flag5 == 1:
								check_pisemna = "✅"


							embed = discord.Embed(title="<:C17_money:979762269263126558> Sklep:", description=f"Poziom sklepu który odwiedzasz: <:D2_arrowup:972095071115689985> 1", color=0xfceade)
							embed.add_field(name="Suwi-Chan", value=f"Nyanho, miło mi że odwiedzasz mój sklep.\nKup coś co ci się spodoba, możemy też pogadać jak chcesz.", inline=True)
							embed.add_field(name="Asortyment:", value=f"", inline=False)
							embed.add_field(name=f"{check_uczestnicy_plus}", value=f"Uczestnicy+", inline=True)
							embed.add_field(name=f"{check_pisemna}", value=f"Sekcja pisemna profilu", inline=True)
							embed.add_field(name=f"{check_stopka}", value=f"Sekcja stopki profilu", inline=True)
							embed.add_field(name=f"{check_kwiatek_idei}", value=f"Kwiatek Idei", inline=True)
							embed.add_field(name=f"{check_reporter}", value=f"Reporter", inline=True)
							embed.add_field(name=f"{check_porada}", value=f"Porada", inline=True)
							embed.add_field(name=f"{check_level}", value=f"Level up", inline=True)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"", value=f"", inline=False)
							embed.add_field(name=f"Otimi-coiny:", value=f":coin: {wallet}", inline=True)
							embed.add_field(name=f"Bank:", value=f":bank: {bank}", inline=True)
							embed.set_image(url=f"{random.choice(lev1)}")
							embed.set_thumbnail(url="https://i.postimg.cc/8zKm6gj0/Suwi.png")
							await interaction.response.edit_message(embed=embed,view=MySelectLevel1())

			await open_profile(interaction.user)
			user = interaction.user
			users = await get_profile_date()
			level = users[str(user.id)]["level"]
			if level == 3:
				levelShop = MySelectShop3()
			elif level == 2:
				levelShop = MySelectShop2()
			else:
				levelShop = MySelectShop()

			await interaction.response.send_message(view=levelShop,ephemeral = True)

		@tree.command(name = "pytania", description= "Tą komendą możesz zadać mi pytanie.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, tresc: str):
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if  interaction.channel == channel:
				responses = ["Czy mógłbyś zadać mi pytanie ponownie, bo nie dosłyszałam.","BEZ WĄTPIENIA TAK.","BEZ WĄTPIENIA NIE.","Zdecydowanie TAK.","Zdecydowanie NIE.","Najprawdopodobniej nie.","Najprawdopodobniej tak.","Ahh, Nie.","Ahh, Tak.","<:5163gchemoji13yes:926276739439669318>","<:emoji_6:921392219343171594>","taaaaaaak.","nieeeeeee.","Jest mi naprawdę przykro, że zadajesz mi takie pytanie <:emoji_16:921393487025422357>","Nie jestem pewna.","Chciałabym powiedzieć TAK, ale wszystko wskazuje na NIE.","Chciałabym powiedzieć NIE, ale wszystko wskazuje na TAK.","Muszę dłużej nad tym pomyśleć.","Nie licz na to.","Nie moge teraz powiedzieć.","Znaki na niebie mówią Nie.","Znaki na niebie mówią Tak.","Jakby się nad tym zastanowić Tak","Jakby się nad tym zastanowić Nie","Spytaj się kogoś innego.","Czemu zadajesz te pytanie akurat mi.","Możliwe.","Wydaje mi się że znam odpowiedź na twoje pytanie ale jakoś nie jestem przekonana czy chce ci mówić.","Daj mi spokój, jestem zmęczona.","Chyba tak.","Zapytaj moją młodszą siostrę.","Oczywiście że tak.","Oczywiście że nie.","Patrząc na ciebie zdecydowanie NIE.","Patrząc na ciebie zdecydowanie TAK.","Reasumując wszystkie aspekty kwintesencji tematu, dochodzę do fundamentalnej konkluzji, TAK.","Reasumując wszystkie aspekty kwintesencji tematu, dochodzę do fundamentalnej konkluzji, NIE.","Chyba nie."]

				if tresc == "0.9":
					await open_flag_profile(interaction.user)
					userf = interaction.user
					usersf = await get_profile_flag_date()
					flag13 = usersf[str(userf.id)]["flag13"]
					channel = await interaction.user.create_dm()
					if flag13 == 1:
						await interaction.response.send_message("Zdobyłeś już ten sekret <:0A41_love:1063248751889743968>", ephemeral = True)
					else:
						usersf[str(userf.id)]["flag13"] = 1
						with open("userflag.json","w") as f:
							json.dump(usersf,f)
						
						await open_profile(interaction.user)
						user = interaction.user
						users = await get_profile_date()
						reward = 9
						wallet = users[str(user.id)]["wallet"]
						users[str(user.id)]["wallet"] = wallet + reward
						with open("userprofile.json","w") as f:
							json.dump(users,f)

						embed = discord.Embed(title="Brawo, odkryłeś sekret !", description=f"W nagrodę za jego odkrycie zdobywasz 9 Otimi-coinów.", color=0xfceade)
						await interaction.response.send_message(embed=embed, ephemeral = True)

				else:
					embed = discord.Embed(title="Pytanie:", description=f"{tresc}", color=0xfceade)
					embed.set_thumbnail(url=config["avatar"])
					embed.add_field(name="Odpowiedź:", value=f"{random.choice(responses)}", inline=False)
					await interaction.response.send_message(embed=embed, ephemeral = False)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)