from datetime import datetime 
import os
import psycopg2
from prettytable import PrettyTable 
from prettytable import from_db_cursor
#from startpage.views import connection


def connection(data):

    read_connection_data = data

    try:       
        
        con = psycopg2.connect(                                                           #Для выполнения запроса к базе, необходимо с ней соединиться и получить курсор.
            database = read_connection_data['dbname'], user = read_connection_data['user_name'], password = read_connection_data['psw'], 
            host = read_connection_data['ip_adress'], port = read_connection_data['port']
            )        
        cur = con.cursor()                                                      #Через курсор происходит дальнейшее общение в базой.
        #resp = ("Database opened successfully.")
        #file_with_data.close()
        #print(resp)
        #log(resp, con)
        #print(exist_now_table())                                                # Покажет сущуствующие таблицы и вызовит функцию start, при большом количестве таблиц
        #start() # Вызывается из exist_now_table()                              # закомментировать и расскомментировать start()
        #pass
        #qeury=("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
        #cur.execute(qeury)
         #print("Exist now table:")
        #resp = from_db_cursor(cur)
        resp = cur
    except psycopg2.OperationalError as err:
        #log(err, read_connection_data)
        #print('Connection eror, check data to connect.')
        #print(read_connection_data)
        return f'Ошибка'
        
    return f'{resp}'

def disconnect_from_db(request):

    #cur.commit()
    #cur.close()
    return f'Disconnected.{request}'