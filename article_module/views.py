from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic import ListView, DetailView
from article_module.models import Article, ArticleCategory, ArticleComment
from jalali_date import datetime2jalali, date2jalali

class ArticlesLIstViews(ListView):
    model = Article
    paginate_by = 1
    template_name = 'article_module/article_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesLIstViews, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesLIstViews, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category') #digita ya mobile , ...

        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'
    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] =ArticleComment.objects.filter(article_id=article.id, parent=None).prefetch_related('articlecomment_set')
        return context


def article_categories_component(request: HttpRequest):
    article_main_category = ArticleCategory.objects.filter(is_active=True, parent_id=None)
    context = {
        'main_categories' : article_main_category
    }
    return render(request, 'article_module/components/article_categories_component.html', context)