from django.conf.urls import url
from .views import post_list
from .views import post_detail
 
urlpatterns = [
    url(r'^blog/$', post_list),
    url(r'^blog/(?P<id>\d+)/$', post_detail),
]