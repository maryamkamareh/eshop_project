from django.shortcuts import render, redirect
from .forms import ContactUsForms, ContactUsModelForm
# Create your views here.
from django.urls import reverse
from django.views import View

from .models import ContactUs
class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
    def post(self, request):
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid(): #checl the format of input
            print(contact_form.cleaned_data)
            contact_form.save() # kare balaro mikone
            return redirect('home_page')
        return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})


def contact_us_page(request):
    if request.method == 'POST':
        #contact_form = ContactUsForms(request.POST)
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid(): #checl the format of input
            print(contact_form.cleaned_data)
            contact_form.save() # kare balaro mikone
            return redirect('home_page')
    else:
        #contact_form = ContactUsForms()
        contact_form = ContactUsModelForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})