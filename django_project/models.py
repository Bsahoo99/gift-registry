from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class Gift(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
