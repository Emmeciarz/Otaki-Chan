import discord
import wavelink
import json
from discord.ui import Button, View
from discord import FFmpegPCMAudio, RoleTags, VoiceChannel, channel
from discord.ext import commands
from wavelink.ext import spotify
from Commands import Role

queue = wavelink.Queue()

class CustomPlayer(wavelink.Player):
	def __init__(self):
		super().__init__()
		self.queue = wavelink.Queue()

class CustomCommands:
	def get_commands(tree,client):

		@tree.command(name = "join", description= "Pozwala ci na dołączenie Otaki-Chan do ciebie na kanał głosowy.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			
			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym żebym mogła do ciebie dołączyć {interaction.user.mention}.",ephemeral = True)
				
				elif vc is None:
					channel = interaction.user.voice.channel
					await channel.connect(cls=CustomPlayer())
					await interaction.response.send_message(f"Pomyślnie dołączono na kanał głosowy.",ephemeral = True)
				else:
					channel = interaction.user.voice.channel
					await vc.disconnect()
					await channel.connect(cls=CustomPlayer())
					await interaction.response.send_message(f"Pomyślnie dołączono na kanał głosowy.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)
			
		@tree.command(name = "leave", description= "Pozwala ci na rozłączenie Otaki-Chan z kanału głosowego.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			
			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				try:
					if vc.channel == interaction.user.voice.channel:
						await vc.disconnect()
						await interaction.response.send_message("Pomyślnie opuszczono kanał głosowy.",ephemeral = True)
					else:
						await interaction.response.send_message(f"Nye mogę wyjść z kanału głosowego jeśli nie jesteśmy razem {interaction.user.mention}.",ephemeral = True)
				except:
					if interaction.user.voice is None:
						await interaction.response.send_message(f"Nye mogę wyjść z kanału głosowego skoro na nim nie jesteś {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "play_yt", description= "Pozwala ci puścić wybrano przez ciebie piosenkę z youtube.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, search: str):
			search = await wavelink.YouTubeTrack.search(query=search, return_first=True)

			button = Button(label="Song", url=search.uri)
			view = View()
			view.add_item(button)

			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 698523673333858336)
			if  interaction.channel == channel or interaction.channel == mchannel:
				
				vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
				if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

					if interaction.user.voice is None:
						await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie puszczę wybranej przez ciebie piosenki {interaction.user.mention}.",ephemeral = True)
						return

					if not vc:
						custom_player = CustomPlayer()
						channel = interaction.user.voice.channel
						vc: CustomPlayer = await channel.connect(cls=custom_player)

					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_playing():

								vc.queue.put(item=search)
								embed = discord.Embed(title=f"{interaction.user.name} dodał do kolejki:", description=f"Autor: {search.author}\n\nTytuł: {search.title}", color=0xfceade)
								embed.set_thumbnail(url=interaction.user.avatar)
								embed.set_image(url=search.thumbnail)

								await interaction.response.send_message(embed=embed,view=view,ephemeral = False)
								
							else:
								await vc.play(search)

								embed = discord.Embed(title=f"{interaction.user.name} puścił piosenkę", description=f"Autor: {search.author}\n\nTytuł: {search.title}", color=0xfceade)
								embed.set_thumbnail(url=interaction.user.avatar)
								embed.set_image(url=search.thumbnail)
								await interaction.response.send_message(embed=embed,view=view,ephemeral = False)

						else:
							await interaction.response.send_message(f"Nye mogę tego dodać do kolejki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message(f"Nye mogę wyjść z kanału głosowego skoro na nim nie jesteś {interaction.user.mention}.",ephemeral = True)
				else:
					await interaction.response.send_message(f"Nye mogę puścić wybranej przez ciebie piosenki skoro  nie jesteś na kanale głosowym {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "play_sp", description= "Pozwala ci puścić wybrano przez ciebie piosenkę z spotify.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, search: str):
			search = await spotify.SpotifyTrack.search(query=search, return_first=True)

			button = Button(label="Song", url=search.uri)
			view = View()
			view.add_item(button)

			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 698523673333858336)
			if  interaction.channel == channel or interaction.channel == mchannel:

				vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
				if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
			
					if interaction.user.voice is None:
						await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie puszczę wybranej przez ciebie piosenki {interaction.user.mention}.",ephemeral = True)
						return

					if not vc:
						custom_player = CustomPlayer()
						channel = interaction.user.voice.channel
						vc: CustomPlayer = await channel.connect(cls=custom_player)

					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_playing():

								vc.queue.put(item=search)

								embed = discord.Embed(title=f"{interaction.user.name} dodał do kolejki:", description=f"Autor: {search.author}\n\nTytuł: {search.title}", color=0xfceade)
								embed.set_thumbnail(url=interaction.user.avatar)
								embed.set_image(url=search.thumbnail)
								await interaction.response.send_message(embed=embed,view=view,ephemeral = False)
							else:
								await vc.play(search)

								embed = discord.Embed(title=f"{interaction.user.name} puścił piosenkę", description=f"Autor: {search.author}\n\nTytuł: {search.title}", color=0xfceade)
								embed.set_thumbnail(url=interaction.user.avatar)
								embed.set_image(url=search.thumbnail)
								await interaction.response.send_message(embed=embed,view=view,ephemeral = False)
						else:
							await interaction.response.send_message(f"Nye mogę tego dodać do kolejki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message(f"Nye mogę wyjść z kanału głosowego skoro na nim nie jesteś {interaction.user.mention}.",ephemeral = True)
				else:
					await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)	
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale 🎵muzyka🎵.",ephemeral = True)

		@tree.command(name = "skip", description= "Pozwala ci pominąć obecnie grająco piosenkę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			
			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie pominę dla ciebie piosenki {interaction.user.mention}.",ephemeral = True)
					return

				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							if not vc.is_playing():
								return await interaction.response.send_message("Nye można pominąć piosenki skoro nic obecnie nie gra. ",ephemeral = True)
							if vc.queue.is_empty:
								await interaction.response.send_message("Pomyślnie pominięto piosenkę.",ephemeral = True)
								return await vc.stop()
								
							await vc.seek(vc.track.length * 1000)
							await interaction.response.send_message("Pomyślnie pominięto piosenkę.",ephemeral = True)

							if vc.is_paused():
								await vc.resume()
								await interaction.response.send_message("Pomyślnie pominięto piosenkę.",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę tego pominąć ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie pominąć piosenki ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie pominąć piosenki ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "pause", description= "Pozwala ci zatrzymać obecnie grająco piosenkę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie zatrzymam dla ciebie piosenki {interaction.user.mention}.",ephemeral = True)
					return
				
				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_playing() and not vc.is_paused():
								await vc.pause()
								await interaction.response.send_message(f"Pomyślnie zatrzymano piosenkę.",ephemeral = True)
							else:
								await interaction.response.send_message(f"Obecnie nie gra żadna piosenka którą mogła bym zatrzymać {interaction.user.mention}.",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę zatrzymać dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie zatrzymać piosenki ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie zatrzymać piosenki ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "resume", description= "Pozwala ci wznowić obecnie grająco piosenkę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie wznowie dla ciebie piosenki {interaction.user.mention}.",ephemeral = True)
					return
				
				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_paused():
								await vc.resume()
								await interaction.response.send_message(f"Pomyślnie wznowiono piosenkę.",ephemeral = True)
							else:
								await interaction.response.send_message(f"Obecnie nie jest wstrzymana żadna piosenka którą mogła bym wznowić {interaction.user.mention}.",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę wznowić dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie wznowić piosenki ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie wznowić piosenki ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "stop", description= "Pozwala ci wyłączyć obecnie grająco piosenkę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie zatrzymam dla ciebie piosenki {interaction.user.mention}.",ephemeral = True)
					return
				
				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_playing():
								await vc.stop()
								await interaction.response.send_message(f"Pomyślnie wyłączono piosenkę.",ephemeral = True)
							else:
								await interaction.response.send_message(f"Obecnie nie gra żadna piosenka którą mogła bym wyłączyć {interaction.user.mention}.",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę wyłączyć dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie wyłączyć piosenki ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie zatrzymać piosenki ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "volume", description= "Pozwala ci zmienić głośność muzyki Otaki-Chan", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, volume: int):

			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie zmienię głośności dla ciebie {interaction.user.mention}.",ephemeral = True)
					return
				
				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							await vc.set_volume(volume=volume)
							await interaction.response.send_message(f"Pomyślnie zmieniono głośność",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę zmienić głośności dla ciebie ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie zmienić głośności ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie zmienić głośności ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "reset", description= "Pozwala ci zresetować piosenkę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:

				if interaction.user.voice is None:
					await interaction.response.send_message(f"Nye jesteś na kanale głosowym dlatego nie zresetuję piosenki dla ciebie {interaction.user.mention}.",ephemeral = True)
					return

				if vc:
					try:
						if vc.channel == interaction.user.voice.channel:
							if vc.is_playing():
								await vc.seek(vc.track.duration)
								await interaction.response.send_message(f"Pomyślnie zresetowano piosenkę.",ephemeral = True)
							else:
								await interaction.response.send_message(f"obecnie nie gra żadna piosenka którą mogła bym zresetować {interaction.user.mention}.",ephemeral = True)
						else:
							await interaction.response.send_message(f"Nye mogę zresetować piosenki dla ciebie ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.",ephemeral = True)
					except:
						await interaction.response.send_message("Nye mogę obecnie zresetować piosenki ponieważ nie ma ciebie na kanale głosowym.",ephemeral = True)
				else:
					await interaction.response.send_message("Nye mogę obecnie zresetować piosenki ponieważ nie ma mnie na kanale głosowym.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "playlist", description= "Pokazuje twoją playliste.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,member:discord.Member=None):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 698523673333858336)
			if  interaction.channel == channel or interaction.channel == mchannel:
				if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
					if member == None:
						await open_playlist_account(interaction.user)
						user = interaction.user
						users = await get_playlist_date()

						one = users[str(user.id)]["one"]
						name = users[str(user.id)]["name"]
						emoji = users[str(user.id)]["emoji"]

						embed=discord.Embed(title="Playlista użytkownika:",description=f"{interaction.user}", color=0xfceade)
						embed.set_thumbnail(url=f"{interaction.user.avatar}")
						embed.add_field(name=f"Nazwa playlisty:",value=f"{name}", inline=False)
						embed.add_field(name=f"Songs:",value=f"", inline=False)

						for i in range(len(one)):
							embed.add_field(name=f"{emoji} |   {i+1}   | {emoji}",value=f"{one[i]}", inline=False)

						await interaction.response.send_message(embed=embed)
					else:
						await open_playlist_account(member)
						user = member
						users = await get_playlist_date()

						one = users[str(user.id)]["one"]
						name = users[str(user.id)]["name"]
						emoji = users[str(user.id)]["emoji"]
						
						embed=discord.Embed(title="Playlista użytkownika:",description=f"{member.display_name}", color=0xfceade)
						embed.set_thumbnail(url=f"{member.avatar}")
						embed.add_field(name=f"Nazwa playlisty:",value=f"{name}", inline=False)
						embed.add_field(name=f"Songs:",value=f"", inline=False)

						for i in range(len(one)):
							embed.add_field(name=f"{emoji} |   {i+1}   | {emoji}",value=f"{one[i]}", inline=False)

						await interaction.response.send_message(embed=embed)
				else:
					await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "add_playlist", description= "Pozwala ci dodać piosenkę do playlisty.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,song: str):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				await open_playlist_account(interaction.user)
				users = await get_playlist_date()
				user = interaction.user

				users[str(user.id)]["one"].append(song)

				with open("../playlist.json","w") as f:
					json.dump(users,f)
				
				await interaction.response.send_message(f"Pomyślnie dodano do playlisty {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "remove_playlist", description= "Pozwala ci usunąć piosenkę z playlisty.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,position: int):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				await open_playlist_account(interaction.user)
				users = await get_playlist_date()
				user = interaction.user

				true_position = position - 1
				users[str(user.id)]["one"].pop(true_position)

				with open("../playlist.json","w") as f:
					json.dump(users,f)
				
				await interaction.response.send_message(f"Pomyślnie usunięto pozycje {position} z playlisty {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "clear_playlist", description= "Pozwala ci wyczyścić wszystkie piosenki z playlisty.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				await open_playlist_account(interaction.user)
				users = await get_playlist_date()
				user = interaction.user

				users[str(user.id)]["one"].clear()

				with open("../playlist.json","w") as f:
					json.dump(users,f)
				
				await interaction.response.send_message(f"Pomyślnie wyczyszczono playliste {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "clone_playlist", description= "Pozwala ci sklonować cało playliste innego uczestnika do twojej playlisty.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member:discord.Member):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				await open_playlist_account(interaction.user)
				users = await get_playlist_date()
				user = interaction.user

				await open_playlist_account(member)
				m_users = await get_playlist_date()
				m_user = member

				m_playlist = m_users[str(m_user.id)]["one"]

				users[str(user.id)]["one"].append(m_playlist)

				with open("../playlist.json","w") as f:
					json.dump(users,f)
				
				await interaction.response.send_message(f"Pomyślnie dokonano klonowania playlisty {member.mention} do twojej playlisty {interaction.user.mention}.",ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)


		# @tree.command(name = "play_playlist", description= "Pozwala ci puścić cało twoją playliste.", guild = discord.Object(id = 698522294414344232))
		# async def self(interaction: discord.Integration):
		
		@tree.command(name = "setting_playlist", description= "Pozwala ci ustawić twoją playliste.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration,name: str, emoji: str):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				await open_playlist_account(interaction.user)
				user = interaction.user
				users = await get_playlist_date()

				users[str(user.id)]["name"] = name
				users[str(user.id)]["emoji"] = emoji

				with open("../playlist.json","w") as f:
					json.dump(users,f)

				await interaction.response.send_message(f"Pomyślnie zmieniono ustawienia playlisty {interaction.user.mention}.",ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		async def open_playlist_account(user):
			with open("../playlist.json","r") as f:
				users = await get_playlist_date()

				if str(user.id) in users:
					return False
				else:
					users[str(user.id)] = {}
					users[str(user.id)]["one"] = []					
					users[str(user.id)]["name"] = "name"
					users[str(user.id)]["emoji"] = "🎶"

				with open("../playlist.json","w") as f:
					json.dump(users,f)
				return True
		
		async def get_playlist_date():
			with open("../playlist.json","r") as f:
				users = json.load(f)
			return users

		@client.event
		async def on_wavelink_track_end(player: CustomPlayer, track: wavelink.Track, reason):
			if not player.queue.is_empty:
				channel = discord.utils.get(player.guild.channels, name="🎵muzyka🎵")
				channel = discord.utils.get(player.guild.channels, id = 698523673333858336)
				next_track = player.queue.get()
				await player.play(next_track)
				# print(player.queue.count)
				# print(player.queue.find_position(id))
				# print(player.queue.find_position(1))
				# print(player.queue.find_position(item=1))
				await channel.send(f"obecnie w kolejce znajduje się {player.queue.count} piosenek.")

		@tree.command(name = "controller", description= "Pozwala ci przywołać kontroler do łatwiejszej obsługi komend muzycznych.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				class MyView(View):

					@discord.ui.button(label="Join", style=discord.ButtonStyle.green)
					async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym żebym mogła do ciebie dołączyć {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
				
						elif vc is None:
							channel = interaction.user.voice.channel
							await channel.connect(cls=CustomPlayer())
							await interaction.response.edit_message(content="Pomyślnie dołączono na kanał głosowy.\nPanel kontrolny:",view=MyView())
						else:
							channel = interaction.user.voice.channel
							await vc.disconnect()
							await channel.connect(cls=CustomPlayer())
							await interaction.response.edit_message(content="Pomyślnie dołączono na kanał głosowy.\nPanel kontrolny:",view=MyView())

					@discord.ui.button(label="Leave", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
						try:
							if vc.channel == interaction.user.voice.channel:
								await vc.disconnect()
								await interaction.response.edit_message(content=f"Pomyślnie opuszczono kanał głosowy.\nPanel kontrolny:",view=MyView())
							else:
								await interaction.response.edit_message(content=f"Nye mogę wyjść z kanału głosowego jeśli nie jesteśmy razem {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
						except:
							if interaction.user.voice is None:
								await interaction.response.edit_message(content=f"Nye mogę wyjść z kanału głosowego skoro na nim nie jesteś {interaction.user.mention}.\nPanel kontrolny:",view=MyView())

					@discord.ui.button(label="Pause", style=discord.ButtonStyle.primary)
					async def primary1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)

						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym dlatego nie zatrzymam dla ciebie piosenki {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							return

						if vc:
							try:
								if vc.channel == interaction.user.voice.channel:
									if vc.is_playing() and not vc.is_paused():
										await vc.pause()
										await interaction.response.edit_message(content="Pomyślnie wstrzymano piosenkę.\nPanel kontrolny:",view=MyView())
									else:
										await interaction.response.edit_message(content=f"Obecnie nie gra żadna piosenka którą mogła bym zatrzymać {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
								else:
									await interaction.response.edit_message(content=f"Nye mogę zatrzymać dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							except:
								await interaction.response.edit_message(content="Nye mogę obecnie zatrzymać piosenki ponieważ nie ma ciebie na kanale głosowym.\nPanel kontrolny:",view=MyView())
						else:
							await interaction.response.edit_message(content=f"Skoro nie jesteś na kanale głosowym to nie widzę potrzeby żeby dla ciebie zatrzymywać {interaction.user.mention}.\nPanel kontrolny:",view=MyView())

					@discord.ui.button(label="Resume", style=discord.ButtonStyle.primary)
					async def primary2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym dlatego nie wznowię dla ciebie piosenki {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							return
						
						if vc:
							try:
								if vc.channel == interaction.user.voice.channel:
									if vc.is_paused():
										await vc.resume()
										await interaction.response.edit_message(content="Pomyślnie wznowiono piosenkę.\nPanel kontrolny:",view=MyView())
									else:
										await interaction.response.edit_message(content=f"Obecnie nie jest wstrzymana żadna piosenka którą mogła bym wznowić {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
								else:
									await interaction.response.edit_message(content=f"Nye mogę wznowić dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							except:
								await interaction.response.edit_message(content="Nye mogę obecnie wznowić piosenki ponieważ nie ma ciebie na kanale głosowym.\nPanel kontrolny:",view=MyView())
						else:
							await interaction.response.edit_message(content=f"Skoro nie jesteś na kanale głosowym to nie widzę potrzeby żeby dla ciebie wznawiać {interaction.user.mention}.\nPanel kontrolny:",view=MyView())

					@discord.ui.button(label="Stop", style=discord.ButtonStyle.grey)
					async def grey_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)

						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym dlatego nie zatrzymam dla ciebie piosenki {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							return
						
						if vc:
							try:
								if vc.channel == interaction.user.voice.channel:
									if vc.is_playing():
										await vc.stop()
										await interaction.response.edit_message(content="Pomyślnie zatrzymaano piosenkę.\nPanel kontrolny:",view=MyView())
									else:
										await interaction.response.edit_message(content=f"Obecnie nie gra żadna piosenka którą mogła bym wyłączyć {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
								else:
									await interaction.response.edit_message(content=f"Nye mogę zatrzymać dla ciebie piosenki ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							except:
								await interaction.response.edit_message(content="Nye mogę obecnie zatrzymać piosenki ponieważ nie ma ciebie na kanale głosowym.\nPanel kontrolny:",view=MyView())
						else:
							await interaction.response.edit_message(content=f"Skoro nie jesteś na kanale głosowym to nie widzę potrzeby żeby dla ciebie zatrzymywać {interaction.user.mention}.\nPanel kontrolny:",view=MyView())

					@discord.ui.button(label="Reset", style=discord.ButtonStyle.primary)
					async def primary4_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
			
						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym dlatego nie zresetuję piosenki dla ciebie {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							return

						if vc:
							try:
								if vc.channel == interaction.user.voice.channel:
									if vc.is_playing():
										await vc.seek(vc.track.duration)
										await interaction.response.edit_message(content=f"Pomyślnie zresetowano piosenkę.\nPanel kontrolny:",view=MyView())
									else:
										await interaction.response.edit_message(content=f"obecnie nie gra żadna piosenka którą mogła bym zresetować {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
								else:
									await interaction.response.edit_message(content=f"Nye mogę zresetować piosenki dla ciebie ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							except:
								await interaction.response.edit_message(content="Nye mogę obecnie zresetować piosenki ponieważ nie ma ciebie na kanale głosowym.\nPanel kontrolny:",view=MyView())
						else:
							await interaction.response.edit_message(content="Nye mogę obecnie zresetować piosenki ponieważ nie ma mnie na kanale głosowym.\nPanel kontrolny:",view=MyView())
			
					@discord.ui.button(label="Skip", style=discord.ButtonStyle.primary)
					async def primary3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						vc: discord.VoiceClient = discord.utils.get(client.voice_clients)
						if interaction.user.voice is None:
							await interaction.response.edit_message(content=f"Nye jesteś na kanale głosowym dlatego nie pominę dla ciebie piosenki {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							return

						if vc:
							try:
								if vc.channel == interaction.user.voice.channel:
									if not vc.is_playing():
										return await interaction.response.edit_message(content="Nye można pominąć piosenki skoro nic obecnie nie gra.\nPanel kontrolny:",view=MyView())
									if vc.queue.is_empty:
										await interaction.response.edit_message(content="Pomyślnie pominięto piosenkę.\nPanel kontrolny:",view=MyView())
										return await vc.stop()
										
									await vc.seek(vc.track.length * 1000)
									await interaction.response.edit_message(content="Pomyślnie pominięto piosenkę.\nPanel kontrolny:",view=MyView())

									if vc.is_paused():
										await vc.resume()
										await interaction.response.edit_message(content="Pomyślnie pominięto piosenkę.\nPanel kontrolny:",view=MyView())
								else:
									await interaction.response.edit_message(content=f"Nye mogę tego pominąć ponieważ nie jesteśmy razem na kanale {interaction.user.mention}.\nPanel kontrolny:",view=MyView())
							except:
								await interaction.response.edit_message(content="Nye mogę obecnie pominąć piosenki ponieważ nie ma ciebie na kanale głosowym.\nPanel kontrolny:",view=MyView())
						else:
							await interaction.response.edit_message(content="Nye mogę obecnie pominąć piosenki ponieważ nie ma mnie na kanale głosowym.\nPanel kontrolny:",view=MyView())
					
				view = MyView()
				await interaction.response.send_message(f"Panel kontrolny:", view=view ,ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)


