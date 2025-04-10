from django.db import models

from core.mixins import SeoMixin


# Create your models here.

class PortfolioItem(SeoMixin):
    tittle = models.CharField(max_length=100, help_text='Işin adı')
    subject = models.CharField(max_length=100, help_text='Hansı iş olduğunu qeyd etmək')
    image = models.ImageField(null=True, blank=False, help_text='Əsas şəkil, Şəkil ölçüləri mütləq verilmiş ölçüdə olmalıdır 1300x750 ')
    content = models.TextField(help_text='İş haqqında məlumat')
    image1 = models.ImageField(null=True, blank=False, help_text='453x499, Şəkil ölçüləri mütləq verilmiş ölçüdə olmalıdır. ')
    image2 = models.ImageField(null=True, blank=False, help_text='572x421, Şəkil ölçüləri mütləq verilmiş ölçüdə olmalıdır. ')
    content2 = models.TextField(null=True, blank=True, help_text='İş haqqında məlumat')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle


class PortfolioIndexPage(SeoMixin):
    def __str__(self):
        return "Portfolio Index Page"
    class Meta:
        verbose_name = "Portfolio Index Page"

