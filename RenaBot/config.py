import os
from telethon import TelegramClient

api_id = "10247139"
api_hash = "96b46175824223a33737657ab943fd6a"
Bot_token = os.environ.get('TOKEN')
Admin= os.environ.get('ADMIN_ID')
client=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)
