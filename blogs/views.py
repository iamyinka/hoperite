from django.shortcuts import render

from blogs.models import Post


def home(request):
    posts = Post.objects.all()[:6]
    context = {
        'posts': posts
    }
    return render(request, 'blogs/index.html', context)


def contact(request):
    return render(request, 'blogs/contact.html')


def blogs(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blogs/blogs.html', context)
