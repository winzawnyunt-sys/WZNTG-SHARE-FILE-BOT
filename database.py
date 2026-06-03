# -*- coding: utf-8 -*-
import motor.motor_asyncio
from config import MONGO_DB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)
db = client["file_store_bot"]
files_db = db["files"]

async def save_file(file_id, file_name):
    await files_db.insert_one({"file_id": file_id, "file_name": file_name})

async def get_file(file_name):
    return await files_db.find_one({"file_name": file_name})
  
