from django.urls import path
from . import views

urlpatterns = [
        path('index/',views.index,name='index'),
        path('articles/',views.ArticleListView.as_view(),name='article-list'),
        path('articles/<int:pk>',views.ArticleDetailView.as_view(),name='article-detail')
        ]
