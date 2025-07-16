import psycopg2 #pip install psycopg2

try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "322692",
        database = "postgres"
    )
    connection.autocommit = True

    ##with connection.cursor() as cursor:
        ##cursor.execute("CREATE TABLE users(id serial PRIMARY KEY, first_name varchar(50) NOT NULL, nick_name varchar(50) NOT NULL)")

    #with connection.cursor() as cursor:
        #cursor.execute("INSERT INTO users (first_name, nick_name) VALUES('Test1', 'test_nick1')")

    #with connection.cursor() as cursor:
        #cursor.execute("SELECT nick_name FROM users WHERE id = '2'")
        #print(cursor.fetchone())

    #with connection.cursor() as cursor:
        #cursor.execute("drop table users;")

except Exception as ex:
    print("Error:"+ ex)
finally:
    if connection:
        connection.close()