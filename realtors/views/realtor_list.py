from django.shortcuts import render

from realtors.models import Realtor


def realtor_list_view(request):
    realtors = Realtor.objects.all()
    context = {"realtors": realtors, "title": "Realtors"}
    return render(request, "realtors/realtor_list.html", context)
