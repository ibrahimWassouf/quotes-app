from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from quotations.models import BookQuote
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = BookQuote
    template_name = 'home.html'

class QuoteDetailView(DetailView):
    model = BookQuote
    template_name = 'quote_detail.html'

class QuoteCreateView(CreateView):
    model = BookQuote
    template_name = 'quote_new.html'
    fields = ['title', 'author', 'quote']

class QuoteUpdateView(UpdateView):
    model = BookQuote
    template_name = 'quote_edit.html'
    fields = ['title', 'author', 'quote']

class QuoteDeleteView(DeleteView):
    model = BookQuote
    template_name='quote_delete.html'
    success_url = reverse_lazy('home')