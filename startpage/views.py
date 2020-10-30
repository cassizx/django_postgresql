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


#from mainpage.views import show_main_page 


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #Request_from_main_page(request)
    return render(request, 'index.html')

# def exist_now_table(con):
#     cur = con.cursor()
#     qeury=("SELECT table_name FROM information_schema.tables  WHERE table_schema='public' ORDER BY table_name")
#     cur.execute(qeury)
#     #print("Exist now table:")
#     resp = from_db_cursor(cur)
#     #print(resp)
#     #con.commit()
#     #log(resp, qeury)
#     #return start()
#     return resp

# pass

def login(request):
    #log = log(a)
    global log
    log = Request_from_main_page(request)
    #return log(request)
    #log.login(request)
    print(log)
    return log.login(request)


def f(request):
    #log = Request_from_main_page(request)
    print(log)
    return log.f(request)

def logout(request):
    #log = Request_from_main_page(request)
    return log.logout(request)

class Request_from_main_page():

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
        #pass

    # def __get__(self):
    #     self.login()
    

    def login(self, request):
        # self.dbname = request.POST['dbname']  #'postgres' #data['dbname']
        # self.user_name = request.POST['user_name'] #'postgres' #data['user_name']
        # self.psw = request.POST['psw'] #'123456789' #data['psw']
        # self.ip_adress = request.POST['ip_adress'] #'localhost' #data['ip_adress']
        # self.port = request.POST['port'] #'5432' #data['port']
        # #self.request = request
               
        # self.data = {
        #     'dbname': self.dbname,
        #     'user_name': self.user_name,
        #     'psw': self.psw,
        #     'ip_adress': self.ip_adress,
        #     'port': self.port
        # }
    
        self.conn = Work_with_db(self.data)
        self.resp = self.conn.connect_to_db()
        
        if self.resp == 'Ошибка':

            self.resp_url = "http://127.0.0.1:8000/"
            self.conn_resp = self.resp

            self.context={
            'resp' : self.conn_resp,
            'resp_url': self.resp_url
            }

            return render(request, 'resp.html', self.context)
        else:
            self.context = {
                'table': self.resp,
            }
            #return self.show_main_page( request, context)
            html = 'main.html'
            return render(request, html, self.context)
            #return JsonResponse(self.context, status = 200)
            #return HttpResponse('FUUUUCK')

            

    # def show_main_page(self, request, context):

    #     return render(request, 'main.html', context)
        # dbname = 'postgres' #data['dbname']
        # user_name = 'postgres' #data['user_name']
        # psw = '123456789' #data['psw']
        # ip_adress = 'localhost' #data['ip_adress']
        # port = '5432' #data['port']
        
        # data = {
        #     'dbname': dbname,
        #     'user_name': user_name,
        #     'psw': psw,
        #     'ip_adress': ip_adress,
        #     'port': port
        # }
        
        # # login = Work_with_db(request)
        # # data = login.login()   
        
        # conn = Work_with_db(data)
        # #conn()
        # resp = conn.connect_to_db()
        

        # if resp == 'Ошибка':

        #     resp_url = "http://127.0.0.1:8000/"
        #     conn_resp = resp

        #     context={
        #     'resp' : conn_resp,
        #     'resp_url': resp_url
        #     }

        #     return render(request, 'resp.html', context)
        # else:
        #     context = {
        #         'table': resp,
        #     }
        #     #return self.show_main_page( request, context)
        #     #return render(request, 'main.html', context)
        #     return JsonResponse(context, status = 200)
            
            

    def show_main_page(self, request, context):

        return render(request, 'main.html', context)


    def logout(self, request):
        self.resp = self.conn.disconnect_from_db()
        context = {
                'resp': self.resp
            }
        return render(request, 'logout.html', context) 


    def f(self, request):

        #self.login(request)
        self.resp_2 = self.conn.select_table(request.GET['request_data'])
        # print(self.resp_2)
        # self.context = {
        #     "resp_2": self.resp_2
        # }
        context = str(self.resp_2)
        print(context)
        return JsonResponse({'context': context}, status = 200)



#log = Request_from_main_page()

log = Request_from_main_page

