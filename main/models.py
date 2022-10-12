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
    sent_msg = models.CharField(max_length=1500, null=True, default=None)
    rec_msg = models.CharField(max_length=1500, null=True, default=None)

    def __str__(self):
        return {
            "user": {self.r_id},
            "time": {self.time},
            "sent_msg": {self.sent_msg},
            "rec_msg": {self.rec_msg}
        }
