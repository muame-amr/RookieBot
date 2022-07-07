import os
from dotenv import load_dotenv
from classes.client import Client

load_dotenv()
token = os.getenv("TOKEN")

client = Client(token);
client.run()
