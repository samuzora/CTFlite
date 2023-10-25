import logging
import os
import time
import traceback

import discord
from discord.ext import commands 

token = os.environ.get("CTFCORD_BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    case_insensitive=True,
    description="CTF management Discord bot",
    intents=intents,
)

@bot.event
async def on_ready():
    await bot.user.edit(username='CTF-cord')
    print("Bot is running")

@bot.slash_command(description="Help command")
async def help(ctx):
    # Command list 
    description = \
"""CTF-cord will help you to manage your CTF team.
With CTF-cord, you can pull data from CTFtime, automatically create Discord text channels and roles for each CTF (with appropriate perms), track challenge solves and more!

```
/ctf details ctftime_link:1616
```
This command will pull data from CTFtime and display it in an embed.
```
/ctf reg team_name:test ctftime_link:<whatever new ctfs are on ctftime>
```
This will pull the relevant info from CTFtime, and use it to send embeds and automatically create a Discord text channel, alongside a team role with access to this channel, and a scheduled Event in Discord.
```
/ctf unreg
```
Invoke this in the created channel to delete the CTF.
"""
    # Format embed
    embed = discord.Embed(
            title="CTF-cord",
            description=description,
            colour=discord.Colour.blurple(),
    )
    embed.url = "https://github.com/samuzora/CTF-cord"
    embed.set_footer(text="Click on the embed title to view the full list of commands!")
    await ctx.respond(embed=embed)

# Error handler
@bot.event
async def on_application_command_error(ctx, e):
    message = "Sorry, something went wrong."
    print(f'ERROR!\n----------\n{ctx.author.name} ({ctx.author.id}) at {time.strftime("%H%M")}:\n')
    traceback.print_exception(type(e), e, e.__traceback__)
    print("----------")
    await ctx.respond(message, ephemeral=True)


if __name__ == "__main__":
    bot.load_extension("cogs.ctf")
    bot.load_extension("cogs.dev")
    # bot.load_extension("cogs.chall")
    # bot.load_extension("cogs.dev")
    # bot.load_extension("cogs.settings")
    bot.run(token)


