from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='videos/seasons/')
    banner = models.ImageField(upload_to='videos/banners/', blank=True)
    rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_episodes(self):
        return self.videos.count()

    def __str__(self):
        return self.name


class Video(models.Model):
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='videos'
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='videos/thumbnails/')
    duration = models.PositiveIntegerField(default=0)
    episode_number = models.PositiveIntegerField()
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['episode_number']
        unique_together = ['season', 'slug']

    def __str__(self):
        return self.title
    