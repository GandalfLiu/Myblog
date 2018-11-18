
from django.conf.urls import url

from app import views

urlpatterns = [
    # url(r'^hello/$',views.hello),
    url(r'^index/$',views.index),  # 首页
]