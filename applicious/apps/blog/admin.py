from django.contrib import admin

from blog import models


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Posts, PostsAdmin)
admin.site.register(models.Categories)
admin.site.register(models.Tags)
