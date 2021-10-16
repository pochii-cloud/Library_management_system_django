from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    total_quantity = models.PositiveIntegerField(default=0)
    details = models.CharField(max_length=500, default='zero')
    image = models.ImageField(default='null', upload_to='media')
    AdminUpload = models.FileField(upload_to='media', default='no file')
    borrowed = models.BooleanField(default=False)
    date = models.DateField('dd/mm/yy', auto_now=True)
    date2 = models.DateField(auto_now=False, auto_now_add=False, null=True)
    penalty = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=200, default='null')
    pages = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "books"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


class Contact(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "contacts"
