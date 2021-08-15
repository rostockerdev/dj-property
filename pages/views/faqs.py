from django.shortcuts import render


def faqs_view(request):
    context = {"title": "FAQ"}
    return render(request, "pages/faqs.html", context)
