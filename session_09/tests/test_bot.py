import sys
import os
import pytest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from session_09.exercise_with_challenge.bot import bot  # Adjust the import based on the structure

@pytest.mark.asyncio
async def test_ping():
    mock_ctx = MagicMock()
    await bot.get_command('ping').callback(mock_ctx)
    mock_ctx.send.assert_called_with("Pong!")

@pytest.mark.asyncio
async def test_welcome():
    mock_ctx = MagicMock()
    mock_user = MagicMock()
    mock_user.mention = "TestUser"
    await bot.get_command('welcome').callback(mock_ctx, mock_user)
    mock_ctx.send.assert_called_with(f"Welcome to the server, {mock_user.mention}!")
