from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/profile.html')

def contact(request):
    return render(request, 'dashboard/basic.html', {'content': ['my email', 'laura@koalacoder.com']})
# Create your views here.
