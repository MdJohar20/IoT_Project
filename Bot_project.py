import os          #operating system
import requests    #for getting data from cloud

!pip install adafruit-io
from Adafruit_IO import Client, Feed,Data                    #import libraries for adafruit
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')     #adafruit username and password should be given as 'Config Vars' in the settings of your app on Heroku 
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY') 
#these keys are from adafruit .io
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')       # create instance of REST client

!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters #importing requires handlers from telegram.ext
import requests #for getting data from cloud
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') #token is generate from telebot

# Create Feed object with name 'waltermittybot'.
#feed = Feed(name='waltermittybot')

# Send the Feed to IO to create.
# The returned object will contain all the details about the created feed.
#result = aio.create_feed(feed)
#try to run upto these in separate cell after running create a dashboard in adafruit with the feed 'projectbot' and status indicator
#to display the properties of bot feed type "result"
#result

def start(update,context):
   print(str(update.effective_chat.id))
   context.bot.send_message(chat_id=update.effective_chat.id,text="Welcome to the Walter Mitty Bot which helps you to control the switch ON and OFF of the Light. Type /lighton to Turn ON the light. Type /lightoff to Turn OFF the light. NOTE:- Here we shown the Light as Bulb image. ")
def unknown(update,context):
   context.bot.send_message(chat_id=update.effective_chat.id,text='Illegal Command')  
   
def lighton(update,context): 
    chat_id=update.message.chat_id
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light is switched ON")
    aio.create_data('waltermittybot',Data(value=1))
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
    
def lightoff(update,context):
    chat_id=update.message.chat_id
    aio.create_data('waltermittybot',Data(value=0))
    context.bot.send_message(chat_id=update.effective_chat.id,text="Light is switched OFF")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
    
def given_message(bot,update):
    text=update.message.text.upper()
    text=update.message.text

    if text =='Turn on the light':
      lighton(bot,update)
    elif text=='Turn off the light':
      lightoff(bot,update)  
    else:
      unknown(bot,update) 
      
u=Updater('TELEGRAM_TOKEN',use_context=True)             #api token of telegram bot
dp=u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))
dp.add_handler(CommandHandler('lightoff',lightoff))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.command,unknown))
dp.add_handler(MessageHandler(Filters.text,given_message))
u.start_polling()
u.idle()
