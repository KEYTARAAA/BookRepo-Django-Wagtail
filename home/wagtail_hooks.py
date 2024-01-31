from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import Book, Author

class BookAdmin(SnippetViewSet):
    model = Book
    base_url_path = 'Bookadmin'
    menu_label = 'Book'
    menu_icon = 'doc-full-inverse'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('title', 'author', 'published', 'description')
    search_fields = ('title', 'description', 'author__name')
    #list_filter = ('title')
    ordering = ("-published")

register_snippet(BookAdmin)

class AuthorAdmin(SnippetViewSet):
    model = Author
    base_url_path = 'Authoradmin'
    menu_label = 'Author'
    menu_icon = 'user'
    menu_order = 201
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('name', 'description')
    search_fields = ('name')
    ordering = ("-name")

register_snippet(AuthorAdmin)