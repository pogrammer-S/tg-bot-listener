FROM python
WORKDIR /app
COPY Main.py /app/Main.py
COPY init.sql /app/init.sql
RUN pip install telebot
RUN pip install dotenv
RUN pip install psycopg2
ENTRYPOINT ["python", "Main.py"]