from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

"""Django中的视图函数不需要指定请求方法,只要路由匹配成功都可以调用, 查询字符串无论是get请求还是post请求都可以有,但一般都是get请求带查询字符串"""


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


# POST /get_json/
def get_json(request):
    """演示获取请求体中的非表单数据:json"""
    # 获取请求体非表单数据用body属性,得到bytes类型的数据
    json_bytes = request.body
    json_str = json_bytes.decode()
    dict = json.loads(json_str)  # 将json字符串转换成json字典或json列表
    # json.dumps()  # 把字典或列表转换成json字符串
    print(dict)
    return HttpResponse('get_json')
