from django.urls import path
from .views import send_msg

urlpatterns = [
    path('<str:f_user>/send/<str:t_user>/<str:msg>', send_msg, name = 'Send_messages')
]

