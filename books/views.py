from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1


class BookView(APIView):

    def get(self, request):
        book = Book.objects.all().order_by('id')
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(book, request)
        serializer = BookSerializer(result_page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookEditView(APIView):
    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response({"status": "success"})