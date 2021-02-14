from pyrogram.types import Message


def get_input(message: Message) -> str: return " ".join(message.command[1:])
