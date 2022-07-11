from django.urls import path
from . import views

urlpatterns=[
    path("task",views.index, name="index"),
    path("insert_Product",views.insert),
    # path("<str:name>",views.greeting, name="greeting"),
]