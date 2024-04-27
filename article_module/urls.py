from django.urls import path
from . import views
from article_module.views import ArticlesLIstViews, ArticleDetailView

urlpatterns = [
    path('', ArticlesLIstViews.as_view(), name='articles_list'),
    path('cat/<str:category>', ArticlesLIstViews.as_view(), name='articles_by_category_list'),
    path('<pk>', ArticleDetailView.as_view(), name='articles_detail'),
    # path('add-article-comment', views.add_article_comment, name='add-article-comment')
]
