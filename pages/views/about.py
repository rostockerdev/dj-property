from django.shortcuts import render

def about_view(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'pages/about.html', context)