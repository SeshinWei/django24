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