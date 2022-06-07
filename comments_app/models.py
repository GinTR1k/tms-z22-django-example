from django.contrib.auth.models import User
from django.db import models

from publication_app.models import Post


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
