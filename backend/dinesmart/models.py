from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)

class UserAuthTokens(models.Model):
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=50)

class PasswordReset(models.Model):
    email = models.CharField(max_length=50)
    resetToken = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
