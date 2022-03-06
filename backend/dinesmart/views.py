from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from secrets import token_bytes
import hmac
import hashlib
import string
import time
import json
from django.views.decorators.csrf import csrf_exempt

from dinesmart.models import Users, UserAuthTokens, PasswordReset

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
    
    # save user in database
    user = Users(email=email, password=password)
    try:
        user.save()
        #create authentication token for session
        token = createAuthToken(email)

        request.session['email'] = email
        request.session['token'] = str(token)
        request.session.set_expiry(1800) #session expires in 1800 seconds = 0.5 hour
        return HttpResponse("user succesfully created", status=201)
    except:
        return HttpResponse("error saving user", status=401)

@csrf_exempt
def login(request):
    # only accept post requests
    if request.method != "POST":
        return HttpResponse("only POST calls accepted", status=404)

    # input validation
    try:
        payload = json.loads(request.body)
        email = payload['email']
        password = payload['password']
    except:
        return HttpResponse("missing/blank email or password", status=401)

    # make sure user exists
    try:
        user_count = Users.objects.filter(email=email).count()
        if user_count != 1:
            return HttpResponse("unable to find user", status=404)
    except Exception as e:
        return HttpResponse(e, status=404)

    #create authentication token for session
    token = createAuthToken(email)

    request.session['email'] = email
    request.session['token'] = str(token)
    request.session.set_expiry(1800) #session expires in 1800 seconds = 0.5 hour

    return HttpResponse("login successful", status=200)

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

        #compare_digest used to secure against timing attacks
        if hmac.compare_digest(token, str(hashedToken)):
            return True
        return False
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
    