from django.contrib import admin
from .models import Author, Book, Reader, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_year', 'country', 'books_count']
    search_fields = ['name', 'country']
    list_filter = ['country']
    
    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = "Книг"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'year', 'in_stock']
    search_fields = ['title', 'description']
    list_filter = ['author', 'year', 'in_stock']
    list_editable = ['in_stock', 'price']

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'registered_at']
    search_fields = ['name', 'email']
    filter_horizontal = ['books_borrowed']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'reader', 'rating', 'created_at']
    list_filter = ['rating', 'book']
    search_fields = ['text']