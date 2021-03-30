from discord.ext import commands

class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		'''
		Help Example:
		e = discord.Embed(title=f"**All Commands**", color=discord.Color.blurple(), description='')
		e.add_field(name="**▬▬▬▬Everyone▬▬▬▬**", value="Commands for @everyone", inline=False)
		e.add_field(name="**help `!help`**", value="Shows a list of commands", inline=False)
		await ctx.author.send(embed=e)/await ctx.send(embed=e)
		------
		e = discord.Embed(title='Commands', description='`!help`: Shows a list of commands \n `!filler`: filler')
		await ctx.author.send(embed=e)/await ctx.send(embed=e)
		'''
		await ctx.send("Edit the help command in ./cogs/help.py!")

def setup(bot):
	bot.add_cog(help(bot))
