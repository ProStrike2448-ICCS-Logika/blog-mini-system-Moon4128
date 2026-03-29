from django.db import models

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

    def __str__(self):
        return f'{self.published_date} - {self.title}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']