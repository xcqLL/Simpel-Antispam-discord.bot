import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

message_counts = {}
cooldown = commands.CooldownMapping.from_cooldown(1, 1, commands.BucketType.user)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    bucket = cooldown.get_bucket(message)
    retry_after = bucket.update_rate_limit()
    channel = bot.get_channel(YOUR_CHANNEL ID)
    
    if retry_after:
        if not message.author.bot: 
            await message.delete()
            await message.author.send("# LU KALO NGETIK JANGAN CEPET CEPET KONTOL ANAK E RIAN ATAU SIAPAPUN") # SEND MESSAGE IN DMS (NOT IN SERVER)
            await channel.send(f"{message.author.mention} NGETIK PELAN PELAN BOS | COOLDOWN = 1 detik")# SEND MESSAGE IN CHANNEL TAHT YOU SET THE CH ID (IN SERVER)
        return

    await bot.process_commands(message)

bot.run('ADD YOUR TOKEN IN HERE')
