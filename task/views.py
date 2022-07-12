from django.contrib import messages
from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item,upload_post
# Create your views here.

# tasks = ['foo','woe','bar','baz','all','is','well']
def index(request):
    products = upload_post.objects.all()
    context = {
        'product':products
    }
    return render(request, "task.html",context)

def insert(request):
    if request.method == "POST":
        prod = upload_post()
        prod.name = request.POST.get('name')
        prod.price = request.POST.get('price')
        prod.description = request.POST.get('description')

        if len(request.FILES) !=0:
            prod.image = request.FILES['image']
        prod.save()
        messages.success(request, "product added successfully")
        return redirect('/task/task')

    return render(request,'insertProduct.html')