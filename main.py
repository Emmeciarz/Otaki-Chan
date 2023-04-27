import os
import discord
import json
import random
import wavelink
import time
import asyncio
import platform
from wavelink.ext import spotify
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle
from pathlib import Path
from discord.ui import Button, View

from Commands import Commands, Kick, Vc, Role
from Commands.EcoRpg import EcoRpg

with open("./config.json") as f:
	config = json.load(f)

status = cycle(['/help',f'v{config["version"]}'])

BOOST_TYPES = discord.MessageType.premium_guild_subscription, discord.MessageType.premium_guild_tier_1, discord.MessageType.premium_guild_tier_2, discord.MessageType.premium_guild_tier_3

data_role_path = Path(r"../role.json")

@tasks.loop(seconds=15)
async def status_swap():
	await client.change_presence(activity=discord.Game(next(status)))

class aclient(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.all())
		self.synced = False

	async def on_message(self,message):
		if message.is_system() and message.type in BOOST_TYPES:
			client.dispatch("server_boost", message.author)

	async def on_server_boost(self,member):
		channel = member.guild.get_channel(920080200308506676)#id kanału
		responses = ["https://i.postimg.cc/FHXMfhmc/anime-girl.gif",#zielone włosy
					"https://i.postimg.cc/WbZRbdRT/anime-heart.gif",#Hatsune 
					"https://i.postimg.cc/jS6GPBd1/i-love-you-kiss.gif",#I love you
					"https://i.postimg.cc/RCy5BcDg/neko-anime.gif",#cynamon heart
					"https://i.postimg.cc/L5rr3p1c/snap.gif"]#azunya

		embed = discord.Embed(title="O Dziękuje!", description=f"Jesteś bardzo kochano osobo że decydujesz się ulepszyć naszą społeczność.{member.mention}", color=0xfceade)
		embed.set_thumbnail(url=config["avatar"])
		embed.set_image(url=f"{random.choice(responses)}")
		await channel.send(embed=embed)

	async def on_ready(self):
		await self.wait_until_ready()
		if not self.synced:
			await tree.sync(guild= discord.Object(id= 698522294414344232))
			self.synced = True
		print(f'{self.user} Jestem Włączona!')
		print('Wersja discord.py')
		print(discord.__version__)
		print('System operacyjny')
		print(platform.system(),platform.release())
		status_swap.start()
		client.loop.create_task(connect_nodes())

	async def on_wavelink_node_ready(self,node: wavelink.Node):
		print("Nawiązano połączenie z Lavalink")
		print(f"Node: <{node.identifier}> jest gotowy do pracy!")

	async def on_raw_reaction_add(self,payload):

		if payload.member.bot:
			pass
				
		else:
			with open(data_role_path) as react_file:

				data = json.load(react_file)
				for x in data:
					if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
						role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x["role_id"])

						await payload.member.add_roles(role)

	async def on_raw_reaction_remove(self,payload):

		with open(data_role_path) as react_file:

			data = json.load(react_file)
			for x in data:
				if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
					role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x["role_id"])

					await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

	async def on_member_join(self,member):
		guild = client.get_guild(698522294414344232) #Id: Serwera Nya
		welcome_channel = guild.get_channel(920080200308506676) # Id: Pogawędek Ayayaya 

		responses = ["https://i.postimg.cc/JhnbmGfd/anime-welcome.gif",#senko
					"https://i.postimg.cc/GtbsR9sx/school-live-cute.gif",#otwieranie drzwi
					"https://i.postimg.cc/tgSNVhdj/noneed-yourewelcome.gif",#Mani hi
					"https://i.postimg.cc/TwVWBnhP/welcome-to-the-server.gif",#migające welcome
					"https://i.postimg.cc/cJ4cHDnh/welcome-1.gif",#hatsune miku
					"https://i.postimg.cc/KcdR94hJ/n1.gif",#dotykanie butelki
					"https://i.postimg.cc/XNZrcdmr/n2.gif",#powoli pojawiające się welcome
					"https://i.postimg.cc/xqDDLW73/n3.gif",#welcome uśmiech
					"https://i.postimg.cc/tCW78yXy/n4.gif",#przymulane machanie
					"https://i.postimg.cc/2Sdm7SCb/n5.gif",#wspólne machanie
					"https://i.postimg.cc/GmjQb0H9/ohayo.gif"] #ayaya

		channel = member.guild.get_channel(926305651968315393)
		embed = discord.Embed(title="Hej, Jestem Otaki-chan.", description=f"Cieszę się że dołączasz do naszej społeczności {member.mention}\n\n**Pamiętaj** jeśli będziesz potrzebować mojej **pomocy** wpisz ***/help***\n**Nie zapomnij** również o odwiedzeniu kanałów\n{channel.mention},\n#Kanały i role.", color=0xfceade)
		embed.set_thumbnail(url=config["avatar"])
		embed.set_image(url=f"{random.choice(responses)}")
		embed.set_footer(text=f"Nick podczas dołączenia: {member.name}")
		await welcome_channel.send(embed=embed)

	async def on_member_update(self,before, after):
		everyone = discord.utils.get(before.guild.roles, id=698522294414344232)
		if everyone in after.guild.roles:
			role  = discord.utils.get(after.guild.roles, id=1093563230250614846)#kolorek dla osób po wejściu
			await after.add_roles(role)

	async def on_member_ban(self,guild,member):

		goodbye_channel = guild.get_channel(922781362514190386) # Id: Modowędki

		logs = [log async for log in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban)]
		logs = logs[0]

		embed = discord.Embed(title=f"Uczestnik:", description=f"{member.mention} został zbanowany przez: {logs.user.mention}", color=0xfceade)
		embed.set_thumbnail(url=member.avatar)
		await goodbye_channel.send(embed=embed)

	async def on_member_remove(self,member):

		guild = client.get_guild(698522294414344232) #Id: Serwera Nya
		goodbye_channel = guild.get_channel(922781362514190386) # Id: Modowędki
		check_ban = False
		async for entry in guild.bans(limit=None):
			if entry.user == member:
				check_ban = True
		
		if check_ban == False:
			embed = discord.Embed(title="Uczestnik:", description=f"{member.mention} Znany nam jako {member.name} opuścił serwer {guild.name}", color=0xfceade)
			embed.set_thumbnail(url=member.avatar)
			await goodbye_channel.send(embed=embed)

	async def on_invite_create(self,invite):
		class MyButton(View):
			@discord.ui.button(label="delete", style=discord.ButtonStyle.danger)
			async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
				button.disabled = True
				await invite.delete()
				embed.add_field(name="USUNIĘTO", value=f"", inline=False)
				await interaction.response.edit_message(content="Usunięto",embed=embed,view=None)

		guild = client.get_guild(698522294414344232) #Id: Serwera Nya
		modowedki_channel = guild.get_channel(922781362514190386) # Id: Modowędki

		embed = discord.Embed(title="Uczestnik:", description=f"{invite.inviter.mention} Znany nam jako {invite.inviter.name} stworzył\nzaprosznie na serwer {guild.name}", color=0xfceade)
		embed.add_field(name="Informacje odnośnie zaprosznia:", value=f"Link: {invite.url}\nNa kanał: {invite.channel}", inline=False)
		embed.set_thumbnail(url=invite.inviter.avatar)


		await modowedki_channel.send(embed=embed,view=MyButton())

async def connect_nodes():
	await client.wait_until_ready()
	await wavelink.NodePool.create_node(
		bot=client,
		host='10.0.0.87',
		port=2333,
		password='reimu9',
		spotify_client=spotify.SpotifyClient(client_id='5c3a5ccfd93249db82e2329bc2369510', client_secret='24e776814362406da2494d142026abb5')
	)

client = aclient()
tree = app_commands.CommandTree(client)
@tree.command(name = "version", description= "Pokazuję moją wersje.", guild = discord.Object(id = 698522294414344232))
async def self(interaction: discord.Integration):
	embed=discord.Embed(title="Wersja Otaki-Chan.", description=f'Obecnie posiadam wersje: {config["version"]}', color=0xfceade)
	embed.set_thumbnail(url = config["avatar"])
	await interaction.response.send_message(embed=embed, ephemeral = False)

@tree.command(name = "logs", description= "Pokazuje opisy moich wersji.", guild = discord.Object(id = 698522294414344232))
async def self(interaction: discord.Integration):
	class MyButton(View):
		@discord.ui.button(label="Back", style=discord.ButtonStyle.gray)
		async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
			button.disabled = True
			await interaction.response.edit_message(content=None,embed=None,view=MySelectView())

	class MySelectView(View):
		@discord.ui.select(
			placeholder="Wybierz wersje.",
				options=[

					discord.SelectOption(
						label="0.7.5",
						emoji="💮",
						value="6",
					),

					discord.SelectOption(
						label="0.7.1",
						value="5",
					),

					discord.SelectOption(
						label="0.7",
						value="4",
					),

					discord.SelectOption(
						label="0.6.5",
						value="3",
					),

					discord.SelectOption(
						label="0.6.1",
						value="2",
					),

					discord.SelectOption(
						label="0.6",
						value="1",
					),
				],)

		async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
			select.disabled = True

			if select.values[0] == "6":

				embed = discord.Embed(title="Wersja: 0.7.5", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Dodano:", value=f"Pokazywanie czy ktoś stworzył zaproszenie oraz przycisk je usuwający.", inline=False)
				embed.add_field(name="Dodano:", value=f"Automatyczne dodawanie koloru nowym uczestnikom.", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

			if select.values[0] == "5":

				embed = discord.Embed(title="Wersja: 0.7.1", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Poprawiono:", value=f"/janken", inline=False)
				embed.add_field(name="Dodano:", value=f"context menu janken", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

			if select.values[0] == "4":

				embed = discord.Embed(title="Wersja: 0.7", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Ulepszono:", value=f"Powiadomienia nowych osób ", inline=False)
				embed.add_field(name="Ulepszono:", value=f"Powiadomienia wychodzących osób ", inline=False)
				embed.add_field(name="Lekko zmieniono:", value=f"/pytania", inline=False)
				embed.add_field(name="Dodano:", value=f"Config Otaki-chan", inline=False)
				embed.add_field(name="Dodano:", value=f"/janken", inline=False)
				embed.add_field(name="Dodano:", value=f"context menu janken", inline=False)
				embed.add_field(name="Dodano:", value=f"context menu pong", inline=False)
				embed.add_field(name="Zoptymalizowano:", value=f"Otaki-Chan", inline=False)
				embed.add_field(name="Naprawiono:", value=f"Komunikaty.", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

			if select.values[0] == "3":

				embed = discord.Embed(title="Wersja: 0.6.5", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Zoptymalizowano:", value=f"Otaki-Chan", inline=False)
				embed.add_field(name="Dodano:", value=f"/server_set", inline=False)
				embed.add_field(name="Ulepszono:", value=f"Zbiór komend głosowych.", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

			if select.values[0] == "2":

				embed = discord.Embed(title="Wersja: 0.6.1", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Usunięto:", value=f"/log", inline=False)
				embed.add_field(name="Dodano:", value=f"/logs", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

			if select.values[0] == "1":
				embed = discord.Embed(title="Wersja: 0.6", description=f"", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Dodano:", value=f"/vocabulary", inline=False)
				embed.add_field(name="Ulepszono/Naprawiono:", value=f"Powiadomienia nowych osób.", inline=False)
				embed.add_field(name="Naprawiono:", value=f"Małe błędy i komunikaty.", inline=False)
				await interaction.response.edit_message(embed=embed,view=MyButton())

	view = MySelectView()
	await interaction.response.send_message(view=view, ephemeral = True)




Vc.CustomCommands.get_commands(tree,client)
Kick.CustomCommands.get_commands(tree,client)
EcoRpg.CustomCommands.get_commands(tree,client)
Commands.CustomCommands.get_commands(tree,client)

if platform.system() == "Windows":
	client.run(config["mtoken"])
elif platform.system() == "Linux":
	client.run(config["otoken"])
else:
	print("Nie rozpoznaje jednego z dwóch systemów operacyjnych z których korzystam Windows/Linux.")