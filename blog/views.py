from django.shortcuts import render
from .models import Post
from django.db.models import Q
from datetime import datetime
from django.shortcuts import get_object_or_404

def post_list(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'blog/post_list.html', {'posts': posts,
    'now': datetime.now()                                       })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
