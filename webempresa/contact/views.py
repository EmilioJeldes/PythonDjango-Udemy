from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse


# Create your views here.
def contact(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(data = request.POST)
        
        if form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            
            # Suponemos que ha salido ok y se redirecciona
            return redirect(reverse("contact") + "?ok")
    
    return render(request, "contact/contact.html", {"form": form})
