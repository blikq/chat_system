
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseServerError, HttpResponseBadRequest
import urllib3
from .models import DumUser, msg_db

# Create your views here.

"""
C-add data to the model(post request)
R-Read the table flawlessly
U-Edit existing data model
D-Delete data from model
"""

def send_msg(response):
    #PUT URL DECODING HERE
    #REMEMBER TO HANDLE THE ERRORS LATER
    # try:
    try:
        f_user = response.headers["fuser"]
        t_user = response.headers["tuser"]
        msg = response.headers["msg"]
    except:
        return HttpResponseBadRequest(JsonResponse({
            "success": False,
            "error": 422
        }))
    u1 = DumUser.objects.get(name=str(f_user)) # sender
    u2 = DumUser.objects.get(name=str(t_user)) # receiver
    u1.messages_sent += 1
    u2.messages_received += 1
    u1.save(); u2.save()
    msg_db.insert_one({
        "message": msg
    })

    # except:
    #     return HttpResponseServerError(JsonResponse({
    #         "success": False,
    #         "error": 500
    #     }))
    return JsonResponse({
        "success": True
    })

