from django.conf.urls import urlfrom . import viewsurlpatterns = [    # url(r'^weather/beijing/2018/$', views.weather1),    # 演示利用正则组提取url路径参数 位置参数    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather1),    # 演示利用正则组起别名 提取url路径参数 关键字参数, 如果给正则组起了别名,那么对应的形参名必须和别名一致    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),    # 演示获取查询字符串    url(r'^get_query_params/$', views.get_query_params),    # 演示获取请求体表单数据    url(r'^get_form_data/$', views.get_form_data),    # 演示获取请求体非表单数据(json)    url(r'^get_json/$', views.get_json),    # 演示获取请求用户    url(r'^get_user/$', views.get_user),    # 演示响应对象基本使用    url(r'^response_demo/$', views.response_demo),    # 演示响应json数据使用    url(r'^json_response_demo_xxxxx/$', views.json_response_demo, name='index'),  # url函数的第三name参数表示给路由起别名    # 演示重定向    url(r'^redirect_demo/$', views.redirect_demo),    # 演示cookie的使用    url(r'^cookie_demo/$', views.cookie_demo),]