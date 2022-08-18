from django.urls import path, include

from books.views import BookView, BookEditView



urlpatterns = [
    path('', BookView.as_view()),
    path('<int:id>', BookEditView.as_view()),
]
