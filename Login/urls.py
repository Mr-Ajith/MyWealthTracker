from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginView,name='loginView'),
    path('register/',views.registerView, name='registerView'),  
    path('resetpassword/',views.resetPasswordView, name='resetPasswordView'),
    path('logout',views.userLogout, name='userLogout'),
    path('login',views.userLogin, name='userLogin'),
    path('userregistration',views.userRegistration, name='userregistration'),
    
]
