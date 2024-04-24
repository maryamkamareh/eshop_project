from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic import ListView
from article_module.models import Article
from jalali_date import datetime2jalali, date2jalali

class ArticlesLIstViews(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/article_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesLIstViews, self).get_context_data(*args, **kwargs)
        context['date'] = datetime2jalali(self.request.user.date_joined)
        return context