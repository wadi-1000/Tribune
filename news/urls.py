from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.news_of_day, name = 'newsToday'),
    path('archives/<str:past_date>/',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name = 'search_results'),
    path('article/<int:article_id>/',views.article,name = 'article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    