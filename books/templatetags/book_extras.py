from django import template

from books.models import Book

register = template.Library()


@register.simple_tag
def recent_books():
    return Book.objects.order_by('-publishing_date')[:3]
