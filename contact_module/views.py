from django.shortcuts import render, redirect
from .forms import ContactUsForms
# Create your views here.
from django.urls import reverse


def contact_us_page(request):
    # if request.method == 'POST':
    #     entered_email = request.POST['email']
    #     if entered_email == '':
    #         return render(request, 'contact_module/contact_us_page.html', {'has_error':True})
    #     print(request.POST)
    #     return redirect(reverse('home_page'))
    if request.method == 'POST':
        contact_form = ContactUsForms(request.POST)
        if contact_form.is_valid(): #checl the format of input
            print(contact_form.cleaned_data)
            return redirect('home_page')
    else:
        contact_form = ContactUsForms()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})