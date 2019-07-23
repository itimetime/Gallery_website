# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/7/22 9:38'

from ph import views
from django.urls import path


urlpatterns = [

    path('',views.product_list,name='产品首页'),
    path('publish/', views.publish, name='发布页面'),
    path('success/', views.success, name='发布成功'),

    ]
