from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def error404(request):
    return render(request, '404-error.html')

def gallery(request):
    return render(request, 'gallery.html')



def requests(request):
    return render(request, 'request-quote.html')

def servicedetails(request):
    return render(request, 'services/services-details.html')

def  team (request):
    return render(request, 'team-two.html')