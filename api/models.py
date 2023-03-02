from django.db import models

class User(models.Model):
    user = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

