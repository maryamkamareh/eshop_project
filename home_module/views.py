from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView
from product_module.models import Product
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.convertors import group_list


class HomeView(TemplateView):  # in va 2 taye bala ye kar mikonan
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['sliders'] = Slider.objects.filter(is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[0:12]
        most_visit_products =Product.objects.filter(is_active=True, is_delete=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[0:12]

        contex['latest_products'] = group_list(latest_products)
        contex['most_visit_products'] = group_list(most_visit_products)
        return contex


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    contex = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_companent.html', contex)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    contex = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_companent.html', contex)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
