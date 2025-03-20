from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View


class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request,'dashboard.html') 


class Registration(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1'] 
        user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password)
        user.save()     
        return redirect('/')
    


# @user_passes_test(not_logged_in)
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print(user)
            return redirect('/dashboard' , user= user )
        else:
            print("None User")
            return redirect('/')
        


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'login.html')
