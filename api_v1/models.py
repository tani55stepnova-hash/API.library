from django.db import models

class Author(models.Model):
    """Автор книги"""
    name = models.CharField(max_length=200, verbose_name="Имя автора")
    birth_year = models.IntegerField(null=True, blank=True, verbose_name="Год рождения")
    country = models.CharField(max_length=100, blank=True, verbose_name="Страна")
    bio = models.TextField(blank=True, verbose_name="Биография")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    """Книга"""
    title = models.CharField(max_length=200, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    pages = models.IntegerField(default=100, verbose_name="Количество страниц")
    year = models.IntegerField(verbose_name="Год издания")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        verbose_name="Автор"
    )
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Reader(models.Model):
    """Читатель библиотеки"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.TextField(blank=True, verbose_name="Адрес")
    books_borrowed = models.ManyToManyField(
        Book, 
        related_name='borrowed_by',
        blank=True,
        verbose_name="Взятые книги"
    )
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

class Review(models.Model):
    """Отзыв на книгу"""
    RATING_CHOICES = [
        (1, '⭐ - Плохо'),
        (2, '⭐⭐ - Так себе'),
        (3, '⭐⭐⭐ - Нормально'),
        (4, '⭐⭐⭐⭐ - Хорошо'),
        (5, '⭐⭐⭐⭐⭐ - Отлично'),
    ]
    
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='reviews',
        verbose_name="Книга"
    )
    reader = models.ForeignKey(
        Reader, 
        on_delete=models.CASCADE, 
        related_name='reviews',
        verbose_name="Читатель",
        null=True,
        blank=True
    )
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва")
    
    def __str__(self):
        return f"{self.rating}⭐ - {self.book.title}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"