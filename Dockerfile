FROM python
WORKDIR /app
COPY Main.py /app/Main.py
COPY Bot_Listener/Bot.py /app/Bot_Listener/Bot.py
COPY Bot_Listener/listener.py /app/Bot_Listener/listener.py
COPY SQL_Con/ConnectionSQL.py /app/SQL_Con/ConnectionSQL.py
COPY Bot_Listener/__init__.py /app/Bot_Listener/__init__.py
COPY SQL_Con/init.sql /app/SQL_Con/init.sql
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt   
ENTRYPOINT ["python", "Main.py"]