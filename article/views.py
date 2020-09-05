from django.shortcuts import render

# 导入 HttpResponse 模块
from django.http import HttpResponse

# 导入数据模型ArticlePost
from .models import ArticlePost

# 引入markdown模块
import markdown

# 引入分页模块
from django.core.paginator import Paginator

# 引入 Q 对象[查询对象]
from django.db.models import Q

# 视图函数
def article_list(request):
    # 从 url 中提取查询参数
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')#栏目
    tag = request.GET.get('tag')

    # 初始化查询集
    article_list = ArticlePost.objects.all()

    # 用户搜索逻辑
    #  1.搜索查询集
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''
    #  2.栏目查询集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)
    #  3.标签查询集
    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])
    #  4.查询集排序
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 7)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 需要传递给模板（templates）的数据对象
    context = {
        'articles': articles,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
    }

    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 将markdown语法渲染成html样式
    md = markdown.Markdown(
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)
        
    # 需要传递给模板的对象
    context = { 'article': article, 'toc': md.toc }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)
