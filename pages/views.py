from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from quotations.models import BookQuote, Collections
from users.models import CustomUser
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

class HomePageView(ListView):
    model = BookQuote
    template_name = 'home.html'

class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = BookQuote
    template_name = 'quote_detail.html'

class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = BookQuote
    template_name = 'quote_new.html'
    fields = ['title', 'author', 'quote']

class QuoteUpdateView(LoginRequiredMixin, UpdateView):
    model = BookQuote
    template_name = 'quote_edit.html'
    fields = ['title', 'author', 'quote']

class QuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = BookQuote
    template_name='quote_delete.html'
    success_url = reverse_lazy('home')


@receiver(post_save, sender=CustomUser)
def createAllCollections(sender, instance, created, **kwargs):
    if created:
        allCollections = Collections(title="All Quotes")
        allCollections.save()
    else:
        pass