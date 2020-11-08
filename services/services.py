from datetime import datetime 
import os
import psycopg2
from prettytable import PrettyTable 
from prettytable import from_db_cursor
from datetime import datetime 
from time import sleep
#from startpage.views import connection


class Work_with_db():


    def __init__(self, data):
        self.dbname = data['dbname']
        self.user_name = data['user_name']
        self.psw = data['psw']
        self.ip_adress = data['ip_adress']
        self.port = data['port']
    

    def connect_to_db(self):
        try:       
            self.con = psycopg2.connect(                                                           #Для выполнения запроса к базе, необходимо с ней соединиться и получить курсор.
                database = self.dbname, user = self.user_name, password = self.psw, 
                host = self.ip_adress, port = self.port
                )        
            self.cur = self.con.cursor()                                                      #Через курсор происходит дальнейшее общение в базой.
            self.resp = self.exist_now_table()
            self.log(f"Succes\n{self.resp}", self.con)
        except psycopg2.OperationalError as err:
            self.log(err, 'Login error')
            return f'Ошибка'
        else:   
            return str(self.resp)
    

    def calculation_execution_time(self, time_start, time_end):
        self.execution_time = time_end - time_start
        return f"Запрос выполнен за {self.execution_time}"


    def select_table(self, table):
        self.con.commit()
        self.query_table = table
        self.query = (f'select * from {self.query_table}')
        self.time_start_qeury = datetime.now()                                                                           # Время перед началом выполнения запроса
        try:
            self.cur.execute(self.query)
            self.reqested_table = from_db_cursor(self.cur) 
            self.time_end_qeury = datetime.now()                                                                             # Время получения ответа                                                   
        except psycopg2.errors.UndefinedTable as err:
            self.time_end_qeury = datetime.now()
            self.con.commit()
            self.execution_time_resp = self.calculation_execution_time(self.time_start_qeury, self.time_end_qeury)            # Вычесление времени выполнения запроса
            self.select_table_response = {
                'reqested_table': 'Wrong table name, try again',
                'execution_time': self.execution_time_resp 
            }
            self.log(err , self.query)
            return self.select_table_response
        except psycopg2.errors.SyntaxError as err:
            self.con.commit()
            self.reqested_table = f'Ошибка {err}'
            self.log(err , self.query)
            return self.reqested_table
        else:
            self.execution_time_resp = self.calculation_execution_time(self.time_start_qeury, self.time_end_qeury)            # Вычесление времени выполнения запроса
            self.con.commit()
            self.select_table_response = {
                'reqested_table':self.reqested_table,
                'execution_time': self.execution_time_resp 
            }
            self.log(self.reqested_table, self.query) 
            return self.select_table_response


    def new_table(self, new_table_name):
        self.query = (f"CREATE TABLE public.{new_table_name} ( id serial NOT NULL , testcomn varchar(50) NULL)")
        try:
            # time_start_qeury = datetime.now() 
            self.cur.execute(self.query)                                                                                          # Выполнение запроса
            self.con.commit()                                                                                                # Отправка изменений
            # time_end_qeury = datetime.now()
        except psycopg2.errors.DuplicateTable as err:
            self.con.commit()
            self.exist_tables = self.exist_now_table()    
            self.resp = {
                'status': f"Table {new_table_name} is already exist.",
                'exist_tables': str(self.exist_tables)
            }
            self.log(self.resp, self.query)
            return self.resp
        else:
            self.exist_tables = self.exist_now_table()
            self.resp = {
                'status': f'Table {new_table_name} created.',
                'exist_tables': str(self.exist_tables)
            }
            # calculation_execution_time(time_start_qeury, time_end_qeury)
            self.log(self.resp, self.query)                                                                                    
            return self.resp


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
            # time_end_qeury = datetime.now()    
        except psycopg2.errors.UndefinedTable as err:       
            self.con.commit()
            self.resp = {
                'status': f'Wrong table name, table {drop_table} not exist, try again.', 
                'exist_tables': str(self.exist_now_table())
            }
            self.log(self.resp, self.query)
            return self.resp
        else:
            # calculation_execution_time(time_start_qeury, time_end_qeury)
            self.resp = {
                'status': f'Table {drop_table} was dropped.', 
                'exist_tables': str(self.exist_now_table())
            }
            self.log(self.resp, self.query)
            return self.resp


    def his(self, reqest):
        self.status = 'Done.'
        self.query = (f'{reqest.strip()}')
        try:
            # time_start_qeury = datetime.now()
            self.cur.execute(self.query)
            self.resp = from_db_cursor(self.cur)
            # time_end_qeury = datetime.now()
        except psycopg2.InterfaceError as err:
            self.con.commit()
            self.status = f'Exception {err}'
            self.log(err, self.query)
            return self.status    
        except psycopg2.ProgrammingError as err: 
            if err == 'psycopg2.ProgrammingError: no results to fetch':
                self.log(self.status, self.query)
                return self.status
            else:
                self.con.commit()
                self.log(err, self.query)
                return err
        else:
            self.con.commit()
            if self.resp == None:
                self.log(self.status, self.query)
                return self.status
            else:
                self.log(self.resp, self.query)
                return self.resp 
                # calculation_execution_time(time_start_qeury, time_end_qeury)
    

    def disconnect_from_db(self):
        try:
            # self.cur.commit()
            self.cur.close()
            self.log('Disconnected','Disconnect')
        except Exception as err:
            return f'Error {err}'
        else:
            return f'Disconnected.'


    def log(self, resp, reqest='what_do'):
        date = datetime.date(datetime.now())
        file_with_log = (f"log{date}.log")                                                       # Создание названия файла   
        with open(file_with_log, 'a') as write_to_file:                                             # Открытие файла лога в режиме a - добавления записи в конец
            write_to_file.write("-----Start new query.-----\n")
            write_to_file.write(f"Time: {datetime.now()} \nQeury: {reqest} \nRespone:\n")
            write_to_file.write(str(resp))
            write_to_file.write("\n-----End of qeury.----- \n")

