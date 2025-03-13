import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    """
    Responds to the !ping command with 'Pong!'
    """
    await ctx.send("Pong!")

@bot.command()
async def welcome(ctx, user: discord.User):
    """
    Welcomes a user to the server by mentioning them.
    """
    await ctx.send(f"Welcome to the server, {user.mention}!")

def run_bot():
    if TOKEN is None:
        raise ValueError("No Discord token found in environment variables")
    bot.run(TOKEN)
