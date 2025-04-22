import discord
from discord.ext import commands
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supabase_utils.query_supabase import query_supabase

def setup_commands(bot):
    @bot.command(name='ask')
    async def ask(ctx, *, question):
        """Ask a question about Uniswap v4"""
        async with ctx.typing():
            try:
                result = query_supabase(question)
                
                if result:
                    embed = discord.Embed(
                        title="📚 Uniswap v4 Documentation",
                        color=discord.Color.blue()
                    )
                    embed.add_field(
                        name="Topic",
                        value=result['title'],
                        inline=False
                    )
                    embed.add_field(
                        name="Description",
                        value=result['description'],
                        inline=False
                    )
                    embed.add_field(
                        name="Learn More",
                        value=f"[Read Documentation]({result['url']})",
                        inline=False
                    )
                    
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("❌ I couldn't find a relevant answer to your question. Try rephrasing it!")
                    
            except Exception as e:
                print(f"Error processing question: {e}")
                await ctx.send("❌ Sorry, I encountered an error while processing your question. Please try again later.")