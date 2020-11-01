from django.urls import path
from .views import Request_from_main_page, index, login, select_from_table, logout, create_table, drop_table, custom_query
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', index),
    path('', index),
    path('login/', login),
    path('main/', login),
    #path('logout/', Request_from_main_page.logout),
    path('logout/',logout),
    #path('f/', Request_from_main_page.f), 
    path('select_from_table/', select_from_table), 
    path('create_table/', create_table),     
    path('drop_table/', drop_table), 
    path('custom_query/', custom_query),
]