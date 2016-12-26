from django.contrib import admin

from .models import Storyboard
from .models import Storyboarder


class StoryboardAdmin(admin.ModelAdmin):
    list_display = ('song', 'artist', 'set_id', 'storyboarders', 'date_added', 'date_created', 'medium', 'gallery', 'featured', 'classic')
    list_filter = ['date_added', 'date_created']
    search_fields = ['song', 'artist']
    fieldsets = [
        ('Metadata', {'fields': ['song', 'artist', 'set_id', 'mapper', 'date_added', 'date_created']}),
        ('Storyboard Stuff', {'fields': ['storyboarder', 'medium', 'gallery', 'video']}),
        ('Essay Questions', {'fields': ['comments', 'description']}),
        ('Flags', {'classes': ['collapse'],'fields': ['featured', 'classic']}),
    ]

    def storyboarders(self, obj):
        return ", ".join([sber.username for sber in obj.storyboarder.all()])

class StoryboarderAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile', 'title', 'role')
    search_fields = ['username']


admin.site.register(Storyboard, StoryboardAdmin)
admin.site.register(Storyboarder, StoryboarderAdmin)