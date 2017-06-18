from django.contrib import admin
from devblog.models import Post, Comment
from draceditor.widgets import AdminDraceditorWidget


admin.site.register(Post)
admin.site.register(Comment)
