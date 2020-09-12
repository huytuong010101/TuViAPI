from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api', views.api),
    url(r'^$', views.lasotuvi_django_index)
]