from django.urls import path
from portfolio.views import portfolio_detail, portfolio


urlpatterns = [
    path('', portfolio, name='portfolio'),
    path('<int:id>/', portfolio_detail, name='portfolio-detail'),
]