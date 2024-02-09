from dotenv import load_dotenv
import os
import discord
from discord.ext import commands


load_dotenv()

DISCORD_KEY= os.getenv('DISCORD_ID')

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("The bot is ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Avicii"))



bot.run(DISCORD_KEY)