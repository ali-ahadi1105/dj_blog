from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Article, Category

class ArticleListView(ListView):
    queryset = Article.objects.published()
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page') or self.kwargs.get('page', 1)
        paginator = Paginator(self.queryset, self.paginate_by)
        context['articles'] = paginator.get_page(page)
        return context

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