from django.contrib import admin

from .models import Bot


# All changes made to the django admin panel
class BotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['bot_name']}),
        ('Modified information', {'fields': ['votes', 'description'], 'classes': ['collapse']}),
        ('Definitive bot information', {'fields': ['author_id', 'add_date'], 'classes': ['collapse']}),
    ]
    list_display = ('bot_name', 'author_id', 'add_date', 'votes')


admin.site.register(Bot, BotAdmin)
