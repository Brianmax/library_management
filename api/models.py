from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Reader(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    edition = models.SmallIntegerField(default=1)
    category = models.CharField(max_length=20)
    price = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Rental(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now=True)


class Staff(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
