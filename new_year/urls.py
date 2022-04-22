from django.urls import path
from . import views
urlpatterns = [
    path("new_year",views.index, name="index")
]
