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


from dinesmart.models import Users, UserAuthTokens, PasswordReset, Reviews

# Create your views here.

@csrf_exempt
def create_user(request):
    #only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        payload = json.loads(request.body)
        email = payload["email"]
        password = payload["password"]
    except:
        return HttpResponse("missing/blank email or password", status=401)

    if (email == "" or password == ""):
        return HttpResponse("missing/blank email or password", status=401)

    # make sure email isn't already taken
    try:
        user_count = Users.objects.filter(email=email).count() 
        if user_count != 0:
            return HttpResponse("email already in use", status=406)
    except Exception as e:
        return HttpResponse(e, status=401)

    hashed_password = hash_password(password)

    # save user in database
    user = Users(email=email, password=hashed_password)
    try:
        user.save()
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
        user_count = Users.objects.filter(email=email, password=hashed_password).count()
        if user_count != 1:
            return HttpResponse("unable to find user", status=404)
    except:
        return HttpResponse("unable to find user", status=404)

    #create authentication token for session
    token = createAuthToken(email)

    request.session['email'] = email
    request.session['token'] = str(token)
    request.session.set_expiry(1800) #session expires in 1800 seconds = 0.5 hour

    return HttpResponse("login successful", status=200)

def hash_password(password):
    key = 'b\'\\xd3\\xf4\\xb7X\\xbd\\x07"\\xf4a\\\'\\xf5\\x16\\xd7a\\xa4\\xbd\\xf0\\xe7\\x10\\xdeR\\x0el\\xc2fW\\x80\\xfd\\xd39\\x953\''
    passwordbytes = bytes(password, 'utf-8')
    keybytes = bytes(key, 'utf-8')

    h = hmac.new( keybytes, passwordbytes, hashlib.sha256 )
    hashed_password = str(h.hexdigest())
    return hashed_password

#this function is just used as a test to make sure the session authentication is working
@csrf_exempt
def auth_test(request):
    try:
        if checkAuthToken(request.session['email'], request.session['token']):
            return HttpResponse("authenticated", status=200)
    except:
        return HttpResponse("not authenticated", status=404)

    return HttpResponse("not authenticated", status=404)

#checks that the user's session is authenticated
def checkAuthToken(request):
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
    user = Users.objects.get(email=email)
    user.password = hashedPassword

    try:
        user.save()
        return HttpResponse("password succesfully updated", status=201)
    except:
        return HttpResponse("error saving user", status=401)


@csrf_exempt
def request_password_reset(request):
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
        user_count = Users.objects.filter(email=email).count()
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
	return ''.join(random.choice(chars) for _ in range(N))

@csrf_exempt
def browse_restaurants(request):

    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        payload = json.loads(request.body)
        city = payload["city"]
        date = payload["date"]
        seats = payload["seats"]
        cuisine = payload["cuisine"]
    except:
        return HttpResponse("missing/blank email or password", status=401)
    
    response = {
        "rest1": {"times": ["5:45", "6:45", "7:45"], "price": "$$", "distance": "20", "cuisine": "Mexican"},
        "rest2": {"times": ["5:50", "6:30"], "distance": "5", "cuisine": "Italian"},
        "rest3": {"times": ["6:55", "7:15", "7:30", "7:45", "8:00"]},
        "rest4": {"times": ["6:55", "7:15", "7:30", "7:45", "8:00"], "price": "$$$"},
    }
    return JsonResponse(response)

@csrf_exempt
def add_review(request):
    try:
        payload = json.loads(request.body)
        user = request.session["email"]
        restaurant = payload["restaurant"]
        rating = payload["rating"]
        content = payload["content"]
        review = Reviews(user=user, restaurant=restaurant, rating=int(rating), content=content)
        review.save()
        return HttpResponse("successfully added review", status=200)
    except:
        return HttpResponse("missing/blank email or password", status=401)

@csrf_exempt
def my_reviews(request):
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    #input validation
    try:
        email = request.session["email"]
        return JsonResponse(model_to_dict(Reviews.objects.get(user=email)))
    except Exception as e:
        return HttpResponse(e, status=401)
