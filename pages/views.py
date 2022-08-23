from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    #updates the query set to include only the quotes created by the user
    def get_queryset(self):
        quoteList = BookQuote.objects.all().filter(creator=self.request.user)
        return quoteList

class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = BookQuote
    template_name = 'quote_detail.html'

class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = BookQuote
    template_name = 'quote_new.html'
    fields = ['title', 'author', 'quote']

    #automatically fills the creator field with the user's name
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class QuoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookQuote
    template_name = 'quote_edit.html'
    fields = ['title', 'author', 'quote']

    #ensures only the correct user -the creator- has access to the view
    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user.username

class QuoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BookQuote
    template_name='quote_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user.username

class CollectionsList(ListView):
    model = Collections
    template_name = 'collections_list.html'

    def get_queryset(self):
        collectionList = Collections.objects.all().filter(creator= self.request.user)
        return collectionList

class CollectionDetailView(DetailView):
    model = Collections
    template_name= 'collection_detail.html'

class CollectionCreateView(CreateView):
    model = Collections
    template_name = 'collection_new.html'
    fields = ['title']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



#creates a collection called 'All Quotes' for each newly signed up user
@receiver(post_save, sender=CustomUser)
def createAllCollections(sender, instance, created, **kwargs):
    if created:
        allCollections = Collections(title="All Quotes", creator = instance.username )
        allCollections.save()

#adds each newly made quote into the user's specific 'all quotes' collection
@receiver(post_save, sender=BookQuote)
def quoteCreated(sender, instance, created, **kwargs):
    if created:
        allCollections = Collections.objects.get(creator=instance.creator)
        allCollections.quotes.add(instance)
