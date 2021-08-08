from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contacts.models import Contact


@login_required(login_url='/accounts/login')
def dashboard(request):
    contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)