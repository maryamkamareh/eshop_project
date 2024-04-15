from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'home_module/index_page.html')

def contact_page(request):
    return render(request, 'home_module/contact_page.html')

def site_header_component(request):
    contex = {
        'link' : 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_companent.html', contex)
def site_footer_component(request):
    return render(request, 'shared/site_footer_companent.html', {})
