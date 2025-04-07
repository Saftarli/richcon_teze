from django.shortcuts import render, get_object_or_404

from portfolio.models import PortfolioItem


# Create your views here.

def portfolio(request):
    items = PortfolioItem.objects.all()
    context = {
        'portfolio_items': items,
    }
    return render(request, 'portfolio/portfolio-three.html', context)

def portfolio_detail(request, id):
    item = get_object_or_404(PortfolioItem, id=id)
    return render(request, 'portfolio/portfolio-details.html', {'item': item})
