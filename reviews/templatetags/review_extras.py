from django import template

register = template.Library()


@register.filter
def stars(value):
    if value is None:
        return "☆☆☆☆☆"

    try:
        rating = float(value)
    except (TypeError, ValueError):
        return "☆☆☆☆☆"

    rating = max(0, min(5, rating))
    full_stars = round(rating)

    return "★" * full_stars + "☆" * (5 - full_stars)
