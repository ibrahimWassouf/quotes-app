from django.urls import path
from .views import HomePageView, QuoteDetailView, QuoteCreateView, QuoteUpdateView, QuoteDeleteView, CollectionsList, CollectionDetailView

urlpatterns = [
    path('quote/<int:pk>/edit', QuoteUpdateView.as_view(), name = 'quote_edit'),
    path('', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name="quote_detail"),
    path('quote/new/', QuoteCreateView.as_view(), name = 'quote_new'),
    path('quote/<int:pk>/delete', QuoteDeleteView.as_view(), name='quote_delete'),
    path('collections', CollectionsList.as_view(), name='collections'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail')
]