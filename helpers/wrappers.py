from typing import Union

from pyrogram import Client
from pyrogram.types import Message, CallbackQuery

from config import OWNER_ID


def owner_only(func):
    async def wrapper(client: Client, message: Union[Message, CallbackQuery]):
        if message.from_user.id == OWNER_ID:
            return await func(client, message)
        else:
            if isinstance(message, Message):
                return await message.reply_text("Only the owner can do this.")
            elif isinstance(message, CallbackQuery):
                return await message.answer("Only the owner can do this.", show_alert=True)
            else:
                return
    return wrapper


def requires_reply(func):
    async def wrapper(client: Client, message: Message):
        if message.reply_to_message:
            return await func(client, message)
        else:
            return await message.reply_text("Reply a message.")
    return wrapper
