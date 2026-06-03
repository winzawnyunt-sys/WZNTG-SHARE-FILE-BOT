# -*- coding: utf-8 -*-
from pyrogram import Client
import config

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="MyBot",
            api_id=int(config.API_ID),
            api_hash=config.API_HASH,
            bot_token=config.TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        print("Bot ပွင့်သွားပါပြီ!")

    async def stop(self, *args):
        await super().stop()
