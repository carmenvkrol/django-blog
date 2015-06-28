from django.shortcuts import render, get_object_or_404
from cvk_blog.models import Post

def index(request):
  posts = Post.objects.filter(published=True)
  return render(request, 'cvk_blog/index.html', {'posts': posts})

def post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, 'cvk_blog/post.html', {'post': post})