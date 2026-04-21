from django.db import models
from django.utils import timezone
from datetime import timedelta

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']




class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)

    def __str__(self):
        return f'{self.published_date} - {self.title}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_date']

    def __str__(self):
        return f'{self.author_name}: {self.text[:20]}'