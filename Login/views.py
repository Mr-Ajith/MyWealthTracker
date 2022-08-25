from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from MainDashboard.views import MainDashboardView
# Create your views here.

def loginView(request):
    if request.user.is_authenticated:
        return redirect(MainDashboardView)
    else:
        return render(request, 'LoginAppTemplates/login.html')

def registerView(request):
    return render(request, 'LoginAppTemplates/register.html')


def resetPasswordView(request):
   return render(request, 'LoginAppTemplates/forgot-password.html')


def userLogin(request):
    #Username is Email
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    return redirect(MainDashboardView)
  else:
    return redirect(loginView)

def userLogout(request):
  logout(request)
  return redirect(loginView)


def userRegistration(request):
  firstName = request.POST['firstName']
  lastName = request.POST['lastName']
  email = request.POST['email']
  password = request.POST['password']
  repeatPassword = request.POST['repeatPassword']
  if (password == repeatPassword):
    user = User.objects.create_user(email, email, password)
    user.first_name = firstName
    user.last_name = lastName
    user.save()
    return redirect(loginView)
  else:
    return redirect(registerView)

