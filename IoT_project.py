pip install adafruit-io
x = "ADAFRUIT_IO_USERNAME" 
y = "ADAFRUIT_IO_KEY" 
from Adafruit_IO import Client, Feed
aio = Client(x,y)
# Create a feed
new = Feed(name='walter_mitty_bot')  # Feed name is given "walter_mitty_bot"
result = aio.create_feed(new)
result
from Adafruit_IO import Data
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('walter_mitty_bot',Data(value = 1))
  bot.send_message(chat_id ,text ="Light ON")
  bot.send_photo(chat_id, photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
  

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('walter_mitty_bot',Data(value = 0))
  bot.send_message(chat_id, text ="Light OFF")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')

updater = Updater('TELEGRAM_TOKEN')     #Use Telegram Token HTTP API
dp =updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
