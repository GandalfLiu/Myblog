from django.conf.urls import url

from app import views

urlpatterns = [
    # url(r'^hello/$',views.hello),
    url(r'^$',views.index, name='index'), # 首页
    url(r'^index/$', views.index, name='index'),  # 首页
    url(r'^callme/$', views.callme, name='callme'),  # 联系我
    url(r'^write/$', views.write, name='write'),  # 写文章
    url(r'^login/$', views.login, name='login'),  # 登录
    url(r'^logout/$', views.logout, name='lgout'),  # 退出
    url(r'^rigister/$', views.register, name='register'),  # 注册
]
