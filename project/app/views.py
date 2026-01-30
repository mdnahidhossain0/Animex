from django.shortcuts import render, get_object_or_404
from .models import Season, Video

def AnimeSeason(request):
    seasons = Season.objects.filter(is_active=True)
    return render(request, 'anime_season.html', {'seasons': seasons})



def Anime(request, slug):
    season = get_object_or_404(Season, slug=slug)

    # Get videos for this season (published)
    episodes = season.videos.filter(is_published=True).order_by('episode_number')

    # Precompute first and last safely
    first_episode = episodes.first()  # returns None if empty
    last_episode = episodes.last()    # returns None if empty

    return render(request, 'anime.html', {
        'season': season,
        'episodes': episodes,
        'first_episode': first_episode,
        'last_episode': last_episode,
    })



def VideoPlayer(request, video_id):
    episode = get_object_or_404(Video, id=video_id, is_published=True)
    season = episode.season

    next_episode = Video.objects.filter(
        season=season,
        episode_number__gt=episode.episode_number,
        is_published=True
    ).order_by('episode_number').first()

    return render(request, 'player.html', {
        'season': season,
        'episode': episode,
        'next_episode': next_episode
    })
