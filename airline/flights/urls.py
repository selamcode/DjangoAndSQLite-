from django.urls import path
from . import views

urlpatterns = [
    # name is used to refer to the path in the view
    path("", views.index, name="index"),

]
