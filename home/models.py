from django.db import models
from django.utils import timezone
from django.urls import reverse

# Add these:
from wagtail.models import Page


class Author(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(default = "No description available")
    slug = models.SlugField(max_length = 200, unique=True)


    
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        reverse('home:book_details', args=[str(self.slug)])
    



class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name = "books")
    description = models.TextField(default = "No description available")
    published = models.DateField(default = timezone.now)
    image = models.ImageField()
    slug = models.SlugField(max_length = 200, unique=True)


    class Meta:
        ordering = ["-published"]



    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home:book_details', args=[str(self.slug)])