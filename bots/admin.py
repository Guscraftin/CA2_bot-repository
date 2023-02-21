from django.contrib import admin

from .models import Author, Bot


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'join_date')


class BotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['bot_name']}),
        ('Definitive bot information', {'fields': ['author', 'add_date'], 'classes': ['collapse']}),
        ('Modified information', {'fields': ['votes', 'description'], 'classes': ['collapse']}),
    ]
    list_display = ('bot_name', 'author', 'add_date', 'votes')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Bot, BotAdmin)
