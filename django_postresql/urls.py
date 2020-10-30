from django.urls import include,path
from django.conf.urls.static import static



urlpatterns = [
    path('', include('startpage.urls')),
    path('login/', include('startpage.urls')),
    #path('login/logout/', include('mainpage.urls')),
    path('logout/', include('startpage.urls')),
    path('main/', include('mainpage.urls')) ,
    #path('login/main/', include('mainpage.urls')) ,
    #path('f/', include('mainpage.urls')),
    #path('login/f/', include('mainpage.urls'))  
    path('login/f/', include('startpage.urls'))   
]