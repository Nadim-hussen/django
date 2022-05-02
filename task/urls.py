from django.urls import path
from . import views

urlpatterns=[
    path("task",views.index, name="index"),
    # path("<str:name>",views.greeting, name="greeting"),
]