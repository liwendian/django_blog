"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from article.views import article_list
from taggit_templatetags2.views import TagCanvasListView
from taggit_templatetags2 import urls as taggit_templatetags2_urls
from article import views

# 存放URL映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),
    # 设置文章列表页作为网站主页
    path('', article_list, name='home'),
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
    path('article-list/', views.article_list, name='article_list'),
]
