from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'tictactoe'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.tictactoe, name='detail')
]
