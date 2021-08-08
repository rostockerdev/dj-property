from django.shortcuts import render


def home_view(request):
    context = {
        'title': 'Nothing'
    }
    return render(request, 'pages/index.html', context)
    
