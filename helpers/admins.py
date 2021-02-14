from pyrogram.types import Chat


async def get_admins(chat: Chat):
    return [member.user.id for member in await chat.iter_members(filter="administrators")]
