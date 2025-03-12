from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

# Create your views here.

class Home(View):
    def get(self, request, format=None):
        list = {'name':'Masroor Anir','age':25}
        return render(request,'index.html',list)
    
class Products(View):
    def get(self, request, format=None): 
        return render(request,'products.html')

class About(View):
    def get(self, request, format=None):
        return render(request,'about.html')