from django.contrib import admin
from portfolio.models import PortfolioItem, PortfolioIndexPage

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(PortfolioIndexPage)