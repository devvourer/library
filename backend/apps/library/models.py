from django.db import models

# from apps.users.models import Author
# from backend.apps.users.models import Author
from .enums import RATE_CHOICES
from ..users.models import Author, User
from statistics import mean


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Book name')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Book author', related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Book category', related_name='books')
    created_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255, verbose_name='Description', blank=True)

    def __str__(self):
        return self.name

    @property
    def rating(self):
        try:
            return mean(comment.rate for comment in self.comments.all())
        except:
            return 0


class Comment(models.Model):
    text = models.CharField(max_length=255, verbose_name='Comment text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Comment author', related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book comment', related_name='comments')
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, verbose_name='Book rate')

    def __str__(self):
        return f'{self.book}: {self.author} says - {self.text}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.book.name}'
