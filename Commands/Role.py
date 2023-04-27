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

def traveler(interaction):
	traveler = discord.utils.get(interaction.user.guild.roles, id=1018206772869222410)

	return traveler