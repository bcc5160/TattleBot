########
#
#   TinyDB and pyTelegramBotAPI
#
######

import telebot
import configparser

# Parse config to get the API key
config = configparser.ConfigParser()
config.read("tattle_bot.cfg")

TOKEN = config['telegram_bot_api']['telegram_token']

# Declare a bot instance
bot = telebot.TeleBot(TOKEN)

# Message handler for the cmds: '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome_message(message):
        bot.reply_to(message, "Ask me who did it! I know.")

# Message Handler for telling bot your secrets (AKA Join group)
@bot.message_handler(commands=['join'])

