from django.conf.urls import urlfrom . import viewsurlpatterns = [    # url(正则, 函数名, 路由别名)    url(r'^demoview/$', views.DemoView.as_view()),]