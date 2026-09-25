from django.http import JsonResponse

from .models import Book


def book_list(request):
    books = Book.objects.values("id", "title", "author", "year")
    return JsonResponse({"books": list(books)})
