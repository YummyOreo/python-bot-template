import discord
from discord.ext import commands
import os, time
from modules import arrows, color
from dotenv import dotenv_values

#Loads the .env file
config = dotenv_values(".env")

#Inits the bot
bot = commands.Bot(command_prefix=config["PREFIX"])
bot.remove_command("help") #Removes the set help command


@bot.event
async def on_ready():
	#Gets the local time
	localtime = time.asctime(time.localtime(time.time()))
	#Prints when ready
	color.green(f'[{localtime}]', f'{arrows.RIGHT} Main file online')
	#changes the activity
	await bot.change_presence(activity=discord.Game(name=config["ACTIVITY"]))

#Sets the var called directory
directory = r'.\cogs'
#Loads in all of the cogs
for filename in os.listdir(directory):

	#Checks if its a .py file
	if filename.endswith(".py"):
		#Logs it
		color.yellow('[Loading]', f'{arrows.RIGHT} {filename[:-3]}...')
		#Loads it
		bot.load_extension(f'cogs.{filename[:-3]}')
		#logs that its loaded
		color.green('[Loaded]', f'{arrows.RIGHT} {filename[:-3]}...')
	else:
		#Logs the fail
		color.red('[Faile]', f'{arrows.RIGHT} {filename}...')

token = config['TOKEN']
bot.run(token)