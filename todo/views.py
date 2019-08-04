from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def home(request):
    content = {'content': Todo.objects.all()}
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            content_warning = {'content':Todo.objects.all(),'warning':'请输入内容!'}
            return render(request, 'todolisthome.html',content_warning)
        else:
            a_row = Todo(thing=request.POST['待办事项'],done =False)
            a_row.save()
            content_success = {'content':Todo.objects.all(),'success':'添加成功!'}
            return render(request,'todolisthome.html',content_success)
    else:

        return render(request, 'todolisthome.html', content)

def about(request):
    return render(request,'todolistabout.html')

def edit(request,key_id):
    a = Todo.objects.get(id = key_id)
    if request.method == 'POST':
        if request.POST['已修改事项'] == '':
            return render(request, 'todolisteditt.html', {'warning':'请输入内容!'})
        else:
            a.thing = request.POST['已修改事项']
            a.save()
            return redirect('待办事项主页')
    else:
        content = {'待修改事项': a.thing}
        return render(request,'todolisteditt.html',content)

def t_del(request,key_id):
    a = Todo.objects.get(id=key_id)
    a.delete()

    return redirect('待办事项主页')

def sus(request,key_id):
    a = Todo.objects.get(id = key_id)
    if a.done == False:
        a.done = True
        a.save()
        return redirect('待办事项主页')
    else:
        a.done = False
        a.save()
        return redirect('待办事项主页')