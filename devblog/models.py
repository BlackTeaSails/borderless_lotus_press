from django.db import models
from django.utils import timezone
from draceditor.models import DraceditorField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    content = DraceditorField(default="")
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey('devblog.Post', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
