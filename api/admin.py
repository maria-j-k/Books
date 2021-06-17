from django.contrib import admin

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

