from django.contrib import admin

# Register your models here.
from api.models import Author, Book, Category

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

