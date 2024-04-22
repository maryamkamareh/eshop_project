from django.shortcuts import render, redirect

from site_module.models import SiteSetting
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
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_module/create_profile_page.html')
    def post(self,request):
        store_file(request.FILES['image'])
        return redirect('/contact-us/create-profile/')

