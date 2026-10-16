from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('books/', include([
        path('', views.book_list, name='list'),
        path('create/', views.book_create, name='create'),
        path('<slug:slug>/', include([
            path('edit/',views.book_edit, name='edit'),
            path('delete/',views.book_delete, name='delete'),
            path('', views.book_detail, name='detail'),
        ])),
    ]))

]
