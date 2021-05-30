from django.db import models
from django.db.models.fields import TextField
from django.shortcuts import render
from .models import Post, Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


 

def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]
    list_posts = Post.objects.filter(deleted=False)

    data = {
        'lista_tecnologias': lista, 
        'posts': list_posts }

    return render(request, 'index.html', data)

@login_required
def post_detail(request, id):
    post = Post.objects.get(id=id) 
    return render(request, 'post_detail.html', {'post': post})


@login_required
def create(request):
    Post.objects.create(
        title=request.POST['title'],
        sub_title=request.POST['sub_title'],
        content = request.POST['content'],
        nota=request.POST['nota']        
    )
    return render(request, 'post_success.html',)


def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name=name, 
        email=request.POST['email'],
        message=request.POST['message']    
    )
    return render(request, 'contact_success.html', {'name_contact': name})

@login_required
def list(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]
    list_posts = Post.objects.filter(deleted=False)

    data = {
        'lista_tecnologias': lista, 
        'posts': list_posts }

    return render(request, 'post_list.html', data)

@login_required
def bio(request):
    return render(request, 'bio.html')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
        
def logout_view(request):
    logout(request)
    # Redirect to a success page.