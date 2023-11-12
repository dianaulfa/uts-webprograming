from django.contrib import admin
from django.urls import path
from berita.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beranda, name='beranda'),
    path('about/', about, name='about'),
    path('coba/', coba, name='coba'),
    path('index/',index, name='index'),

]
