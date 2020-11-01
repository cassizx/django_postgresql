from django.shortcuts import render
from services.services import Work_with_db
from prettytable import from_db_cursor
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import View
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.shortcuts import redirect



#from mainpage.views import show_main_page 


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #Request_from_main_page(request)
    return render(request, 'index.html')


def login(request):
    global log
    if request.method == 'POST':   
        log = Request_from_main_page(request)
        print(log)
        return log.login(request)
    else:
        context = {
            'response': 'Dont loginned.'
        }
        return render(request, 'eror.html', context)


def select_from_table(request):
    if request.is_ajax():    
        print(log)
        return log.select_from_table(request)
    else:
           return JsonResponse({'Erorr':'Erorr'}, status=400) 
    

def logout(request):  
    # cache.clear() 
    return log.logout(request)
    

def create_table(request):
    if request.is_ajax():  
        return log.create_table(request)
    else:
        return JsonResponse({'Erorr':'Erorr'}, status=400) 

def drop_table(request):
    if request.is_ajax():  
        return log.drop_table(request)
    else:
        return JsonResponse({'Erorr':'Erorr'}, status=400) 

def custom_query(request):
    if request.is_ajax():  
        return log.custom_query(request)
    else:
        return JsonResponse({'Erorr':'Erorr'}, status=400) 


class Request_from_main_page():
    ''' Класс для отправки запросов к сервису работы с БД'''

    def __init__(self, request):
        self.dbname = request.POST['dbname']  #'postgres' #data['dbname']
        self.user_name = request.POST['user_name'] #'postgres' #data['user_name']
        self.psw = request.POST['psw'] #'123456789' #data['psw']
        self.ip_adress = request.POST['ip_adress'] #'localhost' #data['ip_adress']
        self.port = request.POST['port'] #'5432' #data['port']
        #self.request = request
               
        self.data = {
            'dbname': self.dbname,
            'user_name': self.user_name,
            'psw': self.psw,
            'ip_adress': self.ip_adress,
            'port': self.port
        }


    def login(self, request):   
        self.conn = Work_with_db(self.data)
        self.resp = self.conn.connect_to_db()
        
        if self.resp == 'Ошибка':

            self.resp_url = "http://127.0.0.1:8000/"
            self.conn_resp = self.resp

            self.context={
            'resp' : self.conn_resp,
            'resp_url': self.resp_url,
            }

            return render(request, 'resp.html', self.context)
        else:
            self.context = {
                'table': self.resp,
                'dbname': self.dbname
            }
            html = 'main.html'
            return render(request, html, self.context)


    def logout(self, request):
        try:
            self.resp = self.conn.disconnect_from_db()
        except Exception as err:
            context = {
                    'response': 'Except {err}'
                }
            return render(request, 'eror.html', context) 
        else:
            context = {
                    'resp': self.resp
                }
            return render(request, 'logout.html', context) 


    def select_from_table(self, request):
        #self.login(request)
        self.resp_2 = self.conn.select_table(request.GET['request_data'])
        # print(self.resp_2)
        # self.context = {
        #     "resp_2": self.resp_2
        # }
        context = str(self.resp_2)
        print(context)
        return JsonResponse({'context': context}, status = 200)


    def create_table(self, request):
        self.table_name = request.POST['table_name_to_create']
        print('create_table', self.table_name)
        self.resp = self.conn.new_table(self.table_name)
        # self.exist_tables = self.resp
        return JsonResponse({'exist_tables' : self.resp['exist_tables'], 'status': self.resp['status']}, status=200)


    def custom_query(self, request):
        self.query = request.POST['custom_query']
        print(self.query)
        self.custom_query_resp = self.conn.his(self.query )
        print(self.custom_query_resp)
        return JsonResponse({'custom_query_resp':str(self.custom_query_resp)}, status=200)


    def drop_table(self, request):
        self.table_name_to_drop = request.POST['table_name_to_drop']
        print('Table to drop ',self.table_name_to_drop)
        self.resp = self.conn.drop_table(self.table_name_to_drop)
        return JsonResponse({'exist_tables' : self.resp['exist_tables'], 'status': self.resp['status']}, status=200)

