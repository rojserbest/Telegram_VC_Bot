from pyrogram import Client, filters
from pyrogram.types import Message

from helpers.wrappers import requires_reply
from helpers.filters import from_chat
from helpers.player import play, prep_item


@Client.on_message(
    filters.command("telegram")
    & from_chat
    & ~filters.edited
)
@requires_reply
async def telegram(client: Client, message: Message):
    file = message.reply_to_message.audio or message.reply_to_message.document

    if not file:
        await message.reply_text("Reply an audio-like thing.")
    elif file.file_size >= 104857600:
        await message.reply_text("Try something less than 100 MB.")
    else:
        message_ = await message.reply_text("Downloading...")
        file = await client.download_media(message.reply_to_message)
        await message_.edit_text(f"Downloaded and added to the queue at position {play(prep_item(file, message))}.")
