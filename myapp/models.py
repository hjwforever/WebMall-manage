from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class User(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    add_time = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
