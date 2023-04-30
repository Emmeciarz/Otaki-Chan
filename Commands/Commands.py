from typing import Counter
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from pathlib import Path
import random
import json
import time

from Commands import Role
data_role_path = Path(r"../role.json")

with open("./config.json") as f:
	config = json.load(f)

class CustomCommands:
	def get_commands(tree,client):
		
		@tree.command(name = "help", description= "Pokazuję zbiory komend.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			class MyButton(View):
					@discord.ui.button(label="Back", style=discord.ButtonStyle.gray)
					async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=None,embed=None,view=MySelectView())

			class MySelectView(View):
				@discord.ui.select(
					placeholder="Wybierz zbiór komend.",
						options=[

							discord.SelectOption(
								label="Help",
								description="Pokazuję zbiory komend.",
								value="1",
								emoji="🔖",
							),

							discord.SelectOption(
								label="Helpg",
								description="Pokazuję ogólne komendy które posiadam.",
								value="2",
								emoji="📗",
							),

							discord.SelectOption(
								label="Helpg+",
								description="Pokazuję komendy dla Uczestników+/Server Boosterów.",
								value="5",
								emoji="📙",
							),

							discord.SelectOption(
								label="Helpm",
								description="Pokazuję komendy dla administracji serwera.",
								value="3",
								emoji="📕",
							),

							discord.SelectOption(
								label="Helpvc",
								description="Pokazuję komendy związane z kanałem głosowym.",
								value="4",
								emoji="📓",
							),
						],)

				async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
					select.disabled = True
					if select.values[0] == "1":

						embed = discord.Embed(title="Proszę, oto wszystkie dostępne zbiory komend.", description='Wymienię ci tu wszystkie zbiory komend które możesz wywołać za po mocą  "/help".', color=0xfceade)
						embed.set_thumbnail(url=config["avatar"])
						embed.add_field(name="🔖 help", value="Pokazuję zbiory komend.", inline=False)
						embed.add_field(name="📗 helpg", value="Pokazuję ogólne komendy które posiadam.", inline=False)
						embed.add_field(name="📙 helpg+", value="Pokazuję komendy dla Uczestników+ oraz Server Boosterów.", inline=False)
						embed.add_field(name="📕 helpm", value="Pokazuję komendy dla administracji serwera.", inline=False)
						embed.add_field(name="📓 helpvc", value="Pokazuję komendy związane z kanałem głosowym.", inline=False)
						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "2":

						embed = discord.Embed(title="Proszę, oto zbiór wszystkich komend generalnych.", description="Wymienie ci tu wszystkie komendy generalne jakie obsługuję, i co one robią.", color=0xfceade)
						embed.set_thumbnail(url=config["avatar"])
						embed.add_field(name=":white_check_mark: /info", value="Pokazuje informacje odnośnie serwera.", inline=False)
						embed.add_field(name=":white_check_mark: /life_time", value="Pokazuję jak długo działam bez snu.", inline=False)
						embed.add_field(name=":white_check_mark: /avatar", value="Pozwala ci wyświetlić avatar wybranej przez ciebie osoby.", inline=False)
						embed.add_field(name=":white_check_mark: /ping", value="Pokazuję opóźnienie między tobą a discordem.", inline=False)
						embed.add_field(name=":white_check_mark: /py", value="Tą komendą możesz zadać mi pytanie. Aby jej użyć, musisz wpisać komendę, a po spacji pytanie na które mogę odpowiedzieć Tak/Nie.", inline=False)
						embed.add_field(name=":white_check_mark: /kiss", value=f"Pozwala ci pocałować wybrano przez ciebie osobę.", inline=False)
						embed.add_field(name=":white_check_mark: /hug", value=f"Pozwala ci przytulić wybrano przez ciebie osobę.", inline=False)
						embed.add_field(name=":white_check_mark: /pat", value=f"Pozwala ci pogłaskać wybrano przez ciebie osobę.", inline=False)
						embed.add_field(name=":white_check_mark: /slap", value=f"Pozwala ci uderzyć wybrano przez ciebie osobę.", inline=False)
						embed.add_field(name=":white_check_mark: /handshake", value=f"Pozwala ci uścisnąć dłoń wybranej przez ciebie osobie.", inline=False)
						embed.add_field(name=":white_check_mark: /pong", value=f"Pozwala ci na zaproszenie kogoś do wspólnego rzucania piłeczką.", inline=False)
						embed.add_field(name=":white_check_mark: /version", value=f"Pokazuję wersję Otaki-Chan", inline=False)
						embed.add_field(name=":white_check_mark: /logs", value=f"Pokazuję logi Otaki-Chan", inline=False)
						embed.add_field(name=":white_check_mark: /vocabulary", value=f"Pokazuję ci słowniczek Otakumani.", inline=False)
						embed.add_field(name=":white_check_mark: /dice", value=f"Pozwala ci rzucić wybraną przez siebie kostką.", inline=False)
						embed.add_field(name=":white_check_mark: /donacje", value=f"Możesz to komendą podarować mi trochę radości.", inline=False)
						embed.add_field(name="Komendy które po lewej stronie posiadają znaczek:", value=f":white_check_mark: działają poprawnie.\n<:AAEC_karenThink:981262325061419009> działają ale nie do końca dobrze.\n<:9881_NotHuTao:926276740437921843> Nie działają lub działają nie właściwie.", inline=False)
						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "3":

						if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
							embed = discord.Embed(title="Proszę, oto zbiór wszystkich komend dla moderacji serwera.", description="Wymienię ci wszystkie komendy jakie obsługuję, i co one robią.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name=":white_check_mark: /sp", value=f"Ta komenda pozwala ci na usuwanie dużej ilości wiadomości.", inline=False)
							embed.add_field(name=":white_check_mark: /otaki", value=f"Piszesz przeze mnie i wysyłam to na wybrany przez ciebie kanał.", inline=False)
							embed.add_field(name=":white_check_mark: /ny", value=f"Pozwala wybrać zbiory pytań do wysłania dla uczestników.", inline=False)
							embed.add_field(name=":white_check_mark: /volume", value=f"Pozwala ci zmienić głośność Otaki-chan", inline=False)
							embed.add_field(name=":white_check_mark: /ban", value=f"Banujesz osobę na serwerze.", inline=False)
							embed.add_field(name=":white_check_mark: /kick", value=f"Wyrzucasz osobę z serwera.", inline=False)
							embed.add_field(name=":white_check_mark: /server_set", value=f"Pozwala na zmianę wyglądu serwera.", inline=False)
							embed.add_field(name=":white_check_mark: /creation", value=f"ta komenda pozwala ci na tworzenie wiadomości z reakcjami emoji po których na ciśniecu daję rolę a po zabraniu reakcji zabiera.", inline=False)
							embed.add_field(name="Komendy które po lewej stronie posiadają znaczek:", value=f":white_check_mark: działają poprawnie.\n<:AAEC_karenThink:981262325061419009> działają ale nie do końca dobrze.\n<:9881_NotHuTao:926276740437921843> Nie działają lub działają nie właściwie.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyButton())
						else:
							await interaction.response.edit_message(content=f"Nye masz uprawnień do wyświetlania tego zbioru komend {interaction.user.mention}.",view=MyButton())

					if select.values[0] == "4":

						if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
							embed = discord.Embed(title="Proszę, oto zbiór wszystkich komend związanych z kanałem głosowym.", description="Wymienie ci tu wszystkie komendy związane z kanałem głosowym jakie obsługuję, i co one robią.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name=":white_check_mark: /join", value="Pozwala ci na dołączenie Otaki-Chan do ciebie na kanał głosowy.", inline=False)
							embed.add_field(name=":white_check_mark: /leave", value="Pozwala ci na rozłączenie Otaki-Chan z kanału głosowego.", inline=False)
							embed.add_field(name=":white_check_mark: /pause", value=f"Pozwala ci zatrzymać obecnie grająco piosenkę.", inline=False)
							embed.add_field(name=":white_check_mark: /stop", value=f"Pozwala ci wyłączyć obecnie grająco piosenkę.", inline=False)
							embed.add_field(name=":white_check_mark: /skip", value=f"Pozwala ci pominąć obecnie grająco piosenkę.", inline=False)
							embed.add_field(name=":white_check_mark: /resume", value=f"Pozwala ci wznowić obecnie grająco piosenkę.", inline=False)
							embed.add_field(name=":white_check_mark: /reset", value=f"Pozwala ci zresetować piosenkę.", inline=False)
							embed.add_field(name=":white_check_mark: /controller", value=f"Pozwala ci przywołać kontroler do łatwiejszej obsługi komend muzycznych.", inline=False)
							embed.add_field(name="<:AAEC_karenThink:981262325061419009> /play_yt", value=f"Pozwala ci puścić wybrano przez ciebie piosenkę z youtuba za pomocą linka lub tytułu.", inline=False)
							embed.add_field(name="<:AAEC_karenThink:981262325061419009> /play_sp", value=f"Pozwala ci puścić wybrano przez ciebie piosenkę z spotify za pomocą linka.", inline=False)
							embed.add_field(name="Komendy które po lewej stronie posiadają znaczek:", value=f":white_check_mark: działają poprawnie.\n<:AAEC_karenThink:981262325061419009> działają ale nie do końca dobrze.\n<:9881_NotHuTao:926276740437921843> Nie działają lub działają nie właściwie.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyButton())
						else:
							await interaction.response.edit_message(content=f"Nye masz uprawnień do wyświetlania tego zbioru komend {interaction.user.mention}.",view=MyButton())

					if select.values[0] == "5":

						if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
							embed = discord.Embed(title="Proszę, oto zbiór wszystkich komend dla Uczestników+ oraz Server Boosterów.", description="Wymienię ci wszystkie komendy jakie obsługuję, i co one robią.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name=":white_check_mark: /kolorkowo", value=f"Wywołuje paletę kolorów.", inline=False)
							embed.add_field(name=":white_check_mark: /janken", value=f"Pozwala ci na zagranie z kimś w papier, kamień, nożyce.", inline=False)
							embed.add_field(name=":white_check_mark: /embeds", value=f'Pozwala ci na tworzenie własnych wiadomości embedowych. Objaśnię ci każdą rubryczkę którą się tam wpisuje:', inline=False)
							embed.add_field(name="title", value=f"Odpowiada za główny tytuł twojej wiadomości", inline=False)
							embed.add_field(name="description", value=f"Odpowiada za opis główny twojej wiadomości znajduję się tuż pod tytułem", inline=False)
							embed.add_field(name="Opcjonalne ustawienia", value=f"teraz przedstawię ci opcje dodatkowe które ulepszą twoją wiadomość ale nie są wymagane:", inline=False)
							embed.add_field(name="footer", value=f"Dodaje stopkę pod twoją wiadomością", inline=False)
							embed.add_field(name="avatar", value=f"Pozwala ci wybrać przez ciebie uczestnika którego avatar będzie się wyświetlał w wiadomości", inline=False)
							embed.add_field(name="image", value=f"Pozwala ci na dodanie głównego obrazka poprzez podanie bezpośredniego URL do obrazka", inline=False)
							embed.add_field(name="subtitle", value=f"Pozwala ci dodać podtytuł", inline=False)
							embed.add_field(name="subtitle_description", value=f"Pozwala ci dodać pod opis ale pamiętaj że pojawi się on tylko wtedy kiedy uzupełnisz wcześniej 'subtitle'", inline=False)
							embed.add_field(name="Komendy które po lewej stronie posiadają znaczek:", value=f":white_check_mark: działają poprawnie.\n<:AAEC_karenThink:981262325061419009> działają ale nie do końca dobrze.\n<:9881_NotHuTao:926276740437921843> Nie działają lub działają nie właściwie.", inline=False)
							await interaction.response.edit_message(embed=embed,view=MyButton())
						else:
							await interaction.response.edit_message(content=f"Nye masz uprawnień do wyświetlania tego zbioru komend {interaction.user.mention}.",view=MyButton())

			view = MySelectView()
			await interaction.response.send_message(view=view, ephemeral = True)

		@tree.command(name = "info", description= "Pokazuje informacje odnośnie serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			class MyButton(View):
					@discord.ui.button(label="Back", style=discord.ButtonStyle.gray)
					async def gray_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=None,embed=None,view=MySelectView())

			class MySelectView(View):
				@discord.ui.select(
					placeholder="Wybierz zbiór komend.",
						options=[

							discord.SelectOption(
								label="UwU",
								description="Uwiecznienie, Wygrań, Uczestników.",
								value="1",
								emoji="<:owo:921393844598239263>",
							),

							discord.SelectOption(
								label="Aktualizacje Otaki-Chan",
								description="Newsy co będą zawierać przyszłe aktualizacje.",
								value="2",
								emoji="<a:Hype:981262325354991716>",
							),

							discord.SelectOption(
								label="Aspiracje serwara.",
								description="Nasze cele do których dążymy.",
								value="3",
								emoji="<:this:1098727934673555477>",
							),

							discord.SelectOption(
								label="Kim jest Otaki/Mani-Chan ?",
								description="Wytłumaczenie kim są i dlaczego są.",
								value="4",
								emoji="<:Hug:1098736403254349865>",
							),

							discord.SelectOption(
								label="Czym jest Context menu ?",
								description="Wytłumaczenie czym jest i jak działa Context menu.",
								value="5",
								emoji="<a:argshow:1099069422821458081>",
							),

							discord.SelectOption(
								label="Gdzie szukać odpowiedzi ?",
								description="Ukazanie gdzie znajdują się odpowiedzi na temat serwera.",
								value="6",
								emoji="<:Peer:1098734415712108635>",
							),
						],)

				async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
					select.disabled = True
					if select.values[0] == "1":

						embed = discord.Embed(title="Uwiecznienie Wygrań Uczestników.", description="", color=0xfceade)
						embed.set_thumbnail(url=config["avatar"])
						embed.add_field(name="Nazwa wydarzenia:", value="Reminiscencjowe Quizium", inline=True)
						embed.add_field(name="Zwyciezca/y:", value="<@403248080193060866>", inline=True)
						embed.set_thumbnail(url = config["avatar"])

						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "2":

						embed = discord.Embed(title="Co zawita do nas w przyszłości ?", description="Wymienione w kolejności priorytetowej.", color=0xfceade)
						embed.add_field(name="1. EcoRpg", value=f"Jest to rozbudowany projekt na Otaki-chan polegającym na stworzeniu gry w stylu rpg z domieszkami economy.", inline=False)
						embed.set_thumbnail(url = config["avatar"])
						await interaction.response.edit_message(embed=embed,view=MyButton())
					
					if select.values[0] == "3":

						embed = discord.Embed(title="Aspiracje serwera Otakumani.", description="Przedstawię ci teraz nasze cele do których dążymy, jeśli będziesz chciał nas wspomóc z realizacją celów/celu napisz do któregoś z nas: <@394162972957605890>,<@277119816043724801>,<@416324164543184907>", color=0xfceade)
						embed.add_field(name="Poszukujemy nowszych:", value=f"Icon Otaki/Mani-Chan, Icon serwera, Banerów serwra.", inline=False)
						embed.add_field(name="Potrzebujemy:", value=f"Loga, Rysownika/Rysowniczki, Strony serwera.", inline=False)
						embed.add_field(name="Usilnie realizujemy:", value=f"Serwerowe RP, Osiągniecie 500 osób na serwerze, Projekt EcpRpg.", inline=False)
						embed.set_thumbnail(url = config["avatar"])
						embed.set_image(url="https://i.postimg.cc/x8vP059p/wp5815954.webp")
						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "4":

						embed = discord.Embed(title="Otaki-Chan oraz Mani-chan.", description="Są to maskotki serwera stworzone przez <@394162972957605890> które pełnią role administracyjne, promujące serwer, oraz zabawowe ich nazwy wzięły się z rozbicia nazwy serwera na dwa człony Otaku oraz Mania po czym przerobienia ich na dziewczęce imiona i tak powstały nazwy <@796459757506134016> z Otaku i <@970417320717615134> z Mania. Jeśli chodzi o ich zarys osobowościowy pojawi się ona w przyszłości, a i wypadało by zaznaczyć czemu Mani-Chan pojawia się sporadycznie online wynika to z faktu bycia przez nią testerko", color=0xfceade)
						embed.set_thumbnail(url = config["avatar"])
						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "5":

						embed = discord.Embed(title="Context menu:", description="Jest to drugi sposób na używanie komend Otaki-Chan żeby wywołać context menu należy kliknąć prawym przyciskiem myszy na uczestnika po czym przejechać do opcji aplikacje i powinniśmy ujrzeć nasze komendy które możemy ujrzeć.", color=0xfceade)
						embed.set_image(url="https://i.postimg.cc/R0FRBqD8/image.png")
						embed.set_thumbnail(url = config["avatar"])
						await interaction.response.edit_message(embed=embed,view=MyButton())

					if select.values[0] == "6":

						embed = discord.Embed(title="Informacje:", description="", color=0xfceade)
						embed.add_field(name="Główne:", value=f"Wszelakie obwieszczenia związane z działaniami, zasadami i wytłumaczeniami na temat ról znajdziesz na kanale \n<#926305651968315393>", inline=False)
						embed.add_field(name="Społecznościowe:", value=f"Adnotacje społecznościowe takie jak wydarzenia pojawiają się w zakładce wydarzenia pod celem serwera a inne wieści znajdziesz po wpisaniu komendy /info", inline=False)
						embed.add_field(name="Komendowe:", value=f"Wskazówki co do działania komend znajdziesz po wpisaniu /help wyświetlą ci się wszystkie zbiory komend jak i co robią poszczególne z nich.", inline=False)
						embed.set_thumbnail(url = config["avatar"])
						await interaction.response.edit_message(embed=embed,view=MyButton())
					
			view = MySelectView()
			await interaction.response.send_message(view=view, ephemeral = True)

		@tree.command(name = "avatar", description= "Pozwala ci zobaczyć avatar wybranej przez ciebie osoby..", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if interaction.channel == channel or interaction.channel == mchannel:
				class MySelectView(View):
					@discord.ui.select(
						placeholder="Wybierz avatar.",
							options=[

								discord.SelectOption(
									label="Główny",
									value="1",
								),

								discord.SelectOption(
									label="Serwerowy",
									value="2",
								),
							],)
					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":
							await interaction.response.edit_message(content=f"{member.avatar}",view=None)

						if select.values[0] == "2":
							await interaction.response.edit_message(content=f"{member.guild_avatar}",view=None)

				view = MySelectView()
				await interaction.response.send_message(view=view, ephemeral = True)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "ping", description= "Pokazuję opóźnienie między tobą a discordem.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if interaction.channel == channel or interaction.channel == mchannel:
				embed = discord.Embed(color=0xfceade)
				embed.add_field(name="Opóźnienie api discorda:", value=str(round(client.latency * 1000)),  inline=False) 
				await interaction.response.send_message(embed=embed, ephemeral = False)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "sp", description= "Pozwala ci na usuwanie dużej ilości wiadomości na raz.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, amount: int):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				await interaction.response.send_message(f"Usunięto {amount} wiadomości", ephemeral = True)
				await interaction.channel.purge(limit=amount)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "pytania", description= "Tą komendą możesz zadać mi pytanie.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, tresc: str):
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if  interaction.channel == channel:
				responses = ["Czy mógłbyś zadać mi pytanie ponownie, bo nie dosłyszałam.","BEZ WĄTPIENIA TAK.","BEZ WĄTPIENIA NIE.","Zdecydowanie TAK.","Zdecydowanie NIE.","Najprawdopodobniej nie.","Najprawdopodobniej tak.","Ahh, Nie.","Ahh, Tak.","<:5163gchemoji13yes:926276739439669318>","<:emoji_6:921392219343171594>","taaaaaaak.","nieeeeeee.","Jest mi naprawdę przykro, że zadajesz mi takie pytanie <:emoji_16:921393487025422357>","Nie jestem pewna.","Chciałabym powiedzieć TAK, ale wszystko wskazuje na NIE.","Chciałabym powiedzieć NIE, ale wszystko wskazuje na TAK.","Muszę dłużej nad tym pomyśleć.","Nie licz na to.","Nie moge teraz powiedzieć.","Znaki na niebie mówią Nie.","Znaki na niebie mówią Tak.","Jakby się nad tym zastanowić Tak","Jakby się nad tym zastanowić Nie","Spytaj się kogoś innego.","Czemu zadajesz te pytanie akurat mi.","Możliwe.","Wydaje mi się że znam odpowiedź na twoje pytanie ale jakoś nie jestem przekonana czy chce ci mówić.","Daj mi spokój, jestem zmęczona.","Chyba tak.","Zapytaj moją młodszą siostrę.","Oczywiście że tak.","Oczywiście że nie.","Patrząc na ciebie zdecydowanie NIE.","Patrząc na ciebie zdecydowanie TAK.","Reasumując wszystkie aspekty kwintesencji tematu, dochodzę do fundamentalnej konkluzji, TAK.","Reasumując wszystkie aspekty kwintesencji tematu, dochodzę do fundamentalnej konkluzji, NIE.","Chyba nie."]
				embed = discord.Embed(title="Pytanie:", description=f"{tresc}", color=0xfceade)
				embed.set_thumbnail(url=config["avatar"])
				embed.add_field(name="Odpowiedź:", value=f"{random.choice(responses)}", inline=False)
				await interaction.response.send_message(embed=embed, ephemeral = False)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "otaki", description= "Pozwala na porozumiewanie się prze zemnie.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, channels: discord.TextChannel, tresc: str):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				await channels.send(f"{tresc}") 
				await interaction.response.send_message(f"{tresc}", ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "ny", description= "Wysyła zbiory pytań.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, channels: discord.TextChannel):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MySelectView(View):
					@discord.ui.select(
						placeholder="Zbiór pytań.",
							options=[
								discord.SelectOption(
									label="Ny",
									description="Podstawowe pytania.",
									value="1",
								),

								discord.SelectOption(
									label="Ny+",
									description="Dodatkowe pytania.",
									value="2",
								),

								discord.SelectOption(
									label="Ny++",
									description="Ekstremalne pytania.",
									value="3",
								),
							],)
			
					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True
						if select.values[0] == "1":

							embed = discord.Embed(title="Hej, Jestem Otaki-chan.", description="Zadam ci kilka pytań. Jeśli nie chcesz odpowiadać na jakieś pytanie to nic nie szkodzi, ale mają one na celu pomóc nam cię poznać i mieć o czym z tobą porozmawiać.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name="Pytanie Pierwsze", value="Czy grasz w jakieś gry, jeśli tak to w jakie?", inline=False)
							embed.add_field(name="Pytanie Drugie", value="Czy oglądasz anime, jeśli tak to jakie ?", inline=False)
							embed.add_field(name="Pytanie Trzecie", value="Czy masz jakieś zainteresowania, jeśli tak to jakie ?", inline=False)
							embed.add_field(name="Pytanie Czwarte", value=f"Jak się nazywasz ? Nie musisz tego podawać jak nie chcesz!", inline=False)
							embed.add_field(name="Pytanie Piąte", value=f"Ile masz lat ? Nie musisz tego podawać jak nie chcesz!", inline=False)
							embed.add_field(name="Pytanie Szóste", value=f"Jeśli zdecydowałeś się nie odpowiadać na pytanie czwarte. Powiedz jak mamy się do ciebie zwracać ?", inline=False)
							embed.add_field(name="Informacje",value="Odpowiedzi na powyższe pytania wyślij tutaj na chacie, ale jeśli masz ochotę na więcej pytań tylko tym razem dziwniejszych poproś o to Administracje.", inline=False)
							await interaction.response.edit_message(content="Zbiór pytań został wysłany.",view=None)
							await channels.send(embed=embed)

						if select.values[0] == "2":

							embed = discord.Embed(title="To ja Otaki-chan.", description="Mam dla ciebie więcej pytań, miłego odpowiadania <:emoji_5:921392177098137600>.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name="Pytanie Pierwsze", value="Jaki jest twój ulubiony kolor ?", inline=False)
							embed.add_field(name="Pytanie Drugie", value="Gdzie mieszkasz ? Nie musisz tego podawać jak nie chcesz!", inline=False)
							embed.add_field(name="Pytanie Trzecie", value="Jaki posiadasz znak zodiaku ?", inline=False)
							embed.add_field(name="Pytanie Czwarte", value=f"Ulubiona przekąska ?", inline=False)
							embed.add_field(name="Pytanie Piąte", value=f"jakie jest twoje ulubione zwierze i dlaczego ?", inline=False)
							embed.add_field(name="Pytanie Szóste", value=f"Na co wydajesz najwięcej pieniędzy ?", inline=False)
							embed.add_field(name="Pytanie Siódme", value=f"Jak opisałbyś siebie w 3 słowach ?", inline=False)
							embed.add_field(name="Pytanie Ósme", value=f"Czy masz czyste sumienie ?", inline=False)
							embed.add_field(name="Pytanie Dziewiąte", value=f"Jaka jest twoja ulubiona piosenka ?", inline=False)
							embed.add_field(name="Pytanie Dziesiąte", value=f"Czy masz rodzeństwo ?", inline=False)
							embed.add_field(name="Pytanie Jedenaste", value=f"Czy lubisz ostre jedzenie ?", inline=False)
							embed.add_field(name="Pytanie Dwunaste", value=f"Jaki jest twój typ osobowości ?", inline=False)
							embed.add_field(name="Informacje",value="Odpowiedzi na powyższe pytania wyślij tutaj na chacie. Ale jeżeli masz ochotę na tym razem EKSTREMALNIE więcej pytań, poproś o to Administracje.", inline=False)
							await interaction.response.edit_message(content="Zbiór pytań został wysłany.",view=None)
							await channels.send(embed=embed)

						if select.values[0] == "3":
							embed = discord.Embed(title="To ja Otaki-chan.", description="Mam dla ciebie Ekstremalne pytania, miłego odpowiadania.", color=0xfceade)
							embed.set_thumbnail(url=config["avatar"])
							embed.add_field(name="Ekstremalne Pytanie Pierwsze", value="Jakie są twoje Fetysze ?", inline=False)
							embed.add_field(name="Ekstremalne Pytanie Drugie", value="Jakie są twoje najbardziej wstydliwe sekrety ?", inline=False)
							embed.add_field(name="Ekstremalne Pytanie Trzecie", value="Czy jesteś Rasistą ?", inline=False)
							embed.add_field(name="Ekstremalne Pytanie Czwarte", value=f"Jaka jest twoja najbardziej niezręczna sytuacja ?", inline=False)
							embed.add_field(name="Informacje",value="Odpowiedzi na powyższe pytania wyślij tutaj na chacie, Na ten momęnt to najbardziej Ekstremalne pytania.", inline=False)
							await interaction.response.edit_message(content="Zbiór pytań został wysłany.",view=None)
							await channels.send(embed=embed)

				view = MySelectView()
				await interaction.response.send_message(view=view, ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "kiss", description= "Pozwala ci pocałować wybrano przez ciebie osobę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, od: discord.Member, dla: discord.Member):
			kissa = ["https://i.postimg.cc/W1pK9mR7/aho-girl.gif","https://i.postimg.cc/7Y18tY5q/anime-ano.gif","https://i.postimg.cc/13zC096C/anime-hug.gif","https://i.postimg.cc/x1FstW30/anime-kiss.gif","https://i.postimg.cc/pd46Xgm0/anime-kiss-1.gif","https://i.postimg.cc/8k6VWbDJ/anime-kiss-2.gif","https://i.postimg.cc/MGTCG7dG/anime-kiss-3.gif","https://i.postimg.cc/rFN3CnHm/anime-kissing.gif","https://i.postimg.cc/HW5fjs4b/anime-love.gif","https://i.postimg.cc/Fzt8G2mf/anime-sheep.gif","https://i.postimg.cc/SxZPHXkb/anime-sweet.gif","https://i.postimg.cc/fyxFPBT8/blowkiss-anime.gif","https://i.postimg.cc/FzZpcqKX/cute-anime.gif","https://i.postimg.cc/3JTzG5nV/cute-girls-cheek-kissing.gif","https://i.postimg.cc/2yf9nhFh/discord-anime.gif","https://i.postimg.cc/B6PRTqW9/engage-kiss-anime-kiss.gif","https://i.postimg.cc/YSsJLvsz/girl-anime.gif","https://i.postimg.cc/6pYswjVS/kiss.gif","https://i.postimg.cc/CxFy3T8k/kiss-1.gif","https://i.postimg.cc/jqQZGW43/kiss-anime.gif","https://i.postimg.cc/8C2ZVMY9/kiss-girls.gif","https://i.postimg.cc/prYGCrq7/kiss-senran-kagura.gif","https://i.postimg.cc/1tDJR4ht/kissing.gif","https://i.postimg.cc/jjL1TsSw/love-couples.gif","https://i.postimg.cc/yYLn8w5F/love-you-kiss.gif","https://i.postimg.cc/TY0NWyy5/naruko-anime.gif","https://i.postimg.cc/FsNnRbKQ/nekopara-kiss.gif","https://i.postimg.cc/7hDX5DwN/rakudai-kishi-kiss.gif","https://i.postimg.cc/yNgL5vL0/rascal-does-not-dream-of-bunny-girl-senpai-mai-sakurajima.gif","https://i.postimg.cc/FsrDm9Pr/shy-anime-blush.gif","https://i.postimg.cc/MKJJYjKs/test.gif"]
			embed = discord.Embed(title=f"Uczestnik {od.name} całuje {dla.name}", description=f"", color=0xfceade)
			embed.set_image(url=f"{random.choice(kissa)}")
			await interaction.response.send_message(embed=embed, ephemeral = False)

		@tree.command(name = "hug", description= "Pozwala ci przytulić wybrano przez ciebie osobę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, od: discord.Member, dla: discord.Member):
			kissa = ["https://i.postimg.cc/R0kvrhJF/anime-cute.gif","https://i.postimg.cc/DzHw25H7/anime-hug.gif","https://i.postimg.cc/6pQWnDN9/catgirl-hug.gif","https://i.postimg.cc/NFYYMn4v/girl-anime.gif","https://i.postimg.cc/bwYJLZ1f/hug.gif","https://i.postimg.cc/3xLwq3Z4/hug-1.gif","https://i.postimg.cc/1RcsT9mm/hug-ana.gif","https://i.postimg.cc/L5TSZVCY/hug-anime.gif","https://i.postimg.cc/k4SXDKPK/hug-anime-1.gif","https://i.postimg.cc/9XGQhdpj/hug-anime-2.gif","https://i.postimg.cc/rwY8JQ85/hugs.gif","https://i.postimg.cc/VvBfWw6N/kitsune-upload-anime.gif","https://i.postimg.cc/Y0w2F0tV/kitsune-upload-anime-1.gif","https://i.postimg.cc/G3S1X9f9/h1.gif","https://i.postimg.cc/XY9SNLYy/h2.gif","https://i.postimg.cc/yNBqDRDp/h3.gif","https://i.postimg.cc/VLrPpmyg/h4.gif","https://i.postimg.cc/xdPwMdHf/h5.gif","https://i.postimg.cc/fLT6Khjx/h6.gif","https://i.postimg.cc/MHXJW8nW/h7.gif","https://i.postimg.cc/KYybtVHN/h8.gif","https://i.postimg.cc/gJgPF0kS/h9.gif","https://i.postimg.cc/VLpmk592/h10.gif","https://i.postimg.cc/R0QBddrz/h11.gif","https://i.postimg.cc/XJj0z53B/h12.gif","https://i.postimg.cc/T3bGLGC1/h13.gif","https://i.postimg.cc/CLzw0b8j/h14.gif","https://i.postimg.cc/WzKLzfZ0/h15.gif","https://i.postimg.cc/9F6HjKCh/h16.gif","https://i.postimg.cc/B624J32C/kobayashi-dragon-maid-anime-hug.gif"]
			embed = discord.Embed(title=f"Uczestnik {od.name} przytula {dla.name}", description=f"", color=0xfceade)
			embed.set_image(url=f"{random.choice(kissa)}")
			await interaction.response.send_message(embed=embed, ephemeral = False)

		@tree.command(name = "pat", description= "Pozwala ci pogłaskać wybrano przez ciebie osobę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, od: discord.Member, dla: discord.Member):
			kissa = ["https://i.postimg.cc/YS0yNBRz/aharen-aharen-san.gif","https://i.postimg.cc/1tLT57pc/anime-girl.gif","https://i.postimg.cc/pVcb3khT/anime-girl-1.gif","https://i.postimg.cc/hjSRR51J/anime-girl-pet.gif","https://i.postimg.cc/GpPnNCGw/anime-good-girl.gif","https://i.postimg.cc/XqdPZKLM/anime-head-pat.gif","https://i.postimg.cc/pTnG7Qg9/anime-pat.gif","https://i.postimg.cc/ryr3Yckh/anime-pat-1.gif","https://i.postimg.cc/bvYfK5TZ/anime-pat-2.gif","https://i.postimg.cc/XqphVSGv/anime-pat-3.gif","https://i.postimg.cc/qM9fvRGH/anime-pat-4.gif","https://i.postimg.cc/D0kjKJTx/eromanga-sensei-pat-pat-pat.gif","https://i.postimg.cc/hv5kxPWx/fantasista-doll-anime.gif","https://i.postimg.cc/W3DCVcJ1/kaede-azusagawa-kaede.gif","https://i.postimg.cc/fbPqBqgn/mai-sakurajima.gif","https://i.postimg.cc/nh0PQh4L/rika-higurashi.gif","https://i.postimg.cc/Z5R42BN2/p1.gif","https://i.postimg.cc/7h9rQwZq/p2.gif","https://i.postimg.cc/2yrfwVmH/p3.gif","https://i.postimg.cc/bJQhkQXD/p4.gif","https://i.postimg.cc/rwPMkVCm/p5.gif","https://i.postimg.cc/gJ9pxg7b/p6.gif","https://i.postimg.cc/28TC0F1n/p7.gif","https://i.postimg.cc/L4t91MRC/p8.gif","https://i.postimg.cc/3w07rsnZ/p9.gif","https://i.postimg.cc/gkwFpR8K/senko-pat.gif","https://i.postimg.cc/mkkxt1qB/uwu-pats.gif"]
			embed = discord.Embed(title=f"Uczestnik {od.name} głaszcze {dla.name}", description=f"", color=0xfceade)
			embed.set_image(url=f"{random.choice(kissa)}")
			await interaction.response.send_message(embed=embed, ephemeral = False)
		
		@tree.command(name = "handshake", description= "Pozwala ci uścisnąć dłoń wybranej przez ciebie osobie.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, od: discord.Member, dla: discord.Member):
			kissa = ["https://i.postimg.cc/W31B14hc/anime-handshake.gif","https://i.postimg.cc/85kSfHX3/anime-handshake-1.gif","https://i.postimg.cc/Dz6VhGfc/ban-meliodas.gif","https://i.postimg.cc/LXyMt1rs/bandori-bangdream.gif","https://i.postimg.cc/2SB8C2g7/bna-nazuna.gif","https://i.postimg.cc/J064zg1P/dab-mp100.gif","https://i.postimg.cc/L658bHT7/dyar-and.gif","https://i.postimg.cc/2S4RHJPM/fairy-tail-anime.gif","https://i.postimg.cc/FKyrL1rf/gundam-mobilesuitgundam.gif","https://i.postimg.cc/xjx0Hw2P/hand-shake-truce.gif","https://i.postimg.cc/50Jt7L7q/high-five-fist-bump.gif","https://i.postimg.cc/hPYtFHZG/infinite-stratos.gif","https://i.postimg.cc/5yHD8kBP/jojo-kakyoin.gif","https://i.postimg.cc/jj0q2yb0/link-click-shiguang-daili-ren.gif","https://i.postimg.cc/XYM6k3D9/makeout-handshake.gif","https://i.postimg.cc/Y0ZKVw2K/martin-mystery-billy.gif","https://i.postimg.cc/QCRwmkSj/nichijou-anime.gif","https://i.postimg.cc/h4wkKcnN/portgas-d-ace-ace.gif","https://i.postimg.cc/Z53ZG0yf/professor-layton-hand-shake.gif","https://i.postimg.cc/B6zVZcr2/sao-alicization.gif","https://i.postimg.cc/cJ0qPhWH/totally-agree-fist-bump.gif"]
			embed = discord.Embed(title=f"{od.name} uściska dłoń {dla.name}", description=f"", color=0xfceade)
			embed.set_image(url=f"{random.choice(kissa)}")
			await interaction.response.send_message(embed=embed, ephemeral = False)

		@tree.command(name = "slap", description= "Pozwala ci uderzyć wybrano przez ciebie osobę.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, od: discord.Member, dla: discord.Member):
			kissa = ["https://i.postimg.cc/sgYLRgSL/anime-girl.gif","https://i.postimg.cc/QNnG6Ckk/anya-forger-anya-spy-x-family-anime.gif","https://i.postimg.cc/zvQs32XP/asobi-asobase-anime.gif","https://i.postimg.cc/tTBQG40b/chikku-neesan-girl-hit-wall.gif","https://i.postimg.cc/vTDRYwMV/gintama-slap.gif","https://i.postimg.cc/43bRw1Bm/hyouka-good.gif","https://i.postimg.cc/wvq8rsGF/joe-flacco.gif","https://i.postimg.cc/zXsmrQQy/kokoro-connect-slap-anime.gif","https://i.postimg.cc/VLry2wKy/rei-rei-ayanami.gif","https://i.postimg.cc/t4WKC502/saki-saki-mukai-naoya.gif","https://i.postimg.cc/KYbdKMxF/slap-1.gif","https://i.postimg.cc/6QhFCppZ/slap-2.gif","https://i.postimg.cc/MHn4k0b0/slap-3.gif","https://i.postimg.cc/xCx7FpHT/slap-4.gif","https://i.postimg.cc/9MFKbHDn/slap-5.gif","ahttps://i.postimg.cc/Fzw6hfDM/slap-bet-chisa-iori.gif--","https://i.postimg.cc/FF68yqNT/slap-bucket.gif","https://i.postimg.cc/15NTJHzs/slap-hit.gif","https://i.postimg.cc/CxT2tqZD/slapping-take-that.gif"]
			embed = discord.Embed(title=f"Uczestnik {od.name} uderza {dla.name}", description=f"", color=0xfceade)
			embed.set_image(url=f"{random.choice(kissa)}")
			await interaction.response.send_message(embed=embed, ephemeral = False)

		@tree.command(name = "donacje", description= "Za pomocą tej komendy możesz mi ofiarować trochę radości.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if interaction.channel == channel or interaction.channel == mchannel:
				button = Button(label="Donacje", url="https://tipply.pl/u/kiriu")
				view = View()
				view.add_item(button)
				responses = ["https://i.postimg.cc/Kz959kcY/touhou.gif",
							"https://i.postimg.cc/sxq4rkhd/touhou-cookie.gif",
							"https://i.postimg.cc/nc91khyH/touhou-reimu.gif",
							"https://i.postimg.cc/Tw29qq6S/unknown.png",
							"https://i.postimg.cc/ZRdfgpHj/ep00000.gif",
							"https://i.postimg.cc/CKtPmmGz/hataage-kemono-michi-shigure.gif",
							"https://i.postimg.cc/43n26rhD/kupo-gossip.gif",
							"https://i.postimg.cc/DwxYb2mQ/money.gif",
							"https://i.postimg.cc/4yR8TyFG/shut-up-take-my-money.gif",
							"https://i.postimg.cc/6qyfFWTf/yay-yeah.gif"]

				embed = discord.Embed(title=f"Donacje", description=f"Jeśli chcesz mi podziękować albo wspomóc lub po prostu postawić herbatkę ten przycisk pozwoli ci mnie zdonejtować.", color=0xfceade)
				embed.set_image(url=f"{random.choice(responses)}")
				await interaction.response.send_message(embed=embed,view=view,ephemeral = False)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "creation", description= "Służy do kreacji ról do wybierania.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, channels: discord.TextChannel, title: str, emoji: str, role: discord.Role,message: str):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				embed = discord.Embed(title=title, description=message, color=0xfceade)
				msg = await channels.send(embed=embed)
				await msg.add_reaction(emoji)
				await interaction.response.send_message("Pomyślnie stworzono", ephemeral = True)
				
				with open(data_role_path) as json_file:
					data = json.load(json_file)

					new_react_role = {
						"role_name":role.name,
						"role_id":role.id,
						"emoji":emoji,
						"message_id":msg.id
					}

					data.append(new_react_role)

				with open(data_role_path,"w") as j:
					json.dump(data,j,indent=4)
		
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.", ephemeral = True)

		@tree.command(name = "kolorkowo", description= "Wywołuje paletę kolorów.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):

			server_id = 698522294414344232
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				class MyView(View):
						@discord.ui.button(label="1", style=discord.ButtonStyle.primary)
						async def primary1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927889321929875467))#Bright Blue
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="2", style=discord.ButtonStyle.primary)
						async def primary2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927890415334596628))#Medium Aqua Marine
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="3", style=discord.ButtonStyle.primary)
						async def primary3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927890916738478120))#Forest Green
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="4", style=discord.ButtonStyle.primary)
						async def primary4_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927891029661720606))#Green Apple
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="5", style=discord.ButtonStyle.primary)
						async def primary5_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927891257139802193))#Yellow
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="6", style=discord.ButtonStyle.primary)
						async def primary6_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927891380980830238))#Beer
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="7", style=discord.ButtonStyle.primary)
						async def primary7_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927891465454096395))#Brown Sugar
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="8", style=discord.ButtonStyle.primary)
						async def primary8_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927892009140768798))#Neon Orange
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="9", style=discord.ButtonStyle.primary)
						async def primary9_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927892168750796810))#Red
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)


						@discord.ui.button(label="10", style=discord.ButtonStyle.primary)
						async def primary10_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927894148164517929))#Aussie Sunset
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)


						@discord.ui.button(label="11", style=discord.ButtonStyle.primary)
						async def primary11_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927892425920364564))#Plum Velvet
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)


						@discord.ui.button(label="12", style=discord.ButtonStyle.primary)
						async def primary12_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927892737733324811))#Neon Pink
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="13", style=discord.ButtonStyle.primary)
						async def primary13_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927892571370438707))#Pastel Pink
							await interaction.user.add_roles(role)
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="14", style=discord.ButtonStyle.primary)
						async def primary14_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							role = discord.utils.get(client.get_guild(server_id).roles, id=(927893071423754310))#White
							role2 = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#White
							await interaction.user.add_roles(role2)
							await interaction.user.add_roles(role)
							await interaction.response.send_message(f"Pomyślnie wybrano kolor {role}",ephemeral = True)

						@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							white = discord.utils.get(client.get_guild(server_id).roles, id=(927893071423754310))#White
							Pastel_Pink = discord.utils.get(client.get_guild(server_id).roles, id=(927892571370438707))#Pastel Pink
							Neon_Pink = discord.utils.get(client.get_guild(server_id).roles, id=(927892737733324811))#Neon Pink
							Plum_Velvet = discord.utils.get(client.get_guild(server_id).roles, id=(927892425920364564))#Plum Velvet
							Aussie_Sunset = discord.utils.get(client.get_guild(server_id).roles, id=(927894148164517929))#Aussie Sunset
							Red = discord.utils.get(client.get_guild(server_id).roles, id=(927892168750796810))#Red
							Neon_Orange = discord.utils.get(client.get_guild(server_id).roles, id=(927892009140768798))#Neon Orange
							Brown_Sugar = discord.utils.get(client.get_guild(server_id).roles, id=(927891465454096395))#Brown Sugar
							Beer = discord.utils.get(client.get_guild(server_id).roles, id=(927891380980830238))#Beer
							Yellow = discord.utils.get(client.get_guild(server_id).roles, id=(927891257139802193))#Yellow
							Green_Apple = discord.utils.get(client.get_guild(server_id).roles, id=(927891029661720606))#Green Apple
							Forest_Green = discord.utils.get(client.get_guild(server_id).roles, id=(927890916738478120))#Forest Green
							Medium_Aqua_Marine = discord.utils.get(client.get_guild(server_id).roles, id=(927890415334596628))#Medium Aqua Marine
							Bright_Blue = discord.utils.get(client.get_guild(server_id).roles, id=(927889321929875467))#Bright Blue
							if white in interaction.user.roles:
								await interaction.user.remove_roles(white)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {white}.",ephemeral = True)

							elif Pastel_Pink in interaction.user.roles:
								await interaction.user.remove_roles(Pastel_Pink)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Pastel_Pink}.",ephemeral = True)

							elif Neon_Pink in interaction.user.roles:
								await interaction.user.remove_roles(Neon_Pink)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Neon_Pink}.",ephemeral = True)

							elif Plum_Velvet in interaction.user.roles:
								await interaction.user.remove_roles(Plum_Velvet)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Plum_Velvet}.",ephemeral = True)

							elif Aussie_Sunset in interaction.user.roles:
								await interaction.user.remove_roles(Aussie_Sunset)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Aussie_Sunset}.",ephemeral = True)

							elif Red in interaction.user.roles:
								await interaction.user.remove_roles(Red)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Red}.",ephemeral = True)

							elif Neon_Orange in interaction.user.roles:
								await interaction.user.remove_roles(Neon_Orange)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Neon_Orange}.",ephemeral = True)
							
							elif Brown_Sugar in interaction.user.roles:
								await interaction.user.remove_roles(Brown_Sugar)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Brown_Sugar}.",ephemeral = True)

							elif Beer in interaction.user.roles:
								await interaction.user.remove_roles(Beer)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Beer}.",ephemeral = True)

							elif Yellow in interaction.user.roles:
								await interaction.user.remove_roles(Yellow)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Yellow}.",ephemeral = True)
							
							elif Green_Apple in interaction.user.roles:
								await interaction.user.remove_roles(Green_Apple)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Green_Apple}.",ephemeral = True)

							elif Forest_Green in interaction.user.roles:
								await interaction.user.remove_roles(Forest_Green)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Forest_Green}.",ephemeral = True)

							elif Medium_Aqua_Marine in interaction.user.roles:
								await interaction.user.remove_roles(Medium_Aqua_Marine)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Medium_Aqua_Marine}.",ephemeral = True)
							
							elif Bright_Blue in interaction.user.roles:
								await interaction.user.remove_roles(Bright_Blue)
								await interaction.response.send_message(f"Pomyślnie wyczyszczono {Bright_Blue}.",ephemeral = True)
							
							else:
								role = discord.utils.get(client.get_guild(server_id).roles, id=(1091875414420508722))#kolorek
								await interaction.user.remove_roles(role)
								await interaction.response.send_message(f"Już wyczyściłeś wszystkie kolory {interaction.user.mention}",ephemeral = True)

				embed = discord.Embed(title="Kolorkowo", description="**1.<@&927889321929875467>**\n**2.<@&927890415334596628>**\n**3.<@&927890916738478120>**\n**4.<@&927891029661720606>**\n**5.<@&927891257139802193>**\n**6.<@&927891380980830238>**\n**7.<@&927891465454096395>**\n**8.<@&927892009140768798>**\n**9.<@&927892168750796810>**\n**10.<@&927894148164517929>**\n**11.<@&927892425920364564>**\n**12.<@&927892737733324811>**\n**13.<@&927892571370438707>**\n**14.<@&927893071423754310>**\n**X.__Usuwa obecnie wybrany kolor.__**", color=0xfceade)
				embed.set_thumbnail(url="https://i.postimg.cc/dQxjNx3B/e8637a5b750d32dad7a3f7da273ee134.png")
				embed.set_footer(text="Żeby wybrać kolorek należy kliknąć przycisk z odpowiadającym\nmu numerkiem. Natomiast żeby go usunąć na leży wybrać ostatni przycisk.")

				view = MyView()
				await interaction.response.send_message(embed=embed, view=view ,ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "dice", description= "Pozwala ci rzucić wybraną przez siebie kostką.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, dice: int, throw: int, bonus: int=None):
			mchannel = discord.utils.get(interaction.guild.channels, id = 922781362514190386)
			channel = discord.utils.get(interaction.guild.channels, id = 925191790284406805)
			if interaction.channel == channel or interaction.channel == mchannel:
				scores = []
				if bonus==None:
					for i in range(throw):
						wynik = random.randint(1,dice)
						scores.append(wynik)
					embed = discord.Embed(title=f"{interaction.user.name} rzuca d{dice}", description=f"Rzuty: {throw}", color=0xfceade)
					embed.add_field(name="Wyniki:", value=f"{scores}", inline=False)
					embed.set_thumbnail(url=f"{interaction.user.avatar}")
					await interaction.response.send_message(embed=embed, ephemeral = False)

				else:
					wynik = random.randint(1,dice)
					sum=wynik+bonus
					embed = discord.Embed(title=f"{interaction.user.name} rzuca d{dice}", description=f"Rzuty: 1", color=0xfceade)
					embed.add_field(name="Wynik:", value=f"{wynik} + {bonus}", inline=False)
					embed.set_thumbnail(url=f"{interaction.user.avatar}")
					embed.set_footer(text=f"Suma: {sum}")
					await interaction.response.send_message(embed=embed, ephemeral = False)
			else:
				await interaction.response.send_message(f"Hej {interaction.user.mention}, Nye jesteś na kanale {channel.mention}.",ephemeral = True)

		@tree.command(name = "embeds", description= "Pozwala ci tworzyć własne wiadomości embedowe.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, title: str, description: str, subtitle: str = None, subtitle_description: str = None, footer: str = None, avatar:discord.Member=None, image: str = None):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				embed = discord.Embed(title=f"{title}", description=f"{description}", color=0xfceade)
				if avatar != None:
					embed.set_thumbnail(url=f"{avatar.avatar}")
				
				if subtitle != None:
					if subtitle_description != None:
						embed.add_field(name=f"{subtitle}", value=f"{subtitle_description}", inline=False)
					else:
						embed.add_field(name=f"{subtitle}", value=f"", inline=False)

				if  footer!= None:
					embed.set_footer(text=f"{footer}")

				if  image!= None:
					embed.set_image(url=f"{image}")

				await interaction.response.send_message(embed=embed, ephemeral = False)
				
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

		@tree.command(name = "pong", description= "Pozwala ci na zaproszenie kogoś do wspólnego rzucania piłeczką.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			try:
				channel = await member.create_dm()
				thrower = interaction.user

				class MyPong(View):
					@discord.ui.button(label="PONG", style=discord.ButtonStyle.primary)
					async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await member.create_dm()
						
						await channel.send(f"{interaction.user.mention} PING!", view=MyPing())

						await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await member.create_dm()

						await channel.send(f"{thrower.mention} przerwał rzucanie piłką.", view=None)
						
						await interaction.response.edit_message(content="Zaprzestano rzucania piłką.",embed=None, view=None)

				class MyPing(View):
					@discord.ui.button(label="PING", style=discord.ButtonStyle.primary)
					async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} PING!", view=MyPong())
						
						await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} przerwał rzucanie piłką.", view=None)
						
						await interaction.response.edit_message(content="Zaprzestano rzucania piłką.",embed=None, view=None)

				class MyStart(View):
					@discord.ui.button(label="Przyjmij", style=discord.ButtonStyle.green)
					async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} PING!", view=MyPong())
						
						await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="Odrzuć", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} odmówił wspólnego rzucania piłką.", view=None)
						
						await interaction.response.edit_message(content="Pomyślnie odrzucono zaproszenie rzucania piłeczką.",embed=None, view=None)

				embed = discord.Embed(title=f"{thrower.name} Zaprasza cię do:", description="", color=0xfceade)
				embed.set_thumbnail(url=f"{thrower.avatar}")
				embed.add_field(name=f"Ping Pong", value="Wspólnego rzucania piłką.", inline=False)
				await channel.send(embed=embed, view=MyStart())
				await interaction.response.send_message(f"Pomyślnie rzuconą piłeczkę.", ephemeral = True)
			except:
				await interaction.response.send_message(f"Przykro mi ale uczestnik {member.mention} ma zablokowane otrzymywanie wiadomości.", ephemeral = True)

		@tree.command(name = "vocabulary", description= "Pokaże ci słowniczek Otakumani.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			embed = discord.Embed(title="Słownik Otakumani", description="Słownictwo i definicje w nim zawarte zostało stworzone przez @Kiriu czytając je pamiętaj że nie występują one normalnie w języku polskim i nie ponosi on żadnych konsekwencji w przypadku zachorowania na nyantyzm.", color=0xfceade)
			embed.set_thumbnail(url="https://i.postimg.cc/9QhBnvBK/pfp.png")
			embed.set_image(url="https://i.postimg.cc/cH8bKQKn/anime-girl-reading-books-by-animeart790-df9isfn-fullview.jpg")
			embed.add_field(name="Nyantyzm", value="Określnie humorystyczne które może być użyte jako: choroba, zachowanie, specyficzność, stan psychiczny, wyjątkowość danej osoby. Powstałe w wyniku chęci stworzenia humorzastego określenia na specyficzność, same słowo jest nawiązaniem do słowa autyzm które ma służyć do podkreślenia inności wybijającej się z utartych zestawu zachowań.", inline=False)
			embed.add_field(name="Nyanho", value="zwrot grzecznościowy, nieformalne powitanie, synonim słów: hej, cześć, hi, witaj", inline=False)
			# embed.add_field(name="Debito", value="b", inline=False)
			embed.set_footer(text="Kolejne słówka dojdą gdy opracuję dla nich dobre definicje.")
			
			await interaction.response.send_message(embed=embed,ephemeral = True)

		@tree.command(name = "server_set", description= "Pozwala na zmianę wyglądu serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MySelectView(View):
					@discord.ui.select(
						placeholder="Wybierz wygląd serwera.",
							options=[

								discord.SelectOption(
									label="Domyślny",
									emoji="<:love2:1063248751889743968>",
									value="1",
								),

								discord.SelectOption(
									label="Wiosenny",
									emoji="🌸",
									value="2",
								),

								discord.SelectOption(
									label="Letni",
									emoji="☀️",
									value="3",
								),

								discord.SelectOption(
									label="Jesienny",
									emoji="🍂",
									value="4",
								),

								discord.SelectOption(
									label="Hallowinowy",
									emoji="🎃",
									value="5",
								),

								discord.SelectOption(
									label="Zimowy",
									emoji="☃️",
									value="6",
								),

								discord.SelectOption(
									label="Nowo roczny",
									emoji="🎉",
									value="7",
								),
							],)

					async def select_callback(self, interaction:discord.Integration, select: discord.ui.Select):
						select.disabled = True

						#Pogawędki,Pogawędki+,Modowędki,Otaki-Mani-Chan,spamchat,Muzyka,Memy,Twórczości,Galeria,Archiwa,Techwędki,Helpdesk,Czatowędki,Dyskutowędki,PogawędkiVC,Pogawędki+VC,ModowędkiVC,PograwędkiVC,GawędkiVC,PoznawędkiVC,StreamwędkiVC
						id_channel = [920080200308506676,924519066276859914,922781362514190386,925191790284406805,757956871607812258,698523673333858336,851148738163376198,1063854038636048496,1063876422285938749,959782877464244244,927594576590553108,1081553062319099964,923682859800199168,942133948367122452,942206391433711687,926455091861520384,921517809270411265,698524923659944057,767087869515923466,933815461899038830,962454168512131192]
						#Regulamin i Weryfikacja,Kanały Tekstowe, Dodatkowo, Techniu, Kanały głosowe
						id_channel_category = [927827745814216745,698522294414344233,923679130690674729,1080978917441142824,698522294414344235]

						if select.values[0] == "1":

							name_table =["💬▏pogawędki","💎▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🔰▏otaki-mani-chan","💥▏spamchat","🎵▏muzyka","🃏▏memy","🎴▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🎶▏Pogawędki","💎▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","☕▏Gawędki","👥▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["Regulaminy i Weryfikacje","kanały tekstowe","DODATKOwO","Techniu","Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Domyślny", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/9fwTJ735/Untitled373-2.png")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])

						if select.values[0] == "2":
							
							name_table =["💬▏pogawędki","🌈▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🌾▏otaki-mani-chan","🍃▏spamchat","🎵▏muzyka","🦦▏memy","🌄▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🎋▏Pogawędki","🌈▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","🐣▏Gawędki","🌹▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["🌹Regulaminy i Weryfikacje","🌷kanały tekstowe","🌸DODATKOwO","🌼Techniu","🌺Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Wiosenny", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/05pH96XK/spring.jpg")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])

						if select.values[0] == "3":

							name_table =["💬▏pogawędki","🍊▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🍒▏otaki-mani-chan","⚡▏spamchat","🎵▏muzyka","🌞▏memy","🌅▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🍨▏Pogawędki","🍊▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","⛺▏Gawędki","🍻▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["🍉Regulaminy i Weryfikacje","🍇kanały tekstowe","🥕DODATKOwO","🌽Techniu","🍍Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Letni", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/d3mW6XZj/summer.jpg")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])
						
						if select.values[0] == "4":

							name_table =["💬▏pogawędki","🍁▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🥓▏otaki-mani-chan","🍂▏spamchat","🎵▏muzyka","🐁▏memy","🌁▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🪁▏Pogawędki","🍁▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","🍷▏Gawędki","🥃▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["💦Regulaminy i Weryfikacje","💨kanały tekstowe","🦔DODATKOwO","🥀Techniu","🦊Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Jesienny", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/kXqYGnL1/autumn.png")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])
						
						if select.values[0] == "5":

							name_table =["💬▏pogawędki","🎃▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🎭▏otaki-mani-chan","👻▏spamchat","🎵▏muzyka","💀▏memy","🌃▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🤡▏Pogawędki","🎃▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","🧛▏Gawędki","🧟▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["🧙Regulaminy i Weryfikacje","🧜 kanały tekstowe","😈DODATKOwO","🧚Techniu","👹Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Hallowinowy", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/4NMMCWcs/hallowin.jpg")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])

						if select.values[0] == "6":

							name_table =["💬▏pogawędki","🧊▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🏒▏otaki-mani-chan","🧤▏spamchat","🎵▏muzyka","🥶▏memy","🏂🏼▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🧣▏Pogawędki","🧊▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","🐻▏Gawędki","⛄▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["🧦Regulaminy i Weryfikacje","🐧kanały tekstowe","🦌DODATKOwO","🐏Techniu","🥾Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Zimowy", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/4NPLhDgJ/winter.png")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])

						if select.values[0] == "7":

							name_table =["💬▏pogawędki","🍾▏pogawędki-𝓹𝓵𝓾𝓼","📝▏modowędki","🥂▏otaki-mani-chan","💫▏spamchat","🎵▏muzyka","🥳▏memy","🎇▏twórczości","📁▏galeria","📝▏archiwa","💻▏techwędki","🔎▏helpdesk","🔇▏czatowędki","📢▏dyskutowędki","🎊▏Pogawędki","🍾▏Pogawędki-𝓹𝓵𝓾𝓼","📝▏Modowędki","🎮▏Pograwędki","🍸▏Gawędki","🎎▏Poznawędki","🎥▏Streamwędki"]
							rang = len(id_channel)

							category_table = ["⭐Regulaminy i Weryfikacje","🎁kanały tekstowe","🏮DODATKOwO","🎐Techniu","🎀Kanały głosowe"]
							rangc = len(id_channel_category)

							embed = discord.Embed(title="Wygląd: Nowo roczny", description=f"Ustawiono pomyślnie", color=0xfceade)
							embed.set_thumbnail(url="https://i.postimg.cc/LszQdRkM/new-year.webp")
							await interaction.response.edit_message(embed=embed,view=None)

							for i in range(rang):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel[i])
								await channel.edit(name=name_table[i])
							
							for i in range(rangc):

								channel = discord.utils.get(interaction.guild.channels, id = id_channel_category[i])
								await channel.edit(name=category_table[i])

				view = MySelectView()
				await interaction.response.send_message(view=view, ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "janken", description= "Pozwala ci na zagranie z kimś w papier, kamień, nożyce.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				try:
					channel = await member.create_dm()
					thrower = interaction.user
					janken = []
					member_point = []
					thrower_point = []

					class MyJanken(View):
						@discord.ui.button(label="paper",emoji="🧻", style=discord.ButtonStyle.gray)
						async def gray1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("a")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="stone",emoji="<:rock:979764802232651856>",style=discord.ButtonStyle.gray)
						async def gray2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("b")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="scissors",emoji="✂️", style=discord.ButtonStyle.gray)
						async def gray3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("c")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)

					class MyJankenTwo(View):
						@discord.ui.button(label="paper",emoji="🧻", style=discord.ButtonStyle.gray)
						async def gray1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"🧻 {member.name}: {len(member_point)}\n\n🧻 {thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"🧻 {member.name}: {len(member_point)}\n\n<:rock:979764802232651856> {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"🧻 {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
						
						@discord.ui.button(label="stone",emoji="<:rock:979764802232651856>",style=discord.ButtonStyle.gray)
						async def gray2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n\n🧻{thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n<:rock:979764802232651856>{thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
						
						@discord.ui.button(label="scissors",emoji="✂️", style=discord.ButtonStyle.gray)
						async def gray3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"✂️ {member.name}: {len(member_point)}\n\n🧻 {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"✂️ {member.name}: {len(member_point)}\n\n<:rock:979764802232651856> {thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"✂️ {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())

					class MyAgian(View):
						@discord.ui.button(label="Again", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{thrower.mention} Again ?", view=MyAgianTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odpowie na twoje zapytanie.",embed=None, view=None)
						
						@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{member.mention} odmówił dalszego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie zakończono gre w papier, kamień, nożyce.",view=None)
					
					class MyAgianTwo(View):
						@discord.ui.button(label="Again", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{thrower.mention} wybierz swój symbol.", view=MyJanken())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							await channel.send(f"{thrower.mention} odmówił dalszego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie zakończono gre w papier, kamień, nożyce.", view=None)

					class MyStart(View):
						@discord.ui.button(label="Przyjmij", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							channel = await thrower.create_dm()

							await channel.send(f"{thrower.mention} wybierz swój symbol.", view=MyJanken())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="Odrzuć", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							channel = await thrower.create_dm()

							await channel.send(f"{member.mention} odmówił wspólnego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie odrzucono zaproszenie gry w papier, kamień, nożyce.",embed=None, view=None)

					embed = discord.Embed(title=f"{thrower.name} Zaprasza cię do:", description="", color=0xfceade)
					embed.set_thumbnail(url=f"{thrower.avatar}")
					embed.add_field(name=f"Janken", value="Wspólnego grania w papier, kamień, nożyce.", inline=False)
					embed.set_footer(text='Komunikat: "Ta czynność się nie powiodła"\nOznacza wygaśniecie zaproszenia/.')
					
					await channel.send(embed=embed, view=MyStart())
					await interaction.response.send_message(f"Pomyślnie wysłano zaproszenie.", ephemeral = True)

				except:
					await interaction.response.send_message(f"Przykro mi ale uczestnik {member.mention} ma zablokowane otrzymywanie wiadomości.", ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

# Context Menu commands

		@tree.context_menu(name = "pong", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			try:
				channel = await member.create_dm()
				thrower = interaction.user

				class MyPong(View):
					@discord.ui.button(label="PONG", style=discord.ButtonStyle.primary)
					async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await member.create_dm()
						
						await channel.send(f"{interaction.user.mention} PING!", view=MyPing())

						await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await member.create_dm()

						await channel.send(f"{thrower.mention} przerwał rzucanie piłką.", view=None)
						
						await interaction.response.edit_message(content="Zaprzestano rzucania piłką.",embed=None, view=None)

				class MyPing(View):
					@discord.ui.button(label="PING", style=discord.ButtonStyle.primary)
					async def primary_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} PING!", view=MyPong())
						
						await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} przerwał rzucanie piłką.", view=None)
						
						await interaction.response.edit_message(content="Zaprzestano rzucania piłką.",embed=None, view=None)

				class MyStart(View):
					@discord.ui.button(label="Przyjmij", style=discord.ButtonStyle.green)
					async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} PING!", view=MyPong())
						
						await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odrzuci piłeczkę",embed=None, view=None)
					
					@discord.ui.button(label="Odrzuć", style=discord.ButtonStyle.danger)
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True

						channel = await thrower.create_dm()

						await channel.send(f"{member.mention} odmówił wspólnego rzucania piłką.", view=None)
						
						await interaction.response.edit_message(content="Pomyślnie odrzucono zaproszenie rzucania piłeczką.",embed=None, view=None)

				embed = discord.Embed(title=f"{thrower.name} Zaprasza cię do:", description="", color=0xfceade)
				embed.set_thumbnail(url=f"{thrower.avatar}")
				embed.add_field(name=f"Ping Pong", value="Wspólnego rzucania piłką.", inline=False)
				embed.set_footer(text='Komunikat: "Ta czynność się nie powiodła"\nOznacza wygaśniecie zaproszenia.')
				await channel.send(embed=embed, view=MyStart())
				await interaction.response.send_message(f"Pomyślnie rzuconą piłeczkę.", ephemeral = True)
			except:
				await interaction.response.send_message(f"Przykro mi ale uczestnik {member.mention} ma zablokowane otrzymywanie wiadomości.", ephemeral = True)

		@tree.context_menu(name = "janken", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles or Role.uczestnicy_plus(interaction) in interaction.user.roles or Role.server_booster(interaction) in interaction.user.roles:
				try:
					channel = await member.create_dm()
					thrower = interaction.user
					janken = []
					member_point = []
					thrower_point = []

					class MyJanken(View):
						@discord.ui.button(label="paper",emoji="🧻", style=discord.ButtonStyle.gray)
						async def gray1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("a")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="stone",emoji="<:rock:979764802232651856>",style=discord.ButtonStyle.gray)
						async def gray2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("b")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="scissors",emoji="✂️", style=discord.ButtonStyle.gray)
						async def gray3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							janken.append("c")
							await channel.send(f"{member.mention} wybierz swój symbol.", view=MyJankenTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {member.mention} wybierze symbol.",embed=None, view=None)

					class MyJankenTwo(View):
						@discord.ui.button(label="paper",emoji="🧻", style=discord.ButtonStyle.gray)
						async def gray1_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"🧻 {member.name}: {len(member_point)}\n\n🧻 {thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"🧻 {member.name}: {len(member_point)}\n\n<:rock:979764802232651856> {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"🧻 {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
						
						@discord.ui.button(label="stone",emoji="<:rock:979764802232651856>",style=discord.ButtonStyle.gray)
						async def gray2_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n\n🧻{thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n<:rock:979764802232651856>{thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"<:rock:979764802232651856> {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
						
						@discord.ui.button(label="scissors",emoji="✂️", style=discord.ButtonStyle.gray)
						async def gray3_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							a ="a"
							b ="b"
							channel = thrower

							if a in janken:
								janken.clear()
								member_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {member.name}", description=f"✂️ {member.name}: {len(member_point)}\n\n🧻 {thrower.name}: {len(thrower_point)}",color=0xfceade)
								if member.avatar != None:
									embed.set_thumbnail(url=f"{member.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							elif b in janken:
								janken.clear()
								thrower_point.append("1")
								embed = discord.Embed(title=f"Wygrywa {thrower.name}", description=f"✂️ {member.name}: {len(member_point)}\n\n<:rock:979764802232651856> {thrower.name}: {len(thrower_point)}", color=0xfceade)
								if thrower.avatar != None:
									embed.set_thumbnail(url=f"{thrower.avatar}")
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())
							else:
								janken.clear()
								embed = discord.Embed(title=f"Remis", description=f"✂️ {member.name}: {len(member_point)}\n\n✂️ {thrower.name}: {len(thrower_point)}", color=0xfceade)
								await channel.send(embed=embed,view=None)
								await interaction.response.edit_message(embed=embed,view=MyAgian())

					class MyAgian(View):
						@discord.ui.button(label="Again", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{thrower.mention} Again ?", view=MyAgianTwo())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} odpowie na twoje zapytanie.",embed=None, view=None)
						
						@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{member.mention} odmówił dalszego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie zakończono gre w papier, kamień, nożyce.", view=None)
					
					class MyAgianTwo(View):
						@discord.ui.button(label="Again", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							await channel.send(f"{thrower.mention} wybierz swój symbol.", view=MyJanken())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="X", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True
							channel = thrower

							await channel.send(f"{thrower.mention} odmówił dalszego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie zakończono gre w papier, kamień, nożyce.", view=None)

					class MyStart(View):
						@discord.ui.button(label="Przyjmij", style=discord.ButtonStyle.green)
						async def green_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							channel = await thrower.create_dm()

							await channel.send(f"{thrower.mention} wybierz swój symbol.", view=MyJanken())
							
							await interaction.response.edit_message(content=f"Poczekaj aż {thrower.mention} wybierze symbol.",embed=None, view=None)
						
						@discord.ui.button(label="Odrzuć", style=discord.ButtonStyle.danger)
						async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
							button.disabled = True

							channel = await thrower.create_dm()

							await channel.send(f"{member.mention} odmówił wspólnego grania w papier, kamień, nożyce.", view=None)
							
							await interaction.response.edit_message(content="Pomyślnie odrzucono zaproszenie gry w papier, kamień, nożyce.",embed=None, view=None)

					embed = discord.Embed(title=f"{thrower.name} Zaprasza cię do:", description="", color=0xfceade)
					embed.set_thumbnail(url=f"{thrower.avatar}")
					embed.add_field(name=f"Janken", value="Wspólnego grania w papier, kamień, nożyce.", inline=False)
					embed.set_footer(text='Komunikat: "Ta czynność się nie powiodła"\nOznacza wygaśniecie zaproszenia/.')
					
					await channel.send(embed=embed, view=MyStart())
					await interaction.response.send_message(f"Pomyślnie wysłano zaproszenie.", ephemeral = True)

				except:
					await interaction.response.send_message(f"Przykro mi ale uczestnik {member.mention} ma zablokowane otrzymywanie wiadomości.", ephemeral = True)
			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.",ephemeral = True)

