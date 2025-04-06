from django.shortcuts import render
from faq.models import Faq

# Create your views here.

def faq(request):
    context = {
        'faqlar': Faq.objects.all(),
    }
    return render(request, 'faq/faq_test.html', context)