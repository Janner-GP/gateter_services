import uuid
from django.db import models
from django.conf import settings

class Meow(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text