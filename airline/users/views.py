from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    # if the user is not authenticated, then redirect them to the login page(view).
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    
def login_view(request):
        
        if request.method == "POST":
            # get the username and password from the form
            username = request.POST["username"]  # use selam for testing purposes
            password = request.POST["password"]  # use pass@1234 for testing purposes

            # authenticate the user
            user = authenticate(request, username=username, password=password)

            # if the user is authenticated, log them in and redirect them to the index page.
            if user is not None:
                # log the user in
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            
            # if the user is not authenticated, then return an error message.
            else:
                return render(request, "users/login.html", {
                    "message": "Invalid credentials."
                })
        return render(request, "users/login.html")

def logout_view(request):
    
    # log the user out
    logout(request)

    # redirect the user to the login page.
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
    
