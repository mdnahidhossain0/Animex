from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AnimeSeason, name='anime_season'),  # homepage
    path('anime/<slug:slug>/', Anime, name='anime_detail'),
    path('watch/<int:video_id>/', VideoPlayer, name='video_player'),
]
