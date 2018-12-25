from base.scaffold import log, telegram_token
from trello.trello import add_to_trello_list
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from requests import codes

def start(bot, update):
    log.info('Got start command')
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def to_watch(bot, update, args):
    message, status_code = add_to_trello_list('to_watch', 'card', update, args)
    bot.send_message(chat_id=update.message.chat_id, text=message)


def main(updater):
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    to_watch_handler = CommandHandler('towatch', to_watch, pass_args=True)
    dispatcher.add_handler(to_watch_handler)
    log.info('Running poller')
    updater.start_polling()


if __name__=='__main__':
    updater = Updater(token=telegram_token)
    log.info('Got token: {}'.format(telegram_token))
    log.info('Running bot')
    main(updater)



