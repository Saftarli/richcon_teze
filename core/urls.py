from django.urls  import  path
from core.views import (index, about,gallery,error404,portfoliodetails,
                        portfolio,requests,services,servicedetails,team)
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('error404/', error404, name='error404'),
    path('portfoliodetails/', portfoliodetails, name='portfoliodetails'),
    path('portfolio/', portfolio, name='portfolio'),
    path('services/', services, name='services'),
    path('servicedetails/', servicedetails, name='servicedetails'),
    path('team/', team, name='team'),
    path('requests/', requests, name='requests'),

]

