from . import views
from django.urls import path

urlpatterns=[
    path('',views.homepage,name='homepage'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    # url(r'^article/(\d+)',views.article,name ='article'),
    # url(r'^newsletter',views.news_letter,name ='newsletter'),
    # url(r'^new/article$', views.new_article, name='new-article'),
]
