from django.urls import include,path
from django.conf.urls.static import static



urlpatterns = [
    path('', include('startpage.urls')),
    path('login/', include('startpage.urls')),
    path('logout/', include('startpage.urls')),
    path('main/', include('startpage.urls')) ,
    path('login/f/', include('startpage.urls')) , 
    path('create_table/', include('startpage.urls')), 
    path('drop_table/', include('startpage.urls')), 
    path('custom_query/', include('startpage.urls')), 
]