
import discord  
from password import  gen_password
from ekolog import gen_ekolog

# Переменная intents - хранит привилегии бота 
intents = discord.Intents.default() 
# Включаем привелегию на чтение сообщений 
intents.message_content = True 
# Создаем бота в переменной client и передаем все привелегии 
client = discord.Client(intents=intents) 
 
@client.event 
async def on_ready(): 
    print(f'We have logged in as {client.user}') 
 
@client.event 
async def on_message(message): 
    if message.author == client.user: 
        return 
    if message.content.startswith('$hello'): 
        await message.channel.send("Hi!") 
    elif message.content.startswith('$bye'): 
        await message.channel.send("\\U0001f642") 
    elif message.content.startswith('$password'): 
        await message.channel.send("Твой паоль:"+ gen_password(10)) 
    elif message.content.startswith('$salam'): 
        await message.channel.send("alekumasalam") 
    elif message.content.startswith('$русский'): 
        await message.channel.send("язык переведен на русский") 
    elif message.content.startswith('$привет'): 
        await message.channel.send("привет если вы хатите посматреть на мемы то напеши слова $мем на английском") 
    elif message.content.startswith('$пока'): 
        await message.channel.send("досвидане")
    elif message.content.startswith('$пока'): 
        await message.channel.send("досвидане")  
    elif message.content.startswith('$ekolog'): 
        await message.channel.send("Экология:"+ gen_ekolog())       

client.run('MTE1MjUzNzY4MDM1MDAyMzY5MQ.GZzdUg.4rrvnKDzrV4wuvlcbuQ7AtAr3j9LQYIX9glT-Q')
