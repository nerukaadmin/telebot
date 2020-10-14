#https://pypi.org/project/telebot/ #pip3 install telebot
import telebot
from datetime import *
import subprocess as sub
import sys

bot = telebot.TeleBot("874510512:AAFvW_lKUykkCjE0F5KSBPZpe5XtFTmNDwo")
stamp=datetime.now()
date=stamp.strftime("%c")
print(date)
print("Up")
chat_id="440074848"

bot.send_message(chat_id,"Hi sir! It's"+" "+date+"\n"+"I hope you are doing good !")
bot.send_message(chat_id,"Now i am sending your server report !")

exe=sub.Popen(['uptime'],stdout=sub.PIPE,shell=False,universal_newlines=True)
t=exe.communicate()[0]
bot.send_message(chat_id,"Server Up Time"+"\n"+t)
#exe=sub.Popen(['/sbin/ifconfig','-a'],stdout=sub.PIPE,shell=False,universal_newlines=True)
#t1=exe.communicate()[0]
#bot.send_message(chat_id,"Server Network details."+"\n"+t1)
exe=sub.Popen(['/bin/df','-h'],stdout=sub.PIPE,shell=False,universal_newlines=True)
t2=exe.communicate()[0]
bot.send_message(chat_id,"Disk Usage."+"\n"+t2)
exe=sub.Popen(['/usr/bin/iostat','-mx'],stdout=sub.PIPE,shell=False,universal_newlines=True)
t3=exe.communicate()[0]
bot.send_message(chat_id,"Server CPU status."+"\n"+t3)
exe=sub.Popen(['/usr/bin/docker','images'],stdout=sub.PIPE,shell=False,universal_newlines=True)
t4=exe.communicate()[0]
bot.send_message(chat_id,"Docker Images."+"\n"+t4)
exe=sub.Popen(['/usr/bin/docker','ps','-a'],stdout=sub.PIPE,shell=False,universal_newlines=True)
t5=exe.communicate()[0]
bot.send_message(chat_id,"Docker Status."+"\n"+t5)                



bot.polling(none_stop=False,interval=0,timeout=10)

