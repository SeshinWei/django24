from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# /weather/beijing/2018
def weather1(request, city, year):
    """演示获取url路径数据"""
    print(city)
    print(year)

    return HttpResponse('weather1')


# /weather/beijing/2018
def weather2(request, year, city):
    """演示获取url路径数据"""
    print(city)
    print(year)

    return HttpResponse('weather1')


# GET /get_query_params/
def get_query_params(request):
    """演示获取url查询字符串数据"""
    # request.GET 后面大写的GET只是一个请求对象的属性而已,和请求方法无关 QueryDict类型对象
    query_dict = request.GET
    # query_dict.get()  取单个值
    # query_dict.getlist() 取某个的多个值,返回列表
    return HttpResponse('get_query_params')


# request.POST 用来获取请求体中的表单数据, 大写的POST只是一个属性而已,和请求方法无关, QueryDict类型对象
# POST /get_form_data/
def get_form_data(request):
    """演示获取请求体表单数据"""

    query_dict = request.POST
    print(query_dict.get('a'))
    print(query_dict.getlist('like'))

    return HttpResponse('get_form_data')

