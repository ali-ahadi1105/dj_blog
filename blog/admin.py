from django.contrib import admin
from .models import Article, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = { 'slug': ('title',) }

admin.site.register(Category, CategoryAdmin)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = { 'slug': ('title',) }
    ordering = ['-status', '-publish']
    
    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = 'دسته‌بندی'

admin.site.register(Article, ArticleAdmin)