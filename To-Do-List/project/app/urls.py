from django.urls import path
from .views import *

urlpatterns = [
  path("register/", registerview, name="register"),
  path("login/",loginview, name="login"),
  path("post/", postdata, name='post'),
  path("", get, name='home'),
  path("update/<int:id>/", updatedata, name='update'),
  path("delete/<int:id>", deleteview, name="delete"),
  path("logout/", logoutview, name="logout"),
]