from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Events'),
    url(r'^articles/$', views.articles, name='Articles'),
    url(r'^articles/(?P<alias>[a-zA-Z-]+)/$', views.article, name='Article'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)