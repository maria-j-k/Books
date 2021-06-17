from django.db import models


class AuthorManager(models.Manager):

    def create(self, name):
        author = Author.objects.filter(name=name).first()
        if author:
            return author
        else:
            author = Author(name=name)
            author.save()
        return author


class CategoryManager(models.Manager):

    def create(self, name):
        category = Category.objects.filter(name=name).first()
        if category:
            return category
        category = Category(name=name)
        category.save()
        return category


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = AuthorManager()


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name


class BookManager(models.Manager):

    def create_or_update(self, id, title, published_date, 
            thumbnail, ratings_count, average_rating):
        book = Book.objects.filter(id=id).first()
        if book:
            book.id=id 
            book.title=title 
            book.published_date=published_date 
            book.thumbnail=thumbnail 
            book.ratings_count=ratings_count 
            book.average_rating=average_rating
        else:
            book = Book(id=id, title=title, 
            published_date=published_date, 
            thumbnail=thumbnail, 
            ratings_count=ratings_count, 
            average_rating=average_rating)
        book.save()
        return book


class Book(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    title = models.CharField(max_length=255)
    published_date = models.CharField(max_length=10, blank=True)
    thumbnail =  models.URLField(blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    ratings_count = models.IntegerField(null=True)
    average_rating = models.FloatField(null=True)
    objects = BookManager()

    def __str__(self):
        return self.title

