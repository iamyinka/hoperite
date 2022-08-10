import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super().save(self, *args, **kwargs)
