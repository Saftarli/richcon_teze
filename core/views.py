from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq/faq.html')

def error404(request):
    return render(request, '404-error.html')

def gallery(request):
    return render(request, 'gallery.html')

def portfolio(request):
    return render(request, 'portfolio-three.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')

def requests(request):
    return render(request, 'request-quote.html')

def services(request):
    return render(request, 'services.html')

def servicedetails(request):
    return render(request, 'services-details.html')

def  team (request):
    return render(request, 'team-two.html')