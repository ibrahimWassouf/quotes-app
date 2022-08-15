from django.urls import path
from .views import HomePageView, QuoteDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('quote/<int:pk>', QuoteDetailView.as_view(), name="quote_detail"),
]