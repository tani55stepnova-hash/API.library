from rest_framework import serializers
from .models import Author, Book, Reader, Review

class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'country', 'bio', 'books_count']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    avg_rating = serializers.FloatField(read_only=True)
    reviews_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'description', 'price', 'pages', 'year',
            'author', 'author_id', 'in_stock', 'created_at',
            'avg_rating', 'reviews_count'
        ]

class ReaderSerializer(serializers.ModelSerializer):
    books_borrowed = BookSerializer(many=True, read_only=True)
    books_borrowed_ids = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='books_borrowed',
        write_only=True,
        many=True,
        required=False
    )
    
    class Meta:
        model = Reader
        fields = ['id', 'name', 'email', 'phone', 'address', 'books_borrowed', 'books_borrowed_ids', 'registered_at']

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )
    reader = serializers.StringRelatedField(read_only=True)
    reader_id = serializers.PrimaryKeyRelatedField(
        queryset=Reader.objects.all(), source='reader', write_only=True, required=False, allow_null=True
    )
    
    class Meta:
        model = Review
        fields = ['id', 'book', 'book_id', 'reader', 'reader_id', 'rating', 'text', 'created_at']