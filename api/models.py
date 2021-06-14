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


class BookQuerySet(models.QuerySet):
    def avg_rating(self):
        return self.annotate(
            ann_overdue=models.Case(
            models.When(borrowed__when__lte=pendulum.now().subtract(months=2),
            then=True),
            default=models.Value(False),
            output_field=models.BooleanField()
                )
            )


class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.IntegerField()
    thumbnail =  models.URLField()
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        val = Rating.objects.filter(
                book__title=self.title).aggregate(models.Avg('value'))
        return val['value__avg']
    
    @property
    def ratings_count(self):
        return self.rating_set.count()


class Rating(models.Model):
    value = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.book.title}, {self.value}'



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
