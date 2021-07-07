from django.contrib import admin
from . import models

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'author',
        'text',
        'created',
        'content_type',
        'object_id'
    ]

admin.site.register(models.Comment, CommentAdmin)