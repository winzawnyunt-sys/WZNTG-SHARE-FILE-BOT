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
        
from database import save_file  # database.py ထဲက save_file ဆိုတဲ့ function ကို ခေါ်လိုက်တာ

# ဘော့တ်က ဖိုင်တစ်ခု လက်ခံရရှိတဲ့အခါ...
async def handle_file(client, message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    
    # Database ထဲ သိမ်းလိုက်မယ်
    await save_file(file_id, file_name)
    await message.reply("ဖိုင်ကို သိမ်းပြီးပါပြီ!")
