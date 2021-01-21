from django.db import models
from django.conf import settings


class UserDetail(models.Model):
    ud_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email  = models.EmailField()
    image = models.ImageField(upload_to='media/')
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class NoteShare(models.Model):
    note_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(UserDetail,on_delete=models.CASCADE, related_name='sender_id')
    reciver_id = models.ForeignKey(UserDetail,on_delete=models.CASCADE, related_name='reciver_id')
    title = models.CharField(max_length=200)
    note = models.FileField(upload_to='media/')


    def __str__(self):
        return self.title
