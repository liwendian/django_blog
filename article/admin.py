from django.contrib import admin
# 导入ArticlerPost
from .models import ArticlePost
#导入文章栏目表
from .models import ArticleColumn

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
# 注册文章栏目到django自带的admin管理后台
admin.site.register(ArticleColumn)
