from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def blog_page(requst):
    blogs = Blog.objects
    return  render(requst,'blog.html',{'blog':blogs})

def blog_text(requst,blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return  render(requst,'text_detail.html',{'blogtext':blogdetail})
