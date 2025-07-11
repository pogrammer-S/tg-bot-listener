from Bot_Listener.Bot import bot 
from SQL_Con.ConnectionSQL import connection
from Bot_Listener.listener import *

bot.polling()
connection.close()