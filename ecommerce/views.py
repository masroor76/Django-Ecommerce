from django.shortcuts import render
from django.views import View
from products.models import ProductsModel

# Create your views here.

class Home(View):
    def get(self, request, format=None):
        data = ProductsModel.objects.all()
        return render(request,'index.html' , {'data': data})
    
class Products(View):
    def get(self, request, format=None): 
        data = ProductsModel.objects.all()
        return render(request,'products.html', {'data': data} )

class About(View):
    def get(self, request, format=None):
        return render(request,'about.html')