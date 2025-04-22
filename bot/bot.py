import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot.commands import setup_commands

# Load environment variables
load_dotenv()

# Bot setup
def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        print(f' {bot.user} is online and ready!')
    
    # Setup commands
    setup_commands(bot)
    
    return bot

def run_bot():
    bot = create_bot()
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    run_bot()