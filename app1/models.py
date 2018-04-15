from django.db import models
import datetime


class Users(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Events(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length =200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField('date of event')
    attended_or_not = models.CharField(max_length=20,default="NO")

    def __str__(self):
        return self.title



