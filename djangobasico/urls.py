from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
