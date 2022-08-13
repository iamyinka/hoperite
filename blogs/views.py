from django.shortcuts import render, get_object_or_404
from blogs.models import Post


def home(request):
    featured_post = Post.objects.first()
    posts = Post.objects.all()[:6]
    context = {
        'posts': posts,
        'featured_post': featured_post
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


def post_detail(request, slug):
    if slug != None:
        post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'blogs/post_detail.html', context)


def tagged_posts(request, tag):
    if tag != None:
        posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blogs/tagged_posts.html', context)
