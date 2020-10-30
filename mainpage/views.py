from django.shortcuts import render
from services.services import Work_with_db
from prettytable import from_db_cursor
from django.conf import settings
from django.http import HttpResponseRedirect



# def show_main_page(request, context):

#     return render(request, 'main.html', context)
#     #return HttpResponseRedirect('main')
#     #render(request, 'main.html', context)


# def f(request):
    
#     context = {
#         "context":request.__dict__
#     }
#     return render(request, 'main.html', context)


# def logout(request):
#     #conn = Work_with_db()
#     with login:
#         resp = Work_with_db.disconnect_from_db()

#         context = {
#             'resp': resp
#         }
#     return render(request, 'logout.html', context) 


def show_main(request):
    return render(request, 'main.html')