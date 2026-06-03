# -*- coding: utf-8 -*-
import asyncio
import logging
from bot import Bot
from pyrogram import idle

# Error အသေးစိတ်ကို Log ထဲမှာ ပေါ်အောင် လုပ်ပေးတာပါ
logging.basicConfig(level=logging.INFO)

async def main():
    try:
        app = Bot()
        print("Bot is starting...")
        await app.start()
        print("Bot started successfully!")
        await idle()
    except Exception as e:
        print(f"Error တက်နေပါတယ်: {e}") # ဒီစာကြောင်းက ဘာကြောင့် Error တက်လဲဆိုတာ ပြောပြပေးလိမ့်မယ်
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
