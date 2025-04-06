from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faq'