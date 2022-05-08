from django.urls import path
from .views import sendData
from . import views


urlpatterns = [
    path('', sendData,name="home"),
    path(r'delete/<id>/', views.deleteTodo,name="del"),
]
