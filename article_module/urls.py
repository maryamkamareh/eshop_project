from django.urls import path
from article_module.views import ArticlesLIstViews

urlpatterns = [
    path('', ArticlesLIstViews.as_view(), name='articles_list'),
]
