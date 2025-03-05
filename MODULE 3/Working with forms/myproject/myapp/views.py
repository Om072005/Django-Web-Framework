from django.shortcuts import render , redirect
from .forms import BookingForm

def booking_view(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():  
            form.save()  
            return redirect('/booking/')  
    else:
        form = BookingForm()
    return render(request, "booking.html", {"form": form})

def home_view(request):
    return render(request, "home.html") 


