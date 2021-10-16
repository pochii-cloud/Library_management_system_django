from django.contrib import admin

# Register your models here.
from core.models import Category, Contact, Book, Profile

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Profile)

