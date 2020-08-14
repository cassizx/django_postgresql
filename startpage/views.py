from django.shortcuts import render
#from django.http import HttpResponse
from services.services import connection, disconnect_from_db
from prettytable import from_db_cursor
from django.conf import settings
from django.conf.urls.static import static



def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    f = 'STATIC_URL'
    context = {
        'f':f
    }
    return render(request, 'index.html', context)

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

    dbname = request.POST['dbname']
    user_name = request.POST['user_name']
    psw = request.POST['psw']
    ip_adress = request.POST['ip_adress']
    port = request.POST['port']
    
    context = {
        'dbname': dbname,
        'user_name': user_name,
        'psw': psw,
        'ip_adress': ip_adress,
        'port': port
    }
    
    conn = connection(context)
    if conn == 'Ошибка':
        return render(request, 'index.html', context={
           'resp' : conn 
        })
    else:
        context = {
            'table': conn
        }
        return render(request, 'resp.html', context)

def logout(request):

    resp = disconnect_from_db(request)
    context = {
        'resp': resp
    }
    return render(request, 'logout.html', context) 