from django.shortcuts import render, HttpResponseRedirect

from login.models import *


# Create your views here.
def login(request):
    # print('path:', path_url)
    if request.method == 'POST':
        path_url = request.POST['path_url']
        name = request.POST['name']
        password = request.POST['password']
        try:
            stu = Students.objects.filter(name=name, password=password)
        except Exception as e:
            print(e)
        if stu:
            try:
                name = Students.objects.get(name=name, password=password)
            except Exception as e:
                print(e)
            name = request.session['name'] = {"name": name.name, "photo": str(name.photo)}
            if path_url is not None:
                sign_code = request.GET.get('sign_code', '')
                return HttpResponseRedirect(path_url + f'?sign_code={str(sign_code)}')
            return HttpResponseRedirect('/')
        else:
            msg = "账号或密码错误！！"
            return render(request, 'login/login.html', {"msg": msg})
    else:
        path_url = request.GET.get('path', '/')
        return render(request, 'login/login.html', {"path_url": path_url})


def reginter(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        photo = request.FILES.get('photo')
        try:
            stu = Students.objects.filter(is_active=True, name=name)
        except Exception as e:
            print(e)
        if stu:
            msg = '用户已存在！'
            return render(request, 'login/register.html', {"msg": msg})
        else:
            try:
                stu = Students.objects.create(
                    name=name,
                    password=password,
                    phone=phone,
                    email=email,
                    photo=photo
                )
            except Exception as e:
                print(e)
            msg = "注册成功！"
            return render(request, 'login/login.html', {"msg": msg})

    return render(request, 'login/register.html')


def pswd_update(request):
    if request.method == "POST":
        name = request.session['name']
        password_1 = request.POST["password_1"]
        password_2 = request.POST["password_1"]

        try:
            stu = Students.objects.get(name=name['name'])
        except Exception as e:
            print(e)
        if stu.password == password_1:
            stu.password = password_2
            stu.save()
            return HttpResponseRedirect("/login/")
        else:
            msg = "账号或密码错误！"
            return render(request, 'login/pswd_update.html', {"msg": msg})
    else:
        return render(request, 'login/pswd_update.html')


def logout(request):
    if 'name' in request.session:
        del request.session['name']

    return HttpResponseRedirect('/login/')


def index(request):
    try:
        text = Text.objects.filter(is_active=True).order_by('time')
    except Exception as e:
        print(e)
    return render(request, 'index/index.html', {"text": text})
