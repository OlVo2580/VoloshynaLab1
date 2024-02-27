from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/library/
    path('about/', about, name='about'),
    path('author/', author, name='author'),
    path('subject/', subject, name='subject'),
    path('abstract/<int:edition_id>/', abstract, name='abstract'), # Доданий новий URL маршрут для сторінки з деталями книги,
    path('author/<int:author_id>/', author_edition, name='author_edition')
    ]
