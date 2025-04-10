from django.db import models

from core.mixins import SeoMixin


# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class ContactPageİndex(SeoMixin):
    def __str__(self):
        return "Contact Page Index"
    class Meta:
        verbose_name_plural = "Contact Page Index"