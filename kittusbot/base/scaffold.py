from logging import basicConfig, getLogger, INFO, DEBUG
from os import environ

telegram_token = environ.get('KITTUSBOT_TOKEN') if 'KITTUSBOT_TOKEN' in environ else exit ("Telegram bot token not set")
trello_api_key = environ.get('TRELLO_APIKEY') if 'TRELLO_APIKEY' in environ else exit ("Trello API key not set")
trello_token = environ.get('TRELLO_TOKEN') if 'TRELLO_TOKEN' in environ else exit ("Trello token not set")

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                          level=INFO)
log = getLogger('kb')
