import typer
import os
from bot import run_bot, send_test_message  # Import send_test_message

app = typer.Typer()

@app.command()
def start():
    """
    Start the Discord bot using the token from the environment variable.
    """
    run_bot()

@app.command()
def send_test_message_command(
    channel_id: int = typer.Option(..., help="ID of the channel to send the message to"),
    message: str = typer.Option(..., help="The message to send to the channel")
):
    """
    Send a test message to a specific Discord channel using the provided token.
    """
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

    @bot.event
    async def on_ready():
        # Use the provided channel_id to send the message to the given channel
        await send_test_message(channel_id, message)
        print(f"Test message sent to channel {channel_id}: {message}")
        await bot.close()

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("No Discord token found in environment variables.")
        
    bot.run(token)  # Now we pass the token explicitly

if __name__ == "__main__":
    app()
