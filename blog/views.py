from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category

# Create your views here.

def home(request, page=1):
    articles = Article.objects.published()
    paginator = Paginator(articles, 4)
    page_data = paginator.get_page(page)
    context = {
        "articles": page_data
    }
    return render(request, 'blog/home.html', context)

def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/detail.html', context)

def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 2)
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "articles": articles
    }
    return render(request, 'blog/category.html', context)