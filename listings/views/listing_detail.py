from django.shortcuts import render, get_object_or_404

from listings.models import Listing


def listing_detail_view(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing, "title": "Listings"}
    return render(request, "listings/listing_detail.html", context)
