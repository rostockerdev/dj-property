from django.urls import path

from contacts.views.contact_view import contact

app_name = "contacts"

urlpatterns = [path("", contact, name="contact")]
