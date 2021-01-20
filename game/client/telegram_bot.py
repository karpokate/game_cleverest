from flask import Flask
import telegram
from game.client.credentials import bot_token

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)
