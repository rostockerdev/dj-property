from django.shortcuts import render
from django.views.generic import DetailView

from realtors.models import Realtor

class RealtorDetailView(DetailView):

    def get(self, *args, **kwargs):
        realtor_slug = kwargs['realtor_slug']
        realtor = Realtor.objects.get(slug=realtor_slug)
        context = {
            'realtor': realtor,
            'title': realtor.name
        }
        return render(self.request, 'realtors/realtor_detail.html', context)
        