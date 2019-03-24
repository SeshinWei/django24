from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class DemoView(View):
    """定义类视图"""

    def get(self, request):
        return HttpResponse('get请求业务逻辑')

    def post(self, request):
        return HttpResponse('post请求业务逻辑')
