from django.shortcuts import get_object_or_404, render

from listings.choices import bedroom_choices, price_choices, state_choices
from listings.models import Listing


def listing_search_view(request):
    qs = Listing.objects.order_by("-list_date")
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            qs = Listing.objects.filter(description__icontains=keywords)

    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            qs = Listing.objects.filter(city__iexact=city)

    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            qs = Listing.objects.filter(state__iexact=state)

    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            qs = Listing.objects.filter(bedrooms__lte=bedrooms)

    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            qs = Listing.objects.filter(price__lte=price)

    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "listings": qs,
        "search_value": request.GET,
    }
    return render(request, "listings/listing_search.html", context)
