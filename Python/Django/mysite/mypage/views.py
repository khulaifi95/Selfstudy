from django.shortcuts import render
from .models import Post
# Create your views here.


posts = [
    {
        'author': 'Kevin Xu',
        'title': 'Post 1',
        'content': 'Landing post.',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'Suzy Zhou',
        'title': 'Post 2',
        'content': 'Second post.',
        'date_posted': 'April 2, 2020'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mypage/home.html', context)


def about(request):
    return render(request, 'mypage/about.html', {'title': 'About'})
