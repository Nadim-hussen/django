from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = ['foo','woe','bar','baz','all','is','well']
def index(request):
    return render(request, "task.html",{
        'tasks':tasks
    })
