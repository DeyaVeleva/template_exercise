from django.db import models

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
    title = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=12, unique=True)
    genre = models.CharField(max_length=40, choices=GENRE_CHOICES, default='FICTION')
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

