import logging
from datetime import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import BadHeaderError
from django.shortcuts import redirect

from contacts.models import Contact


def contact(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        # Check user already contacted
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing"
                )
                return redirect("/listings/" + listing_id)
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=messages,
            user_id=user_id,
        )
        contact.save()

        # Email Send
        m_subject = "Property Listing Inquiry"
        m_body = f"There has been an inquiry for {listing}. Sign into the admin panel for more info"
        f_mail = "rostockerdev@gmail.com"
        t_mail = [realtor_email, "raselrostock@protonmail.com"]
        if m_subject and m_body and f_mail:
            try:
                send_mail(m_subject, m_body, f_mail, t_mail, fail_silently=False)
                messages.success(
                    request,
                    "Your request has been submitted, a realtor will get back to you soon.",
                )
            except BadHeaderError:
                messages.error(request, "Invalid header was set.")
                logging.getLogger("error_logger").error(
                    "Sorry, Was not possible to send the mail"
                )
                return redirect("/listings/" + listing_id)

        return redirect("/listings/" + listing_id)
