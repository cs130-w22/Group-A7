from calendar import c
from re import A
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from secrets import token_bytes
import hmac
import hashlib
import string
import time
import json
import random
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict
from datetime import date

from scraper.main import Scraper


from dinesmart.models import User, UserAuthTokens, PasswordReset, Review, Restaurant, UserProfile, to_dict

# Create your views here.

@csrf_exempt
def create_user(request):
    """Method to create a user instance with an email and a password
    Recieves: request, a payload with user information
    Returns: an http respoinse to display describing the success or failure to create a user

    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        payload = json.loads(request.body)
        email = payload["email"]
        password = payload["password"]
        name = payload["name"]
        location = payload["location"]
    except:
        return HttpResponse("missing/blank email or password", status=401)

    if (email == "" or password == ""):
        return HttpResponse("missing/blank email or password", status=401)

    # make sure email isn't already taken
    try:
        user_count = User.objects.filter(email=email).count() 
        if user_count != 0:
            return HttpResponse("email already in use", status=406)
    except Exception as e:
        return HttpResponse(e, status=401)

    hashed_password = hash_password(password)

    # save user in database
    user = User(email=email, password=hashed_password)
    profile = UserProfile(user=user, name=name, location=location)
    try:
        user.save()
        profile.save()
        #create authentication token for session
        token = createAuthToken(email)

        request.session['email'] = email
        request.session['token'] = str(token)
        request.session.set_expiry(3600) #session expires in 3600 seconds = 1 hour
        return HttpResponse("user succesfully created", status=201)
    except:
        return HttpResponse("error saving user", status=401)

@csrf_exempt
def login(request):
    """Method to login a user by validating or invalidating their given info
    Recieves: request, a payload with theoretically correct login info
    Returns: an http respoinse to display describing the success or failure to login a particular user

    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        payload = json.loads(request.body)
        email = payload['email']
        password = payload['password']
    except:
        return HttpResponse("missing/blank email or password", status=401)

    #hash password
    hashed_password = hash_password(password)

    #make sure user exists
    try:
        user = User.objects.get(email=email, password=hashed_password)
    except:
        return HttpResponse("unable to find user", status=404)

    #create authentication token for session
    token = createAuthToken(email)

    request.session['email'] = email
    request.session['token'] = str(token)
    request.session.set_expiry(1800) #session expires in 1800 seconds = 0.5 hour

    return HttpResponse("login successful", status=200)

def hash_password(password):
    """Method to hash a given password for encryption purposes
    Recieves: password, a password to hash
    Returns: hash_password a password that has been hashed

    """
    key = 'b\'\\xd3\\xf4\\xb7X\\xbd\\x07"\\xf4a\\\'\\xf5\\x16\\xd7a\\xa4\\xbd\\xf0\\xe7\\x10\\xdeR\\x0el\\xc2fW\\x80\\xfd\\xd39\\x953\''
    passwordbytes = bytes(password, 'utf-8')
    keybytes = bytes(key, 'utf-8')

    h = hmac.new( keybytes, passwordbytes, hashlib.sha256 )
    hashed_password = str(h.hexdigest())
    return hashed_password

#this function is just used as a test to make sure the session authentication is working
@csrf_exempt
def auth_test(request):
    """Method to test session authentication
    Recieves: request, the request paylod
    Returns: http response to validate or invalidate authorization
    """
    try:
        if checkAuthToken(request.session['email'], request.session['token']):
            return HttpResponse("authenticated", status=200)
    except:
        return HttpResponse("not authenticated", status=404)

    return HttpResponse("not authenticated", status=404)

#checks that the user's session is authenticated
def checkAuthToken(request):
    """Method to validate a users session
    Recieves: request, the info to check against an authtoken
    Returns: boolean representing a validated or invalidated authentication request
    """
    try:
        email = request.session['email'] 
        token = request.session['token']
        #get the most recent token entry in the database for the user
        userAndToken = UserAuthTokens.objects.filter(email=email).order_by('-timestamp')[0]
        
        tokenbytes = bytes(userAndToken.token, 'utf-8')

        #uses the same key as the createAuthToken method
        key = 'b\'\\xd3\\xf4\\xb7X\\xbd\\x07"\\xf4a\\\'\\xf5\\x16\\xd7a\\xa4\\xbd\\xf0\\xe7\\x10\\xdeR\\x0el\\xc2fW\\x80\\xfd\\xd39\\x953\''
        keybytes = bytes(key, 'utf-8')
        h = hmac.new( keybytes, tokenbytes, hashlib.sha256 )
        hashedToken = h.hexdigest()

        # compare_digest used to secure against timing attacks
        return True if hmac.compare_digest(token, str(hashedToken)) else False
    except Exception:
        return False

#creates the authentication token for sessions
def createAuthToken(email):
    """Method to create the authentication token for an email
    Recieves: email, the email for which to create the authentication token
    Returns: hashedToken, the token corresponding to the given email but hashed for encryption
    """
    #create secure 32 byte token
    token = str(token_bytes(32))
    userAndToken = UserAuthTokens(email=email, token=token, timestamp=time.time())
    
    #save token in database for comparison
    userAndToken.save()

    #key generated using secrets.token_bytes(32)
    #32 byte key for encryption
    key = 'b\'\\xd3\\xf4\\xb7X\\xbd\\x07"\\xf4a\\\'\\xf5\\x16\\xd7a\\xa4\\xbd\\xf0\\xe7\\x10\\xdeR\\x0el\\xc2fW\\x80\\xfd\\xd39\\x953\''
    tokenbytes = bytes(token, 'utf-8')
    keybytes = bytes(key, 'utf-8')

    h = hmac.new( keybytes, tokenbytes, hashlib.sha256 )
    hashedToken = h.hexdigest()

    return hashedToken

@csrf_exempt
def logout(request):
    """Method to logout a particular user
    Recieves: request, the payload describing user intent to logout
    Returns: http response showing the success or failure of a user to logout
    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    
    #only accept requests from users with a logged in, authenticated session
    if not checkAuthToken(request):
        return HttpResponse("user not authorized", status=401)

    try:
        del request.session['email']
        del request.session['token']
        return HttpResponse("success", status=200)
    except:
        return HttpResponse("error", status=404)

@csrf_exempt
def get_current_user(request):
    """Method to get the user that is currently logged in
    Recieves: request, the payload to validate whether a particular user is logged in
    Returns: httprespone validating or invalidating the logged in state of a user
    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    
    #only accept requests from users with a logged in, authenticated session
    if not checkAuthToken(request):
        return HttpResponse("user not authorized", status=401)

    try:
        email = request.session['email']
        return HttpResponse(email, status=200)
    except:
        return HttpResponse("unable to get current user", status=404)

@csrf_exempt
def reset_password(request):
    """Method to reset the password for a user
    Recieves: request, payload containing reset information
    Returns: httpresponse describing reset success
    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    
    #input validation
    try:
        payload = json.loads(request.body)
        email = payload['email']
        password = payload['password']
        token = payload['token']
    except:
        return HttpResponse("missing/blank email or token", status=401)

    #get the token from the database
    try:
        userAndToken = PasswordReset.objects.filter(email=email).filter(resetToken=token)[0]
    except:
        return HttpResponse("invalid token", status=401)
    
    #if token does not equal our database's token, reject
    if userAndToken.resetToken != token:
        return HttpResponse("invalid token", status=401)
    
    #check if token is expired or not
    if float(userAndToken.timestamp) < time.time():
        return HttpResponse("token expired", status=401)

    #delete token after it is used
    userAndToken.delete()


    #hash password
    key = 'b\'\\xd3\\xf4\\xb7X\\xbd\\x07"\\xf4a\\\'\\xf5\\x16\\xd7a\\xa4\\xbd\\xf0\\xe7\\x10\\xdeR\\x0el\\xc2fW\\x80\\xfd\\xd39\\x953\''
    passwordbytes = bytes(password, 'utf-8')
    keybytes = bytes(key, 'utf-8')

    h = hmac.new( keybytes, passwordbytes, hashlib.sha256 )
    hashedPassword = str(h.hexdigest())
    
    #save user in database
    user = User.objects.get(email=email)
    user.password = hashedPassword

    try:
        user.save()
        return HttpResponse("password succesfully updated", status=201)
    except:
        return HttpResponse("error saving user", status=401)


@csrf_exempt
def request_password_reset(request):
    """Method to request the reset of a password
    Recieves: request, payload for which to create a reset password request
    Returns: http response decribing success or failure of reste request
    """
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    
    try:
        payload = json.loads(request.body)
        email = payload['email']
    except:
        return HttpResponse("missing/blank email", status=401)

    #make sure user exists
    try:
        user_count = User.objects.filter(email=email).count()
        if user_count != 1:
            return HttpResponse("unable to find user CHANGE THIS", status=200)
    except:
        return HttpResponse("unable to find user CHANGE THIS", status=200)

    #create secure token that is 20 chars long
    token = randStr(N=20)
    #this token will only be valid for 10 minutes
    passwordResetToken = PasswordReset(email=email, resetToken=token, timestamp=time.time() + 600)
    
    #save token in database for comparison
    passwordResetToken.save()
    
    sendResetEmail(email, token)
    return HttpResponse("email sent, token: " + token, status=200)


#sends a reset email given a token and an email
def sendResetEmail(email, token):
    """Method to send the email to reset password
    Recieves: email, email to send ti; token, authorization token for password reset
    Returns: nothing
    """
    import smtplib, ssl

    port = 465  # For SSL

    smtp_server = "smtp.gmail.com"
    sender_email = "dinesmart@gmail.com" 
    password = "Dinesmart1$"

    receiver_email = email 

    #will have to change this upon deployment
    link = "localhost:8000/passwordResetPage?token=" + token
  
    subject = "DineSmart Password Reset"
    text = "Hello, \n\nIf you are recieving this email, a password reset request has been sent for your account at DineSmart. Follow the link to reset your password.\n\n{link}\n\nBest,\DineSmart  "
    text = text.format(link=link)
    message = 'Subject: {}\n\n{}'.format(subject, text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

# returns a randomly generated token of length N
def randStr(chars = string.ascii_uppercase + string.ascii_lowercase + string.digits, N=10):
    """Method to randomly generate a token
    Recieves: chars, characters on can use; N length of string
    Returns: nothing
    """
    return ''.join(random.choice(chars) for _ in range(N))

@csrf_exempt
def browse_restaurants(request):
    """Method to send the email to reset password
    Recieves: email, email to send ti; token, authorization token for password reset
    Returns: nothing
    """
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        payload = json.loads(request.body)
        city = payload["city"]
        date = payload["date"]
        seats = int(payload["seats"])
        cuisine = payload.get("cuisine", None)
        time = payload.get("time", None)

        scraper = Scraper()
        scraper.scrape_restaurant_info(city, date, seats, time)

        times = scraper.get_restaurant_times()
        tags = scraper.get_restaurant_tags()
        links = scraper.get_restaurant_hyperlinks()

        data = {key: {"times": times[key], "tag": tags[key], "link": links[key]} for key in times}

        return JsonResponse(data, safe=False)
    except Exception as e:
        return HttpResponse(e, status=401)

@csrf_exempt
def add_review(request):
    """Method to add a review
    Recieves: request, the request with payload to add
    Returns: httpresponse showing success or error
    """
    try:
        payload = json.loads(request.body)
        user = User.objects.get(email=request.session['email'])
        restaurant, created = Restaurant.objects.get_or_create(name=payload["restaurant"])
        rating = payload["rating"]
        content = payload["content"]
        review = Review(user=user, restaurant=restaurant, rating=int(rating), content=content)
        review.save()
        return HttpResponse("successfully added review", status=200)
    except Exception as e:
        return HttpResponse(e.stracktrace(), status=401)

@csrf_exempt
def my_reviews(request):
    """Method to see a user's reviews
    Recieves: request, the request to get your reviews
    Returns: httpresponse showing reviews
    """
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    user = User.objects.get(email=request.session['email'])
    try:
        data = list(Review.objects.filter(user=user).values())  
        return JsonResponse(data, safe=False)    
    except Exception as e:
        return HttpResponse(e, status=401)
    
@csrf_exempt
def get_restaurant_by_id(request):
    """Method to get a restaurant given an id
    Recieves: request, relevant id
    Returns: httpresponse showing restaurant
    """
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)
    try:
        payload = json.loads(request.body)
        id = payload["id"]        
        return JsonResponse(to_dict(Restaurant.objects.get(id=id)))  
    except Exception as e:
        return HttpResponse(e, status=401)   

@csrf_exempt
def get_user_profile(request):
    """Method to get a user
    Recieves: request, relevant email
    Returns: httpresponse showing user
    """
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        user = User.objects.get(email=request.session["email"])
        return JsonResponse(to_dict(UserProfile.objects.get(user=user)))
    except Exception as e:
        return HttpResponse(e, status=401)

@csrf_exempt
def get_reviews_by_restaurant(request):
    """Method to get a reviews for a certain restaurant
    Recieves: request, relevant restaurant
    Returns: httpresponse showing reviews
    """
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    try:
        payload = json.loads(request.body)
        restaurant = payload["restaurant"]
    except Exception as e:
        return HttpResponse(e, status=401)

    #input validation
    try:
        data = list(Review.objects.filter(restaurant=Restaurant.objects.get(name=restaurant)).values())  
        return JsonResponse(data, safe=False)    
    except Exception as e:
        return HttpResponse(e, status=401)
