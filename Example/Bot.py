from discord.ext import commands
from UrlMatch import Match

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{str(bot.user)} is On Ready.')

@bot.command(name='Url확인')
async def UrlCheck(ctx, query: str):
    p = Match(query)
    if p.UrlMatch() is True:
        return await ctx.reply('오 이건 Url임')
    return await ctx.reply('오 이건 Url이 아님')


@bot.command(name='이메일확인')
async def EmailCheck(ctx, query: str):
    p = Match(query)
    if p.EmailMatch() is True:
        return await ctx.reply('오 이건 이메일임')
    return await ctx.reply('오 이건 이메일이 아님')

bot.run('Your Token')