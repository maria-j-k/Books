from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Book
from api.serializers import BookSerializer, BookWriteSerializer
from api.utils import download_books
from api.filters import BookFilterSet


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet

    def get_queryset(self):
        queryset = super(BookViewSet, self).get_queryset()

        order_by = self.request.query_params.get('sort', '')
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset


    @action(detail=False, methods=['post'])
    def db(self, request):
        q = request.data.get('q')
        books = download_books(q)
        serializer = BookWriteSerializer(data=books, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

