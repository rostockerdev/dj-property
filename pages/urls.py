from django.urls import path

from pages.views.home import home_view
from pages.views.about import about_view
from pages.views.faqs import faqs_view

app_name = "pages"

urlpatterns = [
    path('', home_view, name='index'),
    path('about', about_view, name='about'),
    path('faqs', faqs_view, name='faqs')
]
