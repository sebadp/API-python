from django.urls import path, include
from .views import home, removeCity

urlpatterns = [
    path('home/', home , name='home'),
    path('delete/<city>', removeCity, name='delete')
] 