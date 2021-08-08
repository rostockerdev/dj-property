from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.shortcuts import reverse

from listings.models import Listing
from realtors.models import Realtor


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['pages:about']

    def location(self, item):
        return reverse(item)


class ListingSitemap(sitemaps.Sitemap):

    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Listing.objects.all().order_by('-list_date')

    def location(self, item):
        return reverse('listings:listing-detail', kwargs={'listing_id': item.pk})


class RealtorSitemap(sitemaps.Sitemap):

    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Realtor.objects.all().order_by('-hire_date')

    def location(self, item):
        return reverse('realtors:realtor-detail', kwargs={'realtor_slug': item.slug})
