from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from itertools import chain

# Create your models here.
"""File to keep track of the various classes that Django interacts with, each is a way to keep track of various actors and important classes they interact with"""
# Create your models here.
class Users(models.Model):
    """Class to represent a user, each has a email and password to log in with"""
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=50, default="")
    num_bookings = models.IntegerField(default=0)
    member_since = models.DateField(auto_now_add=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    cuisine = models.CharField(max_length=50, blank=True, null=True)
    average_rating = models.DecimalField(decimal_places=3, max_digits=4, default=0)
    num_reviews = models.IntegerField(default=0)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserAuthTokens(models.Model):
    """class to keep track of a user login authorization with an email a login token and a timestamp of when the login ocurred"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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
def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data
