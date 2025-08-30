import os
import discord
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv
import secrets

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["luarmor_free_panel"]
keys_collection = db["keys"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command()
async def generate(ctx):
    key = secrets.token_hex(8)
    keys_collection.insert_one({"key": key})
    await ctx.send(f"🔑 Generated Key: `{key}`")

@bot.command()
async def revoke(ctx, key: str):
    result = keys_collection.delete_one({"key": key})
    if result.deleted_count:
        await ctx.send(f"🗑️ Key `{key}` revoked.")
    else:
        await ctx.send(f"❌ Key `{key}` not found.")

@bot.command()
async def stats(ctx):
    total = keys_collection.count_documents({})
    await ctx.send(f"📊 Total Keys: **{total}**")

bot.run(TOKEN)
