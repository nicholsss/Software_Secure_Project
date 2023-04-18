from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Blog


def loginView(request):
    form = AuthenticationForm()
    print('hello')
    return render(request, 'pages/login.html', {'form': form})

def addBlogPost(request):
    return render(request, 'pages/addBlog.html')

def deleteBlogPost(request, id):
    return render(request, 'pages/deleteBlog.html')

def editBlogPost(request, id):
    return render(request, 'pages/editBlog.html')

def homePageView(request):
    if request.user.is_authenticated:
        user = request.user
        blogs = Blog.objects.filter(user=user)
        return render(request, 'pages/index.html', {'blogs': blogs})
    else:
        return render(request, 'pages/index.html')


# Create your views here.
