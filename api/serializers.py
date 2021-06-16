from rest_framework import serializers

from api.models import Author, Book, Category


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('name',)
        extra_kwargs = {
            'name': {
                'validators': []
                }
            }


    def create(self, validated_data):
        return Author.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)
        extra_kwargs = {
            'name': {
                'validators': []
                }
            }

    
    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)   

    class Meta:
        model = Book
        fields = ('title', 'published_date', 
                'thumbnail', 'authors', 'categories', 
                'average_rating', 'ratings_count',
                )


class BookWriteSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(many=True, required=False)
    id = serializers.CharField()
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'published_date', 'thumbnail', 'authors', 
                'categories', 'average_rating', 'ratings_count',
                )


    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        categories_data = validated_data.pop('categories')
        book, _ = Book.objects.update_or_create(**validated_data)
        for author in authors_data:
            a = Author.objects.create(**author)
            book.authors.add(a)
        for category in categories_data:
            cat = Category.objects.create(**category)
            book.categories.add(cat)
        return book

