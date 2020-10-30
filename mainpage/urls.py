from django.urls import include,path
from django.conf.urls.static import static
from . import views


urlpatterns = [
#path('main/', views.show_main_page),
path('', views.show_main),
#path('logout/', views.logout),
#path('f/', views.f),
#path('login/f/', views.f)
]