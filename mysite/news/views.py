from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


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
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            return redirect(form.save())
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
