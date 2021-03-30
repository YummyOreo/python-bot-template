from discord.ext import commands

class test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):
		print('YAY')

def setup(bot): # a extension must have a setup function
	bot.add_cog(test(bot))
