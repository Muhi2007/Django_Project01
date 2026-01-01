from django.shortcuts import render
from .models import Post

posts = Post.objects.all()

def home(request):
    context = {
        'title': "Dummy",
        'posts': posts}

    return render(request, "blog/home.html", context)