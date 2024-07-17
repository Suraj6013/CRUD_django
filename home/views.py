from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def submit_form(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Process your data here, e.g., save to database
        return redirect('success_url')  # Redirect or return a response
    return render(request, 'index.html')  # Show the form on GET request
