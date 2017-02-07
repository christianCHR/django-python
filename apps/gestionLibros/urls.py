from django.conf.urls import url, include
from views import inicio
urlpatterns = [
    url(r'^$',inicio),
]