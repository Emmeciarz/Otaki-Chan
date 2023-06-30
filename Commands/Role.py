import discord

def moderatorzy(interaction):
	moderatorzy = discord.utils.get(interaction.user.guild.roles, id=921504757435203624)

	return moderatorzy

def administrator(interaction):
	administrator = discord.utils.get(interaction.user.guild.roles, id=699301861466832976)

	return administrator

def uczestnicy_plus(interaction):
	uczestnicy_plus = discord.utils.get(interaction.user.guild.roles, id=920081493110423592)

	return uczestnicy_plus

def server_booster(interaction):
	server_booster = discord.utils.get(interaction.user.guild.roles, id=852639143971782688)

	return server_booster

def plus(interaction):
	plus = discord.utils.get(interaction.user.guild.roles, id=1124025539540295840)

	return plus




def moderatorzy_m(member):
	moderatorzy = discord.utils.get(member.guild.roles, id=921504757435203624)

	return moderatorzy

def administrator_m(member):
	administrator = discord.utils.get(member.guild.roles, id=699301861466832976)

	return administrator

def uczestnicy_plus_m(member):
	uczestnicy_plus = discord.utils.get(member.guild.roles, id=920081493110423592)

	return uczestnicy_plus

def server_booster_m(member):
	server_booster = discord.utils.get(member.guild.roles, id=852639143971782688)

	return server_booster

def plus_m(member):
	plus = discord.utils.get(member.guild.roles, id=1124025539540295840)

	return plus