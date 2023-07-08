from django.urls import path
from . import views

 # name is used to refer to the path in the view for example for in views.py the index has a path called "flights/index.html"
urlpatterns = [
   
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int> :flight_id/book", views.book, name="book")
]
