from django.contrib import admin
from tweets.models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']

admin.site.register(Tag, TagAdmin)
admin.site.register(Tweet, TweetAdmin)
