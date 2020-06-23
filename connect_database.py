import psycopg2


def connect_db():
    try:
        conn = psycopg2.connect(dbname='postgres', user='postgres', host='127.0.0.1', password='0000', port='5432')
        return conn
    except:
        print("I am unable to connect to the database")
