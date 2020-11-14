import json

from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from myapp.models import Book, User
from django.db.models import F, Q


def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def get_book(request):
    response = {}
    try:
        books = Book.objects.filter(book_name=request.GET.get('book_name'))
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def add_user(request):
    response = {}
    try:
        # name = request.GET.get('name')
        # result = User.objects.get(name=name)
        user = User(name=request.GET.get('name'),
                    password=request.GET.get('password'),
                    email=request.GET.get('email'))

        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def show_users(request):
    response = {}
    try:
        users = User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 用户登录 GET版
@require_http_methods(["GET"])
def login(request):
    response = {}
    try:
        name = request.GET.get('name')
        result = User.objects.get(name=name)
    except Exception as e:
        response['msg'] = '用户名不存在; User name does not exist'
        response['success'] = False

        return JsonResponse(response)

    try:
        password = request.GET.get('password')
        result = User.objects.get(name=name, password=password)
        response['msg'] = '用户{0}登录成功; User {0} logged in successfully'.format(name)
        response['success'] = True
    except Exception as e:
        response['msg'] = '密码错误; Incorrect password'  # str(e)
        response['success'] = False
    # return render(request, 'HomePage/index.html')
    return JsonResponse(response)


# 用户登录 POST版
@require_http_methods(["POST"])
def signin(request):
    response = {}

    name = request.POST.get('name', 0)
    password = request.POST.get('password', 0)
    # 检查输入是否为空
    if name and password:
        try:
            result = User.objects.get(name=name)
        except Exception as e:
            response['msg'] = '用户名不存在; User name does not exist'
            response['success'] = False

            return JsonResponse(response)

        try:
            result = User.objects.get(name=name, password=password)
            response['msg'] = '用户{0}登录成功; User {0} logged in successfully'.format(name)
            response['success'] = True
        except Exception as e:
            response['msg'] = '密码错误; Incorrect password' # str(e)
            response['success'] = False
        # return render(request, 'HomePage/index.html')
        return JsonResponse(response)

    else:
        response['msg'] = '输入不可为空; The input cannot be null'
        response['success'] = False

        return JsonResponse(response)


# 用户注册
@require_http_methods(["POST"])
def signup(request):
    global password, name, email
    response = {}

    name = request.POST.get('name', 0)
    password = request.POST.get('password', 0)
    email = request.POST.get('email', 0)

    print(name)
    print(password)
    print(email)

    # 判断参数中是否含有name,password,email
    if name and password and email:
        # 查找是否已存在该用户名
        try:
            result = User.objects.get(name=name)
            response['msg'] = '用户名已存在; User name already exists'
            response['success'] = False
        except:
            # 注册用户
            try:
                user = User.objects.create(name=name, password=password, email=email)
                user.save()
                response['msg'] = '用户{0}注册成功'.format(name)
                response['success'] = True

                # return HttpResponseRedirect("HomePage/index.html")
                return JsonResponse(response)
            except Exception as e:
                response['msg'] = str(e)
                print(str(e))
                response['success'] = False
        return JsonResponse(response)
    else:
        response['msg'] = '输入不可为空'
        response['success'] = False
        return JsonResponse(response)