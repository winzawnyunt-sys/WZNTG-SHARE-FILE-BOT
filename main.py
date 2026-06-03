# -*- coding: utf-8 -*-
import asyncio
import logging
from bot import Bot
from pyrogram import idle

# Log ကို အသေးစိတ်ပြဖို့ Setting လုပ်တာ
logging.basicConfig(level=logging.DEBUG)

async def main():
    try:
        print("Bot စတင်ရန် ကြိုးစားနေသည်...")
        app = Bot()
        await app.start()
        print("Bot ပွင့်သွားပါပြီ!")
        await idle()
    except Exception as e:
        # ဒီနေရာမှာ Error တက်ရင် ဘာကြောင့်တက်လဲဆိုတာ Log ထဲမှာ ပေါ်လာလိမ့်မယ်
        print(f"ERROR ဖြစ်နေသည်: {e}") 

if __name__ == "__main__":
    asyncio.run(main())
