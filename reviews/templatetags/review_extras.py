from django import template
from books.models import Book
import math

register = template.Library()

@register.filter(name='stars')
def stars(value):
    try:
        num_stars = math.floor(float(value))
        return '★' * max(0, min(num_stars, 5))
    except (ValueError, TypeError):
        return ''

@register.simple_tag
def recent_books():
    return Book.objects.all().order_by('-publishing_date')[:3]
