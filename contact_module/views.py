from django.shortcuts import render, redirect
from .forms import ContactUsForms, ContactUsModelForm
# Create your views here.
from django.urls import reverse

from .models import ContactUs


def contact_us_page(request):
    # if request.method == 'POST':
    #     entered_email = request.POST['email']
    #     if entered_email == '':
    #         return render(request, 'contact_module/contact_us_page.html', {'has_error':True})
    #     print(request.POST)
    #     return redirect(reverse('home_page'))
    if request.method == 'POST':
        #contact_form = ContactUsForms(request.POST)
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid(): #checl the format of input
            print(contact_form.cleaned_data)
            # contact = ContactUs(
            #     title=contact_form.cleaned_data.get('title'),
            #     full_name=contact_form.cleaned_data.get('full_name'),
            #     email=contact_form.cleaned_data.get('email'),
            #     message=contact_form.cleaned_data.get('message')
            # )
            # contact.save()
            contact_form.save() # kare balaro mikone
            return redirect('home_page')
    else:
        #contact_form = ContactUsForms()
        contact_form = ContactUsModelForm()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})