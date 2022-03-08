from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
"""File to keep track of the various classes that Django interacts with, each is a way to keep track of various actors and important classes they interact with"""
# Create your models here.
class Users(models.Model):
    """Class to represent a user, each has a email and password to log in with"""
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)

class UserAuthTokens(models.Model):
    """class to keep track of a user login authorization with an email a login token and a timestamp of when the login ocurred"""
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=50)

class PasswordReset(models.Model):
    """class to reset the password for a certain user"""
    email = models.CharField(max_length=50)
    resetToken = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)

class Reviews(models.Model):
    """class to keep track of a particular vreview for a restaurant and its content"""
    user = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    content = models.CharField(max_length=500)