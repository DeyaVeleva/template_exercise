from django.contrib import admin
from books.models import Book, Tag

admin.site.register(Book)
admin.site.register(Tag)
