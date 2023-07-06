import json
import discord
from discord.ext import commands

# Get configuration.json
with open("configuration.json", "r", encoding="UTF-8") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]

intents = discord.Intents.all()
bot = commands.Bot(prefix, intents=intents)

# Load cogs
initial_extensions = ["Cogs.help", "Cogs.ping"]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except (FileNotFoundError, Exception) as e:
            print(f"Failed to load extension {extension}. Error {e}")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"for someone to type {bot.command_prefix}help",
        )
    )
    print(discord.__version__)


bot.run(token)
