import asyncio
from bot import Bot
from pyrogram import idle

async def main():
    app = Bot()
    await app.start()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
