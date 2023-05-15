import telebot
import datetime
import random
import requests



# Create an instance of the Telegram bot
bot_token = "6167683526:AAGrSBZOkRvv5d4vf4DmWctUCllRvZW79ts"
bot = telebot.TeleBot(bot_token)

# Define a handler for the "Hi" message
@bot.message_handler(func=lambda message: message.text.lower() == "hi")
def handle_message(message):
    # Reply with a random greeting
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    random_greeting = random.choice(greetings)
    bot.reply_to(message, random_greeting)

# Define a handler for the "/start" command
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Reply with a random welcome message
    welcome_messages = ["Welcome!", "Nice to see you!", "Glad you're here!", "Welcome aboard!"]
    random_welcome = random.choice(welcome_messages)
    bot.reply_to(message, random_welcome)

@bot.message_handler(func=lambda message: message.text.lower() == "time")
def handle_time(message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message,f"The current time is {current_time}")




@bot.message_handler(commands=['quote'])
def handle_quote(message):
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote = response.json()["content"]
        author = response.json()["author"]
        bot.reply_to(message, f"{quote}\n- {author}")
    else:
        bot.reply_to(message, "Failed to fetch a quote.")


# Define a handler for other messages
@bot.message_handler(func=lambda message: True)
def handle_other(message):
    # Reply with a random response
    responses = ["I'm not sure what you mean.", "Could you please rephrase that?", "Sorry, I don't understand."]
    random_response = random.choice(responses)
    bot.reply_to(message, random_response)

# Start the bot
bot.polling()
