from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("blog/<uuid:id>/", blog_detail, name="blog_detail"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]