from django.conf.urls import urlfrom rest_framework.routers import DefaultRouterfrom booktest import djang_viewsfrom . import viewsurlpatterns = [    # 列表视图的路由    # url(r'^books/$', views.BookListView.as_view()),    # # 详情视图的路由    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),    # 列表视图的API路由    url(r'^books/$', views.BookListGenericAPIView.as_view()),    # 详情视图的API路由    url(r'^books/(?P<pk>\d+)/$', views.BookDetailGenericAPIView.as_view()),]# router = DefaultRouter()  # 创建路由器# # router.register(r'books', views.BookInfoViewSet)  # 注册路由# urlpatterns += router.urls  # 把生成好的路由拼接到urlpatterns