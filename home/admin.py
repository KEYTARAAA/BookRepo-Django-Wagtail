from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'description', 'slug']
    
    prepopulated_fields = {'slug': ('title',)}
    ordering = ["-published"]
    list_filter = ['author']
    search_fields = ['title', 'description']




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug']
    
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ["-name"]
    search_fields = ['name', 'description']
    