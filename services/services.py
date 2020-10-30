from datetime import datetime 
import os
import psycopg2
from prettytable import PrettyTable 
from prettytable import from_db_cursor
#from startpage.views import connection


class Work_with_db():

    def __init__(self, data):
            self.dbname = data['dbname']
            self.user_name = data['user_name']
            self.psw = data['psw']
            self.ip_adress = data['ip_adress']
            self.port = data['port']
            self.connect_to_db()
    

    def connect_to_db(self):
        try:       
            self.con = psycopg2.connect(                                                           #Для выполнения запроса к базе, необходимо с ней соединиться и получить курсор.
                database = self.dbname, user = self.user_name, password = self.psw, 
                host = self.ip_adress, port = self.port
                )        
            self.cur = self.con.cursor()                                                      #Через курсор происходит дальнейшее общение в базой.
            #resp = ("Database opened successfully.")
            #file_with_data.close()
            #print(resp)
            #log(resp, con)
            #print(exist_now_table())                                                # Покажет сущуствующие таблицы и вызовит функцию start, при большом количестве таблиц
            #start() # Вызывается из exist_now_table()                              # закомментировать и расскомментировать start()
            #pass
            self.qeury = ("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
            self.cur.execute(self.qeury)
            #print("Exist now table:")
            #resp = from_db_cursor(cur)
            self.resp = from_db_cursor(self.cur)
        except psycopg2.OperationalError as err:
            #log(err, read_connection_data)
            #print('Connection eror, check data to connect.')
            #print(read_connection_data)
            return f'Ошибка'
            
        return f'{ self.resp }'


    def select_table(self, table):
        #con.commit()
        self.query_table = table
        self.query = (f'select * from {self.query_table}')
        #time_start_qeury = datetime.now()                                                                           # Время перед началом выполнения запроса
        try:
            self.cur.execute(self.query)
            self.reqested_table = from_db_cursor(self.cur) 
            #time_end_qeury = datetime.now()                                                                             # Время получения ответа                                                   
        except psycopg2.errors.UndefinedTable as err:
            #con.commit()
            print('Wrong table name, try again')
            #log(err , query)
            #exist_now_table()
            self.reqested_table = 'Ошибка'
        else:
            #calculation_execution_time(time_start_qeury, time_end_qeury)            # Вычесление времени выполнения запроса
            #log(reqested_table, query)
            #print(reqested_table)    
            #con.commit()
            #start()
            return self.reqested_table

        #self.reqested_table



    def disconnect_from_db(self):
        #self.cur.commit()
        self.cur.close()
        return f'Disconnected.'


# class Work_with_db():

#     def __init__(self, data):
#         self.dbname = data.POST['dbname']
#         self.user_name = data.POST['user_name']
#         self.psw = data.POST['psw']
#         self.ip_adress = data.POST['ip_adress']
#         self.port = data.POST['port']
    
#     def login(self):
#         data_to_conn = {
#         'dbname': self.dbname,
#         'user_name': self.user_name,
#         'psw': self.psw,
#         'ip_adress': self.ip_adress,
#         'port': self.port
#         }   
    
#         conn = Connection(data_to_conn)
#         return conn
