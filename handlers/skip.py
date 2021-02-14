from pyrogram import Client, filters
from pyrogram.types import Message

from helpers.filters import from_chat
from helpers.player import stop


@Client.on_message(
    filters.command("skip")
    & from_chat
    & ~filters.edited
)
async def telegram(client: Client, message: Message):
    if stop():
        await message.reply_text("Skipped.")
    else:
        await message.reply_text("Nothing is playing.")
