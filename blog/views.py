from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    template = 'blog/template/blog/home.html'

    context = {
            'posts': posts
    }

    return  render(request, template, context)

def about(request):
    template = 'blog/template/blog/about.html'

    context = {
        'title': 'About'
    }

    return  render(request, template, context)
