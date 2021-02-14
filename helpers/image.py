import os

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import Message

FONT = "./assets/otf/font.otf"
FORE = "./assets/png/foreground.png"
FORE_SQUARE = "./assets/png/foreground_square.png"


def change_size(max_width: int, max_height: int, image):
    width_ratio = max_width / image.size[0]
    height_ratio = max_height / image.size[1]
    new_width = int(width_ratio * image.size[0])
    new_height = int(height_ratio * image.size[1])
    new_image = image.resize((new_width, new_height))
    return new_image


async def generate_cover_square(message: Message, title: str, artist: str, duration: int, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open("./background.png")
    image2 = Image.open(FORE_SQUARE)
    image3 = change_size(600, 500, image1)
    image4 = change_size(600, 500, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 20)
    draw.text((150, 380), f"Title: {title}", (255, 255, 255), font=font)
    draw.text((150, 405), f"By: {artist}", (255, 255, 255), font=font)
    draw.text(
        (150, 430),
        f"Duration: {duration}s",
        (255, 255, 255),
        font=font,
    )
    draw.text(
        (150, 455),
        f"Requester: {message.from_user.first_name}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


async def generate_cover(message: Message, title: str, views: int, duration: int, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open(FORE)
    image3 = change_size(1280, 720, image1)
    image4 = change_size(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Requester: {message.from_user.first_name}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")
