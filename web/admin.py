from django.contrib import admin
from web.models import Team, Blog, Category

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'order']
    ordering = ['order']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", )
    list_filter = ("category", "author")
    search_fields = ("title", "author", "content")
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]