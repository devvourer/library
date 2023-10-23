from django.contrib import admin

from .models import Book, Comment, Category, Favorite

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Favorite)
