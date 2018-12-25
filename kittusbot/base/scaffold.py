from logging import basicConfig, getLogger, INFO, DEBUG
from os import environ
from json import load


telegram_token = environ.get('KITTUSBOT_TOKEN') if 'KITTUSBOT_TOKEN' in environ else exit ("Telegram bot token not set")
trello_api_key = environ.get('TRELLO_APIKEY') if 'TRELLO_APIKEY' in environ else exit ("Trello API key not set")
trello_token = environ.get('TRELLO_TOKEN') if 'TRELLO_TOKEN' in environ else exit ("Trello token not set")
trello_api_url = "https://api.trello.com/1"
querystring = {"key":trello_api_key, "token":trello_token }

with open('kittusbot/base/trello_data.json', 'r') as t:
    trello_data = load(t)

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                          level=INFO)
log = getLogger('kb')
