# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/22 9:38'

from strings import views
from django.urls import path


urlpatterns = [

    path('count',views.count,name='计数'),
    path('about',views.about,name='关于'),
    path('start',views.home,name='开始')
    ]
