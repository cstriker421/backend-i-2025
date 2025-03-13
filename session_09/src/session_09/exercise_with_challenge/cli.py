import typer
from bot import run_bot

app = typer.Typer()

@app.command()
def start():
    """
    Start the Discord bot using the token from the environment variable.
    """
    run_bot()

@app.command()
def send_test_message(token: str, channel_id: int, message: str):
    """
    Send a test message to a specific Discord channel using the provided token.
    """
    import discord
    from discord.ext import commands
    import asyncio

    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(message)
            print(f"Test message sent to channel {channel_id}: {message}")
        else:
            print("Invalid channel ID")
        await bot.close()

    bot.run(token)

if __name__ == "__main__":
    app()
