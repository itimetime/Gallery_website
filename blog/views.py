from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_page(requst):
    blogs = Blog.objects
    return  render(requst,'blog.html',{'blog':blogs})