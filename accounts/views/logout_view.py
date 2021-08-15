from django.shortcuts import redirect
from django.contrib import messages, auth


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Successfully logout.")
        return redirect("pages:index")
