from discord.ext import commands
import discord
import os
import asyncio
import operator

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')

#whlist 927220055194894419 1226943009573179405 1226944434822971505

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(
	 type=discord.ActivityType.watching, name='за призывниками'))
	print('Bot is currently online!')
	# await check_channels()
	await online(927220055194894419)



#help command
@bot.command(pass_context=True)
async def help(ctx):
	await ctx.send('Что ты хочешь здесь увидеть?')


#join commands
# @bot.command(pass_context=True)
# async def join(ctx):
# 	if not (ctx.voice_client):
		# voice_channel = bot.get_channel(123)
		# await voice_channel.connect()


@bot.command(pass_context=True)
async def check_channels(ctx):
	channels_dict = {}
	for guild in bot.guilds:
		print(guild)
		for vc in guild.voice_channels:
			channels_dict[vc.id] = 0
			for member in vc.members:
				channels_dict[vc.id] += 1
				print(member.name)
	print(channels_dict)

async def online(channel_id):
	await bot.wait_until_ready()
	while not bot.is_closed():
		try:
			voice_channel = bot.get_channel(channel_id)
			await voice_channel.connect()
		except discord.errors.ClientException:
			pass

		await asyncio.sleep(15)


TOKEN = 'MTAzNTU2NDY0Nzc0NDUzNjY3Nw.G1Vuoq.rrmKgrMcinug3-wnQF7AHRxPbf6wlasg-vV_tc'
bot.run(TOKEN)
