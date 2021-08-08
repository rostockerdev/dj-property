from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.models import Listing

def listing_list_view(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    per_page = 6
    paginator = Paginator(listings, per_page)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings,
        'title': 'Listings'
    }
    return render(request, 'listings/listing_list.html', context)