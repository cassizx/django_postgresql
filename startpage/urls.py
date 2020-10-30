from django.urls import path
from .views import Request_from_main_page, index, login,f, logout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', index),
    path('', index),
    path('login/', login),
    #path('login/', Request_from_main_page.login),
    #path('logout/', Request_from_main_page.logout),
    path('logout/',logout),
    #path('f/', Request_from_main_page.f), 
    path('f/', f),    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)