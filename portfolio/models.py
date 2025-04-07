from django.db import models

# Create your models here.

class PortfolioItem(models.Model):
    tittle = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
