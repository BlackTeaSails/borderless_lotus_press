from django.shortcuts import render
from devblog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('published_date')[:6]
    return render(request, 'main/index.html', {'posts':posts})
