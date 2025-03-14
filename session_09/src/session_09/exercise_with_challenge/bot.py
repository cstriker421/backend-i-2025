import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

load_dotenv()  # Loads environment variables

TOKEN = os.getenv("DISCORD_TOKEN")  # Gets the Discord token from the environment

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

# Predefined channel ID
CHANNEL_ID = 1349828764204535901  # Replace this with the actual channel ID

# Function to send a test message to a specific channel
async def send_test_message(channel_id: int, message: str):
    channel = bot.get_channel(channel_id)  # Gets the channel by ID
    if channel:
        await channel.send(message)  # Sends the message to the channel
        logging.info(f"Test message sent to channel {channel_id}: {message}")
    else:
        logging.error(f"Invalid channel ID: {channel_id}")  # Note, I have tried to get this to work, 
                                                            # but I keep getting an `Invalid channel ID` error
                                                            # even though it shouldn't I DO NOT KNOW WHY

def run_bot():
    if TOKEN is None:
        raise ValueError("No Discord token found in environment variables")
    bot.run(TOKEN)  # Runs the bot with the token from the environment
