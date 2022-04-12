from django.urls import path

from . import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.intro, name='intro'),
    path('form/article/', views.get_article, name='get_article'),
    path('match/', views.match, name='match'),
    path('match/<int:match_id>/live_info/',views.info,name='info'),
    # we cant put only intro here..we have to put intro/ 
    # path('intro/', views.intro, name='intro'),
    path('match/<int:match_id>', views.match_detail, name='match_detail'),
    path('form/player/', views.get_player, name='get_player'),
    path('form/nation/', views.get_nation, name='get_nation'),
    path('form/ball/', views.get_ball, name='get_ball'),
    path('form/schedule/', views.get_sched, name='get_sched'),
    path('Latest_news/', views.index_news, name='index_news'),
    path('search_news', views.search_news, name='search_news'),
    path('player/<int:player_id>', views.player_detail, name='player_detail'),
    path('Latest_news/<int:article_id>/', views.detail, name='detail'),
    path('get_News/', views.get_News, name='get_News'),
    path('get_player_detail/', views.get_player_detail, name='get_player_detail'),
    
    path('player/', views.player , name='player'),
    path('nation/', views.nation , name='nation'),
    # path('<int:article_id>', views.news, name='news'),
  
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)

    # path('search', views.search , name='search'),
    # path('index_news/', views.news , name='news'),
    # , 
    # path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    # path('match/', views.match_index , name='match_index')