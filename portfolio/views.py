# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/20 3:45'
from django.shortcuts import render,get_object_or_404
from gallery.models import Gallery


def home(request):
     gallerys = Gallery.objects
     return render(request,'home.html',{'gallerys':gallerys})

def gallery_text(requst,gallery_id):
    gallerydetail = get_object_or_404(Gallery, pk=gallery_id)
    return  render(requst,'gallery_detail.html',{'gallerytext':gallerydetail})