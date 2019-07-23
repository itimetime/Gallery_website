
from django.urls import path
from .import views


urlpatterns = [
    path('sign',views.signup,name='注册页面'),
    path('login',views.login,name='登录'),
    path('logout',views.logout,name='登出'),
    path('signsuccess',views.signsuccess,name='注册成功')

]
