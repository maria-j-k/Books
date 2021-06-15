from rest_framework import viewsets
import django_filters

from api.models import Author, Book
from api.serializers import BookSerializer


class BookFilterSet(django_filters.FilterSet):
    author = django_filters.ModelMultipleChoiceFilter(
            field_name='authors__name',
            lookup_expr='iexact',
            to_field_name='name', 
            queryset=Author.objects.all(), 
            conjoined=True)
    category = django_filters.CharFilter(
            field_name='categories__name', 
            lookup_expr='iexact')
    title = django_filters.CharFilter(
            field_name='title', 
            lookup_expr='iexact')
    published_date = django_filters.NumberFilter(field_name='published_date')
    ratings_count=django_filters.NumberFilter(field_name='ratings_count')
    average_rating__gt = django_filters.NumberFilter(
            field_name='average_rating', 
            lookup_expr='gt')
    average_rating__lt = django_filters.NumberFilter(
            field_name='average_rating', 
            lookup_expr='lt')

    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'categories', 'ratings_count', 'average_rating']


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



