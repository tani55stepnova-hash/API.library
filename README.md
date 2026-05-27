# API.library

## Описание проекта

API для управления библиотекой. Позволяет управлять книгами, авторами, читателями и отзывами.

## Функционал

- GET /authors/ - список авторов
- GET /authors/?search=Пушкин - поиск по имени
- GET /authors/{id}/ - один автор
- POST /authors/ - создать автора
- POST /authors/ (со списком) - массовое создание
- PATCH /authors/{id}/ - обновить автора
- DELETE /authors/{id}/ - удалить автора
- DELETE /authors/?ids=1,2,3 - массовое удаление

- GET /books/ - список книг
- GET /books/?min_price=500&max_price=2000 - фильтр по цене
- GET /books/?author_id=1 - фильтр по автору
- GET /books/?year=2020 - фильтр по году
- GET /books/?in_stock=true - только в наличии
- GET /books/{id}/ - одна книга
- POST /books/ - создать книгу
- POST /books/ (со списком) - массовое создание
- PATCH /books/{id}/ - обновить книгу
- DELETE /books/{id}/ - удалить книгу
- DELETE /books/?ids=1,2,3 - массовое удаление

- GET /readers/ - список читателей
- GET /readers/{id}/ - один читатель
- POST /readers/ - создать читателя
- POST /readers/ (со списком) - массовое создание
- POST /readers/{id}/borrow/ - взять книгу
- PATCH /readers/{id}/ - обновить читателя
- DELETE /readers/{id}/ - удалить читателя
- DELETE /readers/?ids=1,2,3 - массовое удаление

- GET /reviews/ - список отзывов
- GET /reviews/?book_id=1 - фильтр по книге
- GET /reviews/?rating=5 - фильтр по оценке
- GET /reviews/{id}/ - один отзыв
- POST /reviews/ - создать отзыв
- POST /reviews/ (со списком) - массовое создание
- PATCH /reviews/{id}/ - обновить отзыв
- DELETE /reviews/{id}/ - удалить отзыв
- DELETE /reviews/?ids=1,2,3 - массовое удаление

## Запуск

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 20000
