from django.shortcuts import render

def portfolio(req):
    return render(req, 'portfolio.html')