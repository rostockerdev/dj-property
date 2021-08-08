from django.urls import path 

from listings.views.listing_list import listing_list_view
from listings.views.listing_detail import listing_detail_view
from listings.views.listing_search import listing_search_view


app_name = 'listings'

urlpatterns = [
    path('', listing_list_view, name='listing-list'),
    path('<int:listing_id>', listing_detail_view, name='listing-detail'),
    path('search', listing_search_view, name='listing-search')
]
