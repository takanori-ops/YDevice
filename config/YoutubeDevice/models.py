from django.contrib.auth.models import User
from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200,default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streamer = models.CharField(max_length=30)
    pic_path = models.CharField(max_length=150)
    youtube_channel = models.CharField(max_length=80)
    device1 = models.CharField(max_length=30)
    device1_spec= models.CharField(max_length=30)
    device2 = models.CharField(max_length=30,default=None, blank=True, null=True)
    device2_spec= models.CharField(max_length=30,default=None, blank=True, null=True)
    viewed_count = models.PositiveIntegerField(default=0) 
    gametitle = models.CharField(max_length=30,default=None, blank=True, null=True) 

    def __str__(self):
        return self.title
    

