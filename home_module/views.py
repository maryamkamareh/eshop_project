from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView

# def index_page(request):
#     return render(request, 'home_module/index_page.html')

# class HomeView(View):
#     def get(self, request):
#         contex = {}
#         return render(request, 'home_module/index_page.html', contex)

class HomeView(TemplateView): # in va 2 taye bala ye kar mikonan
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['data'] = 'this is data in home page'
        return contex


def site_header_component(request):
    contex = {
        'link' : 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_companent.html', contex)
def site_footer_component(request):
    return render(request, 'shared/site_footer_companent.html', {})
