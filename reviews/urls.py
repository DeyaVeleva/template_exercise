from django.urls import path
from . import views

urlpatterns = [
    path('', views.recent_reviews, name='recent_reviews'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
]
