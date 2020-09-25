from django.shortcuts import render
from .models import Portfolio

def portfolio(req):
    portfolios = Portfolio.objects
    return render(req, 'portfolio.html', {'portfolios' : portfolios})