from django.shortcuts import render

from listings.choices import bedroom_choices, price_choices, state_choices
from listings.models import Listing


def home_view(request):

    listings = (
        Listing.objects.select_related("realtor")
        .order_by("-list_date")
        .filter(is_published=True)[:3]
    )
    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "title": "Nothing",
    }
    return render(request, "pages/index.html", context)
