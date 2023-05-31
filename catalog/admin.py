from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
from catalog.models import Book, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'show_books')

    def show_books(self, obj):
        count = Book.objects.filter(author=obj).count()
        url = reverse('admin:catalog_book_changelist') + f'?author__id__exact={obj.id}'
        plural = 's' if count > 1 else ''

        return format_html(f'<a href="{url}">{count} book{plural}</a>')

  

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_last_name') 
    list_filter = ('author',)

    def author_last_name(self, obj):
        return obj.author.last_name