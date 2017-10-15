from django.conf.urls import url
from django.contrib import admin

from posts.api.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    PostCreateAPIView,
	)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDestroyAPIView.as_view()),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
