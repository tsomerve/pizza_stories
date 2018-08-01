from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post

def all(request):
    posts = get_list_or_404(Post)
    context = {
        'posts': posts
    }
    return render(request, 'blog/all.html', context)
    
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
       'post': post
    }
    return render(request, 'blog/detail.html', context)
# Create your views here.
