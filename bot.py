import discord
import config
from discord.ext import commands
import config


initial_extensions = ['cogs.utility',
                      'cogs.owner',
                      'cogs.help']


bot = commands.Bot(command_prefix=config.bot_prefix, case_insensitive=True)
bot.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
        print("loaded: {}".format(extension))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game("{}help for commands".format(config.bot_prefix))
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send("error: {}".format(error))


bot.run(config.bot_key)
