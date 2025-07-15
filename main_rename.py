from scr.bot.bot import bot 
from scr.database.connection import connection
from scr.bot.listener import *

bot.polling()
connection.close()