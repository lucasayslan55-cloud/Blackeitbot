import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Online {bot.user}")
    await bot.tree.sync()
@bot.tree.command(name="ping", description="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")
bot.run(os.getenv("DISCORD_TOKEN"))
