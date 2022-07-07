import discord
from multiprocessing.connection import Client

class Client:
    client = discord.Client()
    def __init__(self, token):
        self.token = token
        
    @client.event
    async def on_ready():
        print(f'We have logged in as {Client.client.user}')

    @client.event
    async def on_message(message):
        if message.author == Client.client.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('👋 Hello!');

        if message.content.startswith('$ping'):
            await message.channel.send('🏓 Pong!');
    
    def run(self):
        Client.client.run(self.token)