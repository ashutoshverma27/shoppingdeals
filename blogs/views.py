from django.shortcuts import render
from .models import BlogPost

def blog(request):
    all=BlogPost.objects.get(postid=1)
    return render(request,'blogs/blog.html',{'all':all})
