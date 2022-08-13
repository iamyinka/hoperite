from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('blog/tagged_posts/<str:tag>/',
         views.tagged_posts, name='tagged_posts'),
]
