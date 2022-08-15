from django.shortcuts import render
from django.views.generic import ListView, DetailView
from quotations.models import BookQuote

# Create your views here.

class HomePageView(ListView):
    model = BookQuote
    template_name = 'home.html'

class QuoteDetailView(DetailView):
    model = BookQuote
    template_name = 'quote_detail.html'