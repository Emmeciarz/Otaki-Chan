import discord
import asyncio
from discord.ui import View
from Commands import Role


class CustomCommands:
	def get_commands(tree, client):

		@tree.command(name="kick", description="Pozwala na wyrzucanie uczestników z serwera.", guild=discord.Object(id=698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MyView(View):
					@discord.ui.button(label="YES", style=discord.ButtonStyle.green, emoji="<:5163gchemoji13yes:926276739439669318>")
					async def button_callback(self, interaction: discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await member.kick()
						await interaction.response.edit_message(content=f"Pomyślnie wyrzucono {member.mention}.", view=None)

					@discord.ui.button(label="NO", style=discord.ButtonStyle.danger, emoji="<:emoji_6:921392219343171594>")
					async def danger_button_callback(self, interaction: discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=f"Anulowano wyrzucanie {member.mention}.", view=None)

				view = MyView()
				await interaction.response.send_message(f"Czy chcesz wyrzucić uczestnika {member.mention} z serwera ?", view=view, ephemeral=True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral=True)

		@tree.command(name="ban", description="Pozwala na zbanowanie uczestnika z serwera.", guild=discord.Object(id=698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MyView(View):
					@discord.ui.button(label="YES", style=discord.ButtonStyle.green, emoji="<:5163gchemoji13yes:926276739439669318>")
					async def button_callback(self, interaction: discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await member.ban()
						await interaction.response.edit_message(content=f"Pomyślnie zbanowano {member.mention}.", view=None)

					@discord.ui.button(label="NO", style=discord.ButtonStyle.danger, emoji="<:emoji_6:921392219343171594>")
					async def danger_button_callback(self, interaction: discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=f"Anulowano banowanie {member.mention}.", view=None)

				view = MyView()
				await interaction.response.send_message(f"Czy chcesz zbanować uczestnika {member.mention} z serwera ?", view=view, ephemeral=True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral=True)

		@tree.command(name="klateczka", description="Pozwala ci na przetrzymanie/ograniczanie chatów.", guild=discord.Object(id=698522294414344232))
		async def self(interaction: discord.Integration):
			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				settings = []
				channel_this = interaction.channel
				uczestnicy = discord.utils.get(interaction.guild.roles, id=920078527930445915)
				uczestnicy_plus = discord.utils.get(interaction.guild.roles, id=920081493110423592)
				server_booster = discord.utils.get(interaction.guild.roles, id=852639143971782688)

				administracyjne_panowanie_one = channel_this.set_permissions(target=uczestnicy,send_messages=False,send_messages_in_threads=False,use_external_stickers=False,create_private_threads=False,create_public_threads=False,manage_threads=False,manage_emojis=False,manage_emojis_and_stickers=False,embed_links=False,attach_files=False,add_reactions=False,use_external_emojis=False,external_emojis=False)

				administracyjne_panowanie_two = channel_this.set_permissions(target=uczestnicy_plus,send_messages=False,send_messages_in_threads=False,use_external_stickers=False,create_private_threads=False,create_public_threads=False,manage_threads=False,manage_emojis=False,manage_emojis_and_stickers=False,embed_links=False,attach_files=False,add_reactions=False,use_external_emojis=False,external_emojis=False)

				administracyjne_panowanie_three = channel_this.set_permissions(target=server_booster,send_messages=False,send_messages_in_threads=False,use_external_stickers=False,create_private_threads=False,create_public_threads=False,manage_threads=False,manage_emojis=False,manage_emojis_and_stickers=False,embed_links=False,attach_files=False,add_reactions=False,use_external_emojis=False,external_emojis=False)

				hegemonia_aktywnych = channel_this.set_permissions(target=uczestnicy,send_messages=False,send_messages_in_threads=False,use_external_stickers=False,create_private_threads=False,create_public_threads=False,manage_threads=False,manage_emojis=False,manage_emojis_and_stickers=False,embed_links=False,attach_files=False,add_reactions=False,use_external_emojis=False,external_emojis=False)

				cancel_uczestnicy = channel_this.set_permissions(target=uczestnicy, overwrite=None)
				cancel_uczestnicy_plus = channel_this.set_permissions(target=uczestnicy_plus, overwrite=None)
				cancel_server_booster = channel_this.set_permissions(target=server_booster, overwrite=None)


				class MySelectViewFive(View):
					@discord.ui.select(
						placeholder="Uruchomić klateczkę ?",
						options=[

							discord.SelectOption(
								label="TAK",
								emoji="<:yes:926276739439669318>",
								value="1",
							),

							discord.SelectOption(
								label="NIE",
								emoji="<:no:921392219343171594>",
								value="2",
							),
						],)
					async def select_callback(self, interaction: discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":  #Nałożyć klatkę
							if "all" in settings:
								await interaction.response.send_message(view=view)

							elif "this" in settings:
								embed = discord.Embed(title="Klatka włączona !", description=f"", color=0xfceade)
								embed.add_field(name="Obszar działania:", value=f"{channel_this.mention}", inline=False)
								if "1" in settings:
									tryb_name = "Administracyjne panowanie"
									embed.set_image(url="https://i.postimg.cc/pTGFwWKR/1897691-bigthumbnail.webp")
									await administracyjne_panowanie_one
									await administracyjne_panowanie_two
									await administracyjne_panowanie_three
								if "2" in settings:
									tryb_name = "Hegemonia aktywnych"
									embed.set_image(url="https://i.postimg.cc/0jzwxTCm/desktop-wallpaper-school-girls-happy-girl-anime-friends.jpg")
									await hegemonia_aktywnych
								embed.add_field(name="Wybrany tryb:", value=f"{tryb_name}", inline=True)
								if "a" in settings:
									time_name = "5 Minut"
									time_nuber = 300
								if "b" in settings:
									time_name = "30 Minut"
									time_nuber = 1800
								if "c" in settings:
									time_name = "1 Godzine"
									time_nuber = 3600
								if "d" in settings:
									time_name = "3 Godziny"
									time_nuber = 10800
								if "e" in settings:
									time_name = "6 Godzin"
									time_nuber = 21600
								
								embed.add_field(name="Czas trwania:", value=f"{time_name}", inline=True)
								await interaction.response.edit_message(embed=embed,view=None)

								embed = discord.Embed(title=f"{interaction.user.name} włączył klateczkę !", description=f"", color=0xf54227)
								embed.add_field(name="⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘", value=f"", inline=False)
								embed.add_field(name="Czas trwania:", value=f"{time_name}", inline=True)
								embed.add_field(name="Tryb działania:", value=f"{tryb_name}", inline=True)
								embed.add_field(name="⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘", value=f"", inline=False)
								embed.set_footer(text="Chwilowe ograniczenie chatu.")
								await channel_this.send(embed=embed)

								await asyncio.sleep(time_nuber)
								await cancel_uczestnicy
								await cancel_uczestnicy_plus
								await cancel_server_booster

								embed = discord.Embed(title="Wrota piekieł zostały otwarte !", description=f"Czas trwania klatki dobiegł końca, miłego ponownego pisania.", color=0x56e455)
								embed.set_image(url="https://i.postimg.cc/43Gt4cSC/anime-ch-niby-demo-koi-ga-shitai.gif")
								await channel_this.send(embed=embed)

						if select.values[0] == "2":  #Anulować klateczke
							embed = discord.Embed(title="BEZ KLATECZKII ?!", description=f"", color=0xf54227)
							embed.set_image(url="https://i.postimg.cc/TwNjK0Gm/megumin.gif")
							await interaction.response.edit_message(embed=embed, view=None)

				class MySelectViewFour(View):
					@discord.ui.select(
						placeholder="Jak długo ma trwać ?",
						options=[

							discord.SelectOption(
								label="5 Minut",
								emoji="<:scared:1098732736933527775>",
								value="1",
							),

							discord.SelectOption(
								label="30 Minut",
								emoji="<a:lnepreto:1099070176403652749> ",
								value="2",
							),

							discord.SelectOption(
								label="1 Godzine",
								emoji="<:scared:921400267516280892>",
								value="3",
							),

							discord.SelectOption(
								label="3 Godziny",
								emoji="<:mentalbreakdown:926276740437921843> ",
								value="4",
							),

							discord.SelectOption(
								label="6 Godzin",
								emoji="<a:yadeadinside:1099093180193968198>",
								value="5",
							),
						],)
					async def select_callback(self, interaction: discord.Integration, select: discord.ui.Select):
						select.disabled = True
						if select.values[0] == "1":  # 5 Minut								
							await interaction.response.edit_message(view=MySelectViewFive())
							settings.append("a")
								
						if select.values[0] == "2":  # 30 Minut
							await interaction.response.edit_message(view=MySelectViewFive())
							settings.append("b")

						if select.values[0] == "3":  # 1 Godzine
							await interaction.response.edit_message(view=MySelectViewFive())
							settings.append("c")

						if select.values[0] == "4":  # 3 Godzin
							await interaction.response.edit_message(view=MySelectViewFive())
							settings.append("d")

						if select.values[0] == "5":  # 6 Godziny
							await interaction.response.edit_message(view=MySelectViewFive())
							settings.append("e")

				class MySelectViewThree(View):
					@discord.ui.select(
						placeholder="Jaki tryb chcesz użyć ?",
						options=[

							discord.SelectOption(
									label="Administracyjne panowanie",
									emoji="<:conflict:921394533449744394>",
									value="1",
							),

							discord.SelectOption(
								label="Hegemonia aktywnych",
								emoji="<a:diamond:929083661083611186>",
								value="2",
							),
						],)
					async def select_callback(self, interaction: discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":  # Administracyjne panowanie
							await interaction.response.edit_message(view=MySelectViewFour())
							settings.append("1")

						if select.values[0] == "2":  # Hegemonia aktywnych
							await interaction.response.edit_message(view=MySelectViewFour())
							settings.append("2")

				class MySelectViewTwo(View):
					@discord.ui.select(
						placeholder="Jaką cześć chcesz zamknąć ?",
						options=[

							discord.SelectOption(
									label="Cały serwer",
									emoji="<:report:921400267440791662>",
									# emoji="<a:panic:926303374410936351>",
									value="1",
							),

							discord.SelectOption(
								label="Kanał na którym przebywasz",
								emoji="<a:cmrudumb:1099069910027616326>",
								value="2",
							),
						],)
					async def select_callback(self, interaction: discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":  # Cały serwer
							await interaction.response.edit_message(view=MySelectViewThree())
							settings.append("all")

						if select.values[0] == "2":  # Kanał na którym przebywasz
							await interaction.response.edit_message(view=MySelectViewThree())
							settings.append("this")

				class MySelectViewOne(View):
					@discord.ui.select(
						placeholder="Co chcesz zrobić ?",
						options=[

							discord.SelectOption(
									label="Nałożyć klatkę",
									emoji="🔒",
									value="1",
							),

							discord.SelectOption(
								label="Zdjąć klatkę",
								emoji="<:report:921400267440791662>",
								# emoji="🔓",
								value="2",
							),
						],)
					async def select_callback(self, interaction: discord.Integration, select: discord.ui.Select):
						select.disabled = True

						if select.values[0] == "1":  # Nałożyć klatkę
							await interaction.response.edit_message(view=MySelectViewTwo())

						if select.values[0] == "2":  # Zdjąć klatkę
							embed = discord.Embed(
								title="Zdjęto klateczkę !", description=f"", color=0xfceade)
							await interaction.response.edit_message(embed=embed, view=None)

				view = MySelectViewOne()
				await interaction.response.send_message(view=view, ephemeral=True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy {interaction.user.mention}.", ephemeral=True)
