import discord

class Client:
    client = discord.Client()
    def __init__(self, token):
        self.token = token
        self.prefix = '$'
        
    @client.event
    async def on_ready():
        print(f'We have logged in as {Client.client.user}')

    @client.event
    async def on_message(self, message):
        commands = message.content.split(' ')[0].lower()
        if message.author == Client.client.user:
            return
        
        if prefix.startswith(self.prefix + "hello"):
            await message.channel.send("Hello! :wave:");

        if prefix.startswith(self.prefix + "ping"):
            await message.channel.send("Pong! :ping_pong:");
    
    def run(self):
        Client.client.run(self.token)