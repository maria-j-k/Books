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

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    title = models.CharField(max_length=255)
    published_date = models.CharField(max_length=10, blank=True)
    thumbnail =  models.URLField(blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    ratings_count = models.IntegerField(null=True)
    average_rating = models.FloatField(null=True)

    def __str__(self):
        return self.title

