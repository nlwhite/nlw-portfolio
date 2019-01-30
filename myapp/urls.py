from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

import gis_portfolio_pieces.views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name='home'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('pronk/', admin.site.urls),
    path('', gis_portfolio_pieces.views.nlw, name='home'),
    path('portfolio_pieces/<int:piece_id>', gis_portfolio_pieces.views.detail, name='detail'),
    path('about/', TemplateView.as_view(template_name='static_pages/about.html'), name='about'),
    path('skills/', TemplateView.as_view(template_name='static_pages/skills.html'), name='skills'),
    path('contact/', gis_portfolio_pieces.views.contact, name='contact'),
    path('geo/', gis_portfolio_pieces.views.nlw, name='home'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
