from django.shortcuts import render,redirect
from django.contrib.auth.models import User #获取用户数据
from django.contrib import auth  #判断用户信息
# Create your views here.


def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        user_name = request.POST.get('用户名')
        password1 = request.POST.get('密码')
        password2 = request.POST.get('确认密码')
        # user_name = request.POST['用户名']
        # password1 = request.POST['密码']
        # password2 = request.POST['确认密码']
        try:
            User.objects.get(username = user_name)
            return render(request,'signup.html',{'用户名错误':'该邮箱已存在'})
        except User.DoesNotExist:
            if password1 == password2:
                if len(password1) < 6:
                    return render(request, 'signup.html', {'密码过短': '请至少设置六位数密码'})
                else:
                    User.objects.create_user(username=user_name,password=password1)
                    return redirect('注册成功')
            else:
                return render(request, 'signup.html', {'密码不一致': '两次密码输入不一致'})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST.get('用户名')
        # user_name = request.POST['用户名']
        password1 = request.POST.get('密码')
        user = auth.authenticate(username=user_name,password=password1)
        if user is None:
            return render(request,'login.html',{'错误':'用户名或者密码错误'})
        else:
            auth.login(request,user)
            return redirect('产品首页')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect( '产品首页')

def signsuccess(request):
    return render(request,'signsuccess.html')