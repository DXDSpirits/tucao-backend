from django.contrib import admin
from django.forms import Textarea, SelectMultiple
from tweets.models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_filter = ('tags',)
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 50})},
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'style': 'height: 20em; min-width: 10em;'})},
    }

admin.site.register(Tag, TagAdmin)
admin.site.register(Tweet, TweetAdmin)
