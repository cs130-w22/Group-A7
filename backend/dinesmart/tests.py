from unicodedata import ucd_3_2_0
from django.test import TestCase
from django.urls import reverse
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from dinesmart.models import User, UserAuthTokens, PasswordReset, Review, Restaurant, UserProfile, to_dict

class UserTestCase(TestCase):
    def setUpTestData():
        #User create
        User.objects.create(email="a1@gmail.com", password="pass")
        User.objects.create(email="a2@gmail.com", password="pass")
        User.objects.create(email="a3@gmail.com", password="pass")
        a1 = User.objects.get(email="a1@gmail.com")
        a2 = User.objects.get(email="a2@gmail.com")
        a3 = User.objects.get(email="a3@gmail.com")
        
        #UserProfile create
        UserProfile.objects.create(user=a1)
        UserProfile.objects.create(user=a2, name="Bob", location="Los Angeles", num_bookings=1)
        UserProfile.objects.create(user=a3, name = "Tom", location="Westwood")
        
        #Restaurant create
        Restaurant.objects.create(name="Chipotle", location="Westwood", cuisine="Mexican")
        Restaurant.objects.create(name="Cava", location="Westwood", cuisine="Mediterranean")
        r1 = Restaurant.objects.get(name="Chipotle")
        r2 = Restaurant.objects.get(name="Cava")
        
        #Review create
        Review.objects.create(user=a2, restaurant=r1, rating = 5, content="I love it")
        Review.objects.create(user=a3, restaurant=r1, rating = 1, content="I hate it")
        Review.objects.create(user=a3, restaurant=r2, rating = 3, content="It's okay")

        #UserAuthTokens
        UserAuthTokens.objects.create(user=a2, email="a2@gmail.com", token="tmptoken1", timestamp="12:00:00")
        UserAuthTokens.objects.create(user=a3, email="a3@gmail.com", token="tmptoken2", timestamp="01:00:00")
        
        #PasswordReset
        PasswordReset.objects.create(email="a2@gmail.com", resetToken="tmptoken1", timestamp="12:00:00")
        PasswordReset.objects.create(email="a3@gmail.com", resetToken="tmptoken2", timestamp="01:00:00")

    def testUsers(self):
        
        #test Users are added properly
        a1 = User.objects.get(email="a1@gmail.com")
        a2 = User.objects.get(email="a2@gmail.com")
        self.assertEqual(a1.password, "pass")
        self.assertEqual(a2.password, "pass")
        a1profile = UserProfile.objects.get(user=a1)
        a2profile = UserProfile.objects.get(user=a2)
        
        #test Userprofile objects are created and defaults
        self.assertEqual(a1profile.name,"")
        self.assertEqual(a1profile.location, "")
        self.assertEqual(a1profile.num_bookings,0)
        self.assertEqual(a1profile.member_since, date.today())

        #test Userprofile after updates
        a2profile = UserProfile.objects.get(user=a2)
        self.assertEqual(a2profile.name,"Bob")
        self.assertEqual(a2profile.location, "Los Angeles")
        self.assertEqual(a2profile.num_bookings,1)

        #test that User deletion deletes UserProfile
        a1.delete()
        try:
            a1profile = UserProfile.objects.get(user=a1)
        except UserProfile.DoesNotExist:
            a1profile=None
        self.assertEqual(None,a1profile)
   


    def testRestaurants(self):
        #get Restaurants
        r1=Restaurant.objects.get(name="Chipotle")
        r2=Restaurant.objects.get(name="Cava")

        #check values
        self.assertEqual(r1.location, "Westwood")
        self.assertEqual(r2.location, "Westwood")
        self.assertEqual(r1.cuisine, "Mexican")
        self.assertEqual(r2.cuisine, "Mediterranean")
        self.assertEqual(r1.cuisine, "Mexican")
        self.assertEqual(r2.cuisine, "Mediterranean")
        
    def testReviews(self):
        #Get users and restaurants and reviews
        a2 = User.objects.get(email="a2@gmail.com")
        a3 = User.objects.get(email="a3@gmail.com")
        r1=Restaurant.objects.get(name="Chipotle")
        r2=Restaurant.objects.get(name="Cava")
        Rev1 = Review.objects.get(user=a2, restaurant=r1)
        Rev2 = Review.objects.get(user=a3, restaurant=r1)
        Rev3 = Review.objects.get(user=a3, restaurant=r2)

        #check values
        self.assertEqual(Rev1.rating,5)
        self.assertEqual(Rev2.rating,1)
        self.assertEqual(Rev3.rating,3)
        self.assertEqual(Rev1.content, "I love it")
        self.assertEqual(Rev2.content, "I hate it")
        self.assertEqual(Rev3.content, "It's okay")
    
        r2.delete()
        try:
            revtemp1 = Review.objects.get(user=a3, restaurant=r2)
        except Review.DoesNotExist:
            revtemp1=None

        self.assertEqual(None,revtemp1)

        a3.delete()
        try:
            revtemp2 = Review.objects.get(user=a3, restaurant=r1)
        except Review.DoesNotExist:
            revtemp2=None
        self.assertEqual(None,revtemp2)

    def testPasswordReset(self):
        #get PasswordResets
        p2 = PasswordReset.objects.get(email="a2@gmail.com")
        p3 = PasswordReset.objects.get(email="a3@gmail.com")

        #check values
        self.assertEqual(p2.resetToken,"tmptoken1")
        self.assertEqual(p3.resetToken,"tmptoken2")
        self.assertEqual(p2.timestamp,"12:00:00")
        self.assertEqual(p3.timestamp,"01:00:00")

    def testUserAuth(self):
        #get Users and UserAuthTokens
        a2 = User.objects.get(email="a2@gmail.com")
        a3 = User.objects.get(email="a3@gmail.com")
        u2 = UserAuthTokens.objects.get(user=a2)
        u3 = UserAuthTokens.objects.get(user=a3)

        #check values
        self.assertEqual(u2.email,"a2@gmail.com")
        self.assertEqual(u3.email,"a3@gmail.com")
        self.assertEqual(u2.token,"tmptoken1")
        self.assertEqual(u3.token,"tmptoken2")
        self.assertEqual(u2.timestamp,"12:00:00")
        self.assertEqual(u3.timestamp,"01:00:00")





        
        
        



