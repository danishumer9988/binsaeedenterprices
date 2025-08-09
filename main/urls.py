from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-order/', views.submit_order, name='submit_order'),

    # Policy pages with both clean URLs and index.html support
    # re_path(r'^shipping-policy/(?:index\.html)?$', views.shipping_policy_view, name='shipping_policy'),
    # re_path(r'^returns-refunds/(?:index\.html)?$', views.returns_refunds_view, name='returns_refunds'),
    # re_path(r'^privacy-policy/(?:index\.html)?$', views.privacy_policy_view, name='privacy_policy'),

    # Alternative: If you prefer redirects instead of direct handling
    path('shipping-policy/', views.shipping_policy_view, name='shipping_policy'),
    path('shipping-policy/index.html', RedirectView.as_view(url='/shipping-policy/', permanent=True)),
    path('returns-refunds/', views.returns_refunds_view, name='returns_refunds'),
    path('returns-refunds/index.html', RedirectView.as_view(url='/returns-refunds/', permanent=True)),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('privacy-policy/index.html', RedirectView.as_view(url='/privacy-policy/', permanent=True)),
]