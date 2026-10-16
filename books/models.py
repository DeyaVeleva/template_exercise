from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON_FICTION', 'Non-Fiction'),
        ('FANTASY', 'Fantasy'),
        ('SCIENCE_FICTION', 'Science Fiction (Sci-Fi)'),
        ('MYSTERY', 'Mystery & Detective'),
        ('THRILLER', 'Thriller & Suspense'),
        ('ROMANCE', 'Romance'),
        ('HORROR', 'Horror'),
        ('HISTORICAL_FICTION', 'Historical Fiction'),
        ('DYSTOPIAN', 'Dystopian'),
        ('Romantasy', 'Romantasy'),
        ('BIOGRAPHY', 'Biography & Memoir'),
        ('HISTORY', 'History'),
        ('SCIENCE', 'Science & Technology'),
        ('SELF_HELP', 'Self-Help & Personal Development'),
        ('BUSINESS_FINANCE', 'Business & Finance'),
        ('PHILOSOPHY', 'Philosophy'),
        ('PSYCHOLOGY', 'Psychology'),
        ('TRAVEL', 'Travel & Adventure'),
        ('COOKBOOKS', 'Cookbooks & Food'),
    ]
    title = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    image_url = models.URLField()
    genre = models.CharField(
        max_length=40,
        choices=GENRE_CHOICES,
        default='FICTION'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    publishing_date = models.DateField()
    isbn = models.CharField(
        max_length=12,
        unique=True
    )
    slug = models.SlugField(
        unique=True,
        max_length=100,
        blank=True,
    )
    publisher = models.CharField(
        max_length=100,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )
    books = models.ManyToManyField(
        Book,
    )

    def __repr__(self) -> str:
        return self.name
    def __str__(self) -> str:
        return self.name
