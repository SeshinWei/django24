from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
路由定义三种写法:
1. 总 + 子
2. 总
3. 总 + 子
"""

# GET http://127.0.0.1:8000/users/index/?a=10&b=20
def index(request):
    """
    视图函数, 只少要有一个参数
    :param request: 接收请求对象 类型HttpRequest
    :return: 响应对象  HttpResponse
    """
    return HttpResponse('hello world')


