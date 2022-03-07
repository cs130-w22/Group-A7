from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50)
    num_bookings = models.IntegerField(default=0)
    member_since = models.CharField(default='xx', max_length=50)

class Restaurant(models.Model):
    location = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    average_rating = models.DecimalField
    num_reviews = models.IntegerField

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    content = models.CharField(max_length=500)

class UserAuthTokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=50)

class PasswordReset(models.Model):
    email = models.CharField(max_length=50)
    resetToken = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)