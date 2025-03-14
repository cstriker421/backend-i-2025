import sys
import os
import pytest
from unittest.mock import MagicMock, AsyncMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from session_09.exercise_with_challenge.bot import bot

# Note: `discord.py` uses the deprecated `audioop` module, and `pytest-asyncio` has deprecated event loop handling.
# They are slated for removal and cause warnings, but they are due to the libraries and not the code.

@pytest.mark.asyncio
async def test_ping():

    mock_ctx = MagicMock()
    mock_ctx.send = AsyncMock()
    
    await bot.get_command('ping').callback(mock_ctx)

    mock_ctx.send.assert_called_with("Pong!")

@pytest.mark.asyncio
async def test_welcome():

    mock_ctx = MagicMock()
    mock_ctx.send = AsyncMock()
    
    mock_user = MagicMock()
    mock_user.mention = "TestUser"

    await bot.get_command('welcome').callback(mock_ctx, mock_user)

    mock_ctx.send.assert_called_with(f"Welcome to the server, {mock_user.mention}!")
