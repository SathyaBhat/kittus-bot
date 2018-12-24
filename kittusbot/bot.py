from base.scaffold import log, telegram_token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    log.info('Got start command')
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def towatch(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=args)


def main(updater):
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    towatch_handler = CommandHandler('towatch', towatch, pass_args=True)
    dispatcher.add_handler(towatch_handler)
    log.info('Running poller')
    updater.start_polling()


if __name__=='__main__':
    updater = Updater(token=telegram_token)
    log.info('Got token: {}'.format(telegram_token))
    log.info('Running bot')
    main(updater)



