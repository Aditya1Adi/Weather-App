from django.contrib import admin
from django.urls import path,include

# from . import views

# C:\Users\Admin\Desktop\kalvium\Myproject\Myapp\views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Myapp.urls')), 
    # path('get_weather/', views.get_weather, name='get_weather'),
]
