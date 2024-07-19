from typing import Final
import os 
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)