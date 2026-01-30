from django.contrib import admin

from .models import Season, Video

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'is_active',
        'release_date',
        'created_at',
    )

    list_filter = (
        'is_active',
        'release_date',
    )

    search_fields = (
        'name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    ordering = ('-created_at',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'season',
        'episode_number',
        'duration',
        'views',
        'is_published',
        'created_at',
    )

    list_filter = (
        'is_published',
        'season',
    )

    search_fields = (
        'title',
        'season__name',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    autocomplete_fields = (
        'season',
    )

    ordering = ('episode_number',)
