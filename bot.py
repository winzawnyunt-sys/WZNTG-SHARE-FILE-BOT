from pyrogram import Client
from config import API_ID, API_HASH, TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="MyBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        print("Bot is running!")

    async def stop(self, *args):
        await super().stop()
