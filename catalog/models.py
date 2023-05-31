from django.db import models

# Create your models here.

class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    birth_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Author: {self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book{self.id} title = {self.title} authors_id: {self.author.id}'
    
    class Meta:
        ordering  = ['author__last_name', 'title']
        verbose_name = 'Bookington'
        indexes = [
            models.Index(fields=['title', 'author']),
        ]