# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/20 3:45'
from django.shortcuts import render
from gallery.models import Gallery


def home(request):
     gallerys = Gallery.objects
     return render(request,'home.html',{'gallerys':gallerys})