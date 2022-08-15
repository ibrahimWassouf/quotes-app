from django.urls import path
from .views import HomePageView, QuoteDetailView, QuoteCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>', QuoteDetailView.as_view(), name="quote_detail"),
    path('quote/new', QuoteCreateView.as_view(), name = 'quote_new'),
]