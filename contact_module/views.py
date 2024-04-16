from django.shortcuts import render, redirect
from .forms import ContactUsModelForm
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView,CreateView

from .models import ContactUs
class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
