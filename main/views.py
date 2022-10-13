
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import urllib3
from .models import DumUser, FailedMsg

# Create your views here.

"""
C-add data to the model(post request)
R-Read the table flawlessly
U-Edit existing data model
D-Delete data from model
"""

def send_msg(response, f_user:str, t_user:str, msg):
    #PUT URL DECODING HERE
    try:
        u1 = DumUser(name=f_user) # sender
        u2 = DumUser(name=t_user) # receiver
        u1.dummsg_set.create(msg=msg, sender = f_user,receiver=t_user, if_sender=True)
        u1.save()
        u2.dummsg_set.create(msg=msg, sender=f_user, receiver=t_user, if_rec=True)
        u2.save()
    except:
        a = FailedMsg(msg=msg, sender=f_user, receiver=t_user)
        a.save()
        return JsonResponse({
        "success": False
        })
    return JsonResponse({
        "success": True
    })
    # pass


