from rest_framework import permissions, viewsets, filters

from rest_framework.response import Response
from .models import Author, Books
from .serializer import AuthorSerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backend = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fileds = ['name']
    ordering_fileds = ['name']

class BookView(viewsets.ModelViewSet):
    queryset = Books.objects.related('author').all()
    serializer_class = BookSerializer
    filter_backend = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fileds = ['author__name', 'genre']
    ordering_fileds = ['published_date']

    def list(self,request,*args,**kwargs):
        cache_key='book_list'
        cached_books = cache.get(cache_key)
        if cached_books:
            return Response(cached_books)
        response = super().list(request,*args,**kwargs)
        cache.set(cache_key, response.data,timeout=60*15)
        return response

    def perform_create(self,serializer):
        super().perform_create(serializer)
        cache.delete('book_list')
    def perform_update(self,serializer):
        super().perform_update(serializer)
        cache.delete('book_list')
    def perform_destroy(self,instance):
        super().perform_destroy(instance)
        cache.delete('book_list')
