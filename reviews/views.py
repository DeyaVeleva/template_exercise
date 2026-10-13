from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Review

def recent_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    context = {
        'page_title': 'Recent Reviews',
        'reviews': reviews,
        'current_year': timezone.now().year,
    }
    return render(request, 'reviews/recent_reviews.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'page_title': f'Review for {review.book.title}',
        'review': review,
        'current_year': timezone.now().year,
    }
    return render(request, 'reviews/review_detail.html', context)
