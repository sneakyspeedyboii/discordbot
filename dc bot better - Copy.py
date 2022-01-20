from discord.ext import commands
import random
import discord
TOKEN = "OTMwNTY4MjAzNTM5NzM4Njc1.Yd3xLA.pBHSN6XrGe28aOeCEDsXzlBA2O4"

bot = commands.Bot(command_prefix="[")
client = discord.Client()
guild = client.guilds

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
 
    if message.content == '[hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == '[bye':
        await message.channel.send(f'Goodbye {message.author}')
    if message.content == 'men':
        one = str(random.randint(0, 255))
        two = str(random.randint(0, 255))
        three = str(random.randint(0, 255))
        four = str(random.randint(0, 255))
        done = one + '.' + two + '.' + three + '.' + four
        await message.channel.send(done)
    if message.content == '[go':
        while True:
            await message.channel.send('men')
    if message.content == '[109.186.142.255':
        await guild.create_role(name="role name")

    await bot.process_commands(message)

bot.run(TOKEN)
