# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = Category
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')

# def index(request):
#     context = {
#         'news': News.objects.all(),
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)
#
#
# def get_category(request, category_id):
#     context = {
#         'news': News.objects.filter(category_id=category_id),
#         'title': 'Список новостей',
#         'category': Category.objects.get(pk=category_id),
#     }
#     return render(request, 'news/category.html', context=context)


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             return redirect(form.save())
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
