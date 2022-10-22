from django.urls import path
from .views import send_msg

urlpatterns = [
    path('apiv1/send/', send_msg, name = 'Send_messages')
]

