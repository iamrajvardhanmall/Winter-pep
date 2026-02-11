from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def RajView(Request):
    return HttpResponse("Welcome to Raj's Django Application!")

def RajTemplateView(Request):
    return render(Request, 'raj.html')

def saveDetails(Request):
    print(Request.POST)
    title = Request.POST.get("title", "")
    description = Request.POST.get("description", "")

    if not title or not description:
        messages.error(Request, "Fill all details")
        return redirect("save_data")

    # return HttpResponse(f"Title= {Request.POST.get('title')} Description = {Request.POST.get('description')}")
    return render(Request, 'saveDetails.html')

def base(Request):
    return render(Request, 'base.html')