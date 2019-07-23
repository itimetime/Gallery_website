from django.shortcuts import render,redirect
from  django.contrib.auth.decorators import login_required  #装饰器，登录才能访问
from.models import Product
from django.utils import timezone
# Create your views here.


def product_list(request):
    pro = Product.objects
    return render(request, 'products.html', {'products': pro})

@login_required
def publish(request):
    if request.method == 'GET':
         return render(request,'publish.html')
    elif request.method == 'POST':
         title = request.POST['标题']
         intro = request.POST['APP介绍']
         url = request.POST['APP链接']
         try:
             icon = request.FILES['APP图标']
             image = request.FILES['大图']
             product = Product()
             product.title = title
             product.intro = intro
             product.url = url
             product.icon = icon
             product.image = image

             product.pub_date = timezone.datetime.now()
             product.hunter = request.user  # request 中包含了一个用户
             product.save()
             return redirect('发布成功')
         except Exception as err:
             return render(request,'publish.html',{'err':'上传错误,请上传图片'})

def success(request):
    return render(request,'successful.html')
