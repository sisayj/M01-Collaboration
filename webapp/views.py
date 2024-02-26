from django.shortcuts import render

def home(request):
    context = {
        'title': 'Dynamic Web Page',
        'content': 'Welcome to our dynamic web page!'
    }
    return render(request, 'home.html', context)

