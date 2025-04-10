from django.contrib import admin

from core.admin import SingleInstanceAdmin
from contact.models import ContactMessage,ContactPageİndex
from portfolio.models import PortfolioItem

# Register your models here.
class ContactPageIndexAdmin(SingleInstanceAdmin):
    pass
admin.site.register(ContactMessage)
admin.site.register(ContactPageİndex, ContactPageIndexAdmin)