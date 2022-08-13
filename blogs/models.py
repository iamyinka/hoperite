import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150, blank=True,
                            null=True, db_index=True, unique=True)
    content = HTMLField()
    published_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-published_at",)
