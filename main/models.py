from django.db import models
from django.utils import timezone
# Create your models here.

class DumUser(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class DumMsg(models.Model):
    r_id = models.ForeignKey(DumUser, on_delete=models.CASCADE)
    # change messages limit here
    time = models.TimeField(max_length=1500, default=timezone.now())
    msg = models.CharField(max_length=1500, null=False)
    sender = models.CharField(max_length=1500, null=True)
    receiver = models.CharField(max_length=1500, null=True)
    if_sender = models.BooleanField(default=False)
    if_rec = models.BooleanField(default=False)

    def __str__(self):
        return {
            "user": {self.r_id},
            "time": {self.time},
            "sent_msg": {self.sent_msg},
            "rec_msg": {self.rec_msg},
            "sender": {self.sender},
            "receiver": {self.receiver},
        }


class FailedMsg(models.Model):
    time = models.TimeField(max_length=1500, default=timezone.now())
    msg = models.CharField(max_length=1500, null=False)
    sender = models.CharField(max_length=1500, null=True)
    receiver = models.CharField(max_length=1500, null=True)
    