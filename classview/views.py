from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

# Create your views here.

"""
类视图必须继承View 
类视图中的方法名都必须是请求方法名小写
"""

def my_decorator(view_func):
    """定义装饰器"""
    def wrapper(request, *args, **kwargs):
        print('装饰器被调用了')
        return view_func(request, *args, **kwargs)

    return wrapper

# @my_decorator
# def index(request):
#     return HttpResponse('ok')


@method_decorator(my_decorator, name='get')
class DemoView(View):
    """定义类视图"""

    # @my_decorator
    def get(self, request):
        return HttpResponse('get请求业务逻辑')

    def post(self, request):
        return HttpResponse('post请求业务逻辑')
# 映射机制 动态查找
# hasattr()  判断类中是否有某个成员(属性和方法) bool
# getattr()  获取类中的属性或方法
# __import__()  # 动态导包

