from django.db import models

# Create your models here.

from django.db import models


class ContactMessage(models.Model):
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    was_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.message[:30]}..."