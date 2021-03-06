# -*- coding: utf-8 -*-
# Example code for telegrambot.py module
from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
from django.contrib.auth.models import User
from loginsys.models import Link_with_email

import logging
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    row_personal_id = update.message.text
    personal_id = row_personal_id[7:]
    chat_id = update.message.chat_id
    our_user = User.objects.get(pk = personal_id)
    link = Link_with_email.objects.create(email = our_user.email,chat_id = chat_id,get_notice = True)
    link.save()
    bot.sendMessage(update.message.chat_id, text=our_user.email)


def startgroup(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')
    #bot.sendMessage(update.message.chat_id, text=update.start)



def me(bot, update):
    bot.sendMessage(update.message.chat_id, text='Your information:\n{}'.format(update.effective_user))


def chat(bot, update):
    bot.sendMessage(update.message.chat_id, text='This chat information:\n {}'.format(update.effective_chat))


def forwarded(bot, update):
    bot.sendMessage(update.message.chat_id, text='This msg forwaded information:\n {}'.format(update.effective_message))


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for telegram bot")

    # Default dispatcher (this is related to the first bot in settings.TELEGRAM_BOT_TOKENS)
    dp = DjangoTelegramBot.dispatcher
    # To get Dispatcher related to a specific bot
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_token')     #get by bot token
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_username')  #get by bot username

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("startgroup", startgroup))
    dp.add_handler(CommandHandler("me", me))
    dp.add_handler(CommandHandler("chat", chat))
    dp.add_handler(MessageHandler(Filters.forwarded , forwarded))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)


