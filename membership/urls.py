from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('submitted/', views.insert),
    path('admin1/', views.adm, name='ad1'),
    path('process/', views.proc),
]
