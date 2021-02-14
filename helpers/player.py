from queue import Queue
import threading

from mpv import MPV
from pyrogram.types import Message


mpv = MPV()
queue = Queue()
status = {}


def worker():
    while True:
        item = queue.get()
        item["start"][0](**item["start"][1])
        mpv.play(item["file"])
        mpv.wait_for_playback()
        item["stop"][0](**item["stop"][1])


threading.Thread(target=worker, daemon=True).start()


def play(item):
    queue.put(item)
    return queue.qsize()


def stop() -> bool: return not mpv.stop() if mpv.filename else False


def prep_item(file: str, message: Message):
    return {"file": file, "start": [message.reply_text, {"text": "Playing..."}], "stop": [message.reply_text, {"text": "Finished playing."}]}


def seek(amount: str) -> bool: return not mpv.seek(amount) if mpv.filename else False
