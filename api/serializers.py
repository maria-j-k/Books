from rest_framework import serializers

from api.models import Author, Book, Category


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)   
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'published_date', 
                'thumbnail', 'authors', 'categories', 
                'average_rating', 'ratings_count',
                )

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name')


