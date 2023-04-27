import discord
from discord.ui import View
from Commands import Role

class CustomCommands:
	def get_commands(tree,client):

		@tree.command(name = "kick", description= "Pozwala na wyrzucanie uczestników z serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MyView(View):
					@discord.ui.button(label="YES", style=discord.ButtonStyle.green, emoji="<:5163gchemoji13yes:926276739439669318>")
					async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await member.kick()
						await interaction.response.edit_message(content=f"Pomyślnie wyrzucono {member.mention}.", view=None)

					@discord.ui.button(label="NO", style=discord.ButtonStyle.danger, emoji="<:emoji_6:921392219343171594>")
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=f"Anulowano wyrzucanie {member.mention}.", view=None)

				view = MyView()
				await interaction.response.send_message(f"Czy chcesz wyrzucić uczestnika {member.mention} z serwera ?", view=view ,ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)

		@tree.command(name = "ban", description= "Pozwala na zbanowanie uczestnika z serwera.", guild = discord.Object(id = 698522294414344232))
		async def self(interaction: discord.Integration, member: discord.Member):

			if Role.moderatorzy(interaction) in interaction.user.roles or Role.administrator(interaction) in interaction.user.roles:
				class MyView(View):
					@discord.ui.button(label="YES", style=discord.ButtonStyle.green, emoji="<:5163gchemoji13yes:926276739439669318>")
					async def button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await member.ban()
						await interaction.response.edit_message(content=f"Pomyślnie zbanowano {member.mention}.", view=None)

					@discord.ui.button(label="NO", style=discord.ButtonStyle.danger, emoji="<:emoji_6:921392219343171594>")
					async def danger_button_callback(self, interaction:discord.Integration, button: discord.ui.Button):
						button.disabled = True
						await interaction.response.edit_message(content=f"Anulowano banowanie {member.mention}.", view=None)

				view = MyView()
				await interaction.response.send_message(f"Czy chcesz zbanować uczestnika {member.mention} z serwera ?", view=view ,ephemeral = True)

			else:
				await interaction.response.send_message(f"Nye masz uprawnień do korzystania z tej komendy{interaction.user.mention}", ephemeral = True)
