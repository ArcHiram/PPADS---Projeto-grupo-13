from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form, list, bio, create

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('list/', list, name='list'),
    path('bio/', bio, name='bio'),
    path('create/', create, name='create'),
    path('save-form/', save_form, name='save_form'),
]