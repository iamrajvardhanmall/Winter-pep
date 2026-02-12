from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def RajView(Request):
    return HttpResponse("Welcome to Raj's Django Application!")

def RajTemplateView(Request):
    return render(Request, 'raj.html')

def saveDetails(Request):
    if Request.method == 'POST':
        title = Request.POST.get("title", "")
        description = Request.POST.get("description", "")
        
        if not title or not description:
            messages.error(Request, "Fill all details")
            return redirect('raj/')  # Redirect to form page instead of rendering
        
        # Process valid data
        return render(Request, 'saveDetails.html')
    
    # Handle GET request - show the form
    return render(Request, 'raj.html')

def base(Request):
    return render(Request, 'base.html')