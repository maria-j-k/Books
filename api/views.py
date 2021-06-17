from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Book
from api.serializers import BookSerializer, BookWriteSerializer, QSerializer
from api.utils import download_books
from api.filters import BookFilterSet


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet

    def get_queryset(self):
        queryset = super(BookViewSet, self).get_queryset()

        order_by = self.request.query_params.get('sort', '')
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset


class BookWriteView(generics.CreateAPIView):
    serializer_class = QSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        q = self.request.data.get('q')
        books = download_books(q)
        serializer = BookWriteSerializer(data=books, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

