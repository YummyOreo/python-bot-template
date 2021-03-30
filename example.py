from discord.ext import commands

class NAME(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def NAME(self, ctx):
		'''CODE'''
def setup(bot):
	bot.add_cog(NAME(bot))
