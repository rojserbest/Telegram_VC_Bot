from pyrogram import Client, filters
from pyrogram.types import Message

from helpers.wrappers import owner_only
from helpers.filters import from_chat
from helpers.player import seek


@Client.on_message(
    filters.command("seekf")
    & from_chat
    & ~filters.edited
)
@owner_only
async def seekf(client: Client, message: Message):
    try:
        seek(f"+{int(message.command[1])}")
        await message.delete()
    except:
        pass


@Client.on_message(
    filters.command("seekb")
    & from_chat
    & ~filters.edited
)
@owner_only
async def seekb(client: Client, message: Message):
    try:
        seek(f"-{int(message.command[1])}")
        await message.delete()
    except:
        pass
