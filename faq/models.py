from django.db import models
from core.mixins import SeoMixin


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

class FaqPageIndex(SeoMixin):
    def __str__(self):
        return 'Faq Page Index'
    class Meta:
        verbose_name = 'Faq Page Index'