from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home  , name='index'),
    url(r'^donate', views.donate  , name='donate'),
    url(r'^about', views.about  , name='about'),
    url(r'^sent', views.message_sent  , name='message'),
    url(r'^contact', views.contact  , name='contact'),
    url(r'^messagesent', views.message_sent2  , name='message2'),
    url(r'^report', views.report  , name='report'),
    url(r'^detailssent', views.details_sent  , name='details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)