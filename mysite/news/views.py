from django.shortcuts import render, get_object_or_404

from .models import News, Category


# Create your views here.
def index(request):
    context = {
        'news': News.objects.all(),
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    context = {
        'news': News.objects.filter(category_id=category_id),
        'title': 'Список новостей',
        'category': Category.objects.get(pk=category_id),
    }
    return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})
