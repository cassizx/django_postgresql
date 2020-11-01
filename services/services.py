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
            # self.connect_to_db()
    

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
        self.con.commit()
        self.query_table = table
        self.query = (f'select * from {self.query_table}')
        #time_start_qeury = datetime.now()                                                                           # Время перед началом выполнения запроса
        try:
            self.cur.execute(self.query)
            self.reqested_table = from_db_cursor(self.cur) 
            #time_end_qeury = datetime.now()                                                                             # Время получения ответа                                                   
        except psycopg2.errors.UndefinedTable as err:
            self.con.commit()
            print('Wrong table name, try again')
            #log(err , query)
            #exist_now_table()
            self.reqested_table = f'Ошибка {err}'
            return self.reqested_table
        except psycopg2.errors.SyntaxError as err:
            self.con.commit()
            print('Wrong table name, try again')
            #log(err , query)
            #exist_now_table()
            self.reqested_table = f'Ошибка {err}'
            return self.reqested_table
        else:
            #calculation_execution_time(time_start_qeury, time_end_qeury)            # Вычесление времени выполнения запроса
            #log(reqested_table, query)
            #print(reqested_table)    
            self.con.commit()
            #start()
            return self.reqested_table

        #self.reqested_table


    def new_table(self, new_table_name):
        self.query = (f"CREATE TABLE public.{new_table_name} ( id serial NOT NULL , testcomn varchar(50) NULL)")
        try:
            # time_start_qeury = datetime.now() 
            self.cur.execute(self.query)                                                                                          # Выполнение запроса
            self.con.commit()                                                                                                # Отправка изменений
            # time_end_qeury = datetime.now()
        except psycopg2.errors.DuplicateTable as err:
            self.con.commit()
            # self.cur.execute("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
            # self.exist_tables = from_db_cursor(self.cur) 
            self.exist_tables = self.exist_now_table()
            # log(err, query)
            self.resp = {
                'status': f"Table {new_table_name} is already exist.",
                'exist_tables': str(self.exist_tables)
            }
            return self.resp
            # start()
        else:
            # self.cur.execute("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
            self.exist_tables = self.exist_now_table()
            print(self.exist_tables)
            self.resp = {
                'status': f'Table {new_table_name} created.',
                'exist_tables': str(self.exist_tables)
            }
            # calculation_execution_time(time_start_qeury, time_end_qeury)
            # log(to_log_resp, query)                                                                                    
            # print(to_log_resp)
            # start()
            return self.resp
        pass    
    pass 


    def exist_now_table(self):
        self.cur.execute("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
        self.exist_tables = from_db_cursor(self.cur) 
        return self.exist_tables

    def drop_table(self, drop_table):
        # drop table    
        try:
            self.query = (f"drop table {drop_table}")
            # time_start_qeury = datetime.now()
            self.cur.execute(self.query)
            self.con.commit()     
            # resp = (f"Done.")
            # time_end_qeury = datetime.now()    
        except psycopg2.errors.UndefinedTable as err:
            # log(err, query)         
            print('Wrong table name, try again.')
            self.con.commit()
            # return exist_now_table()
            self.resp = {
                'status': 'Wrong table name, try again.', 
                'exist_tables': str(self.exist_tables)
            }
            return self.resp
        else:
            # calculation_execution_time(time_start_qeury, time_end_qeury)
            # print(resp)
            # log(resp, query)
            self.exist_now_table() 

            # self.cur.execute("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
            # self.exist_tables = from_db_cursor(self.cur) 
            self.resp = {
                'status': f'Table {drop_table} was dropped.', 
                'exist_tables': str(self.exist_tables)
            }
            return self.resp


    def his(self, reqest):
        self.status = 'Done.'
        self.query = (f'{reqest}')
        try:
            # time_start_qeury = datetime.now()
            self.cur.execute(self.query)
            self.resp = from_db_cursor(self.cur)
            # time_end_qeury = datetime.now()
        except psycopg2.InterfaceError as err:
            self.con.commit()
            print(f'Exception {err}')
            # log(err, query)
            self.status = f'Exception {err}'
            return self.status    
            # start()
        except psycopg2.ProgrammingError as err: 
            print(f'Exception {err} , try again.')
            if err == 'psycopg2.ProgrammingError: no results to fetch':
                print('Done.')
                return self.status
            # log(err, query)
            self.con.commit()
            # start()
        else:
            self.con.commit()
            if self.resp == None:
                print ('Done.')
               
                return self.status
            else:
                return self.resp 
                # calculation_execution_time(time_start_qeury, time_end_qeury)
            # else:
            #     try:
            #         # calculation_execution_time(time_start_qeury, time_end_qeury)
            #         # print(resp)
            #     except:
            #         pass
            # log(resp, query)
  

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
