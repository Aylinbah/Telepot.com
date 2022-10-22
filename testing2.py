import sys
import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    #print 'Got command: %s' % command
   
    if command == 'command1': 
        bot.sendMessage(chat_id="5420353293", text='Yo bruh')
    elif command == 'command2':
        bot.sendMessage(chat_id="5420353293", text='Im NEZUKO CHANNNN')
    elif command == 'photo':
        bot.sendMessage(chat_id="5420353293", text="https://thecinemaholic.com/wp-content/uploads/2021/01/nezuu-e1638963260523.jpg")

bot = telepot.Bot('5527673378:AAHDDAdEFs1nM5l4J6Hb2Sba0_2AUqfeE7I')
bot.message_loop(handle)

while 1:
    time.sleep(10)