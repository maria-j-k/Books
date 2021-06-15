from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.IntegerField()
    thumbnail =  models.URLField(blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    ratings_count = models.IntegerField(null=True)
    average_rating = models.FloatField(null=True)

    def __str__(self):
        return self.title
    





#{
#    "title": "Hobbit czyli Tam i z powrotem",
#    "authors": ["J. R. R. Tolkien"],
#    "published_date": "2004",
#    "categories": [
#        "Baggins, Bilbo (Fictitious character)"
#      ],
#    "average_rating": 5,
#    "ratings_count": 2,
#    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
#}
