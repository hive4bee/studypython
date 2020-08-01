from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    website=models.URLField()

    def __str__(self):
        return self.name
'''
테이블 간 관계를 나타내는 필드는 ForeignKey, ManyToManyField, OneToOneField
3가지가 있으며 각각 N:1, N:N, 1:1관계를 표시한다.
'''