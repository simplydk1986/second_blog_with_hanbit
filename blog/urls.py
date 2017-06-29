from django.conf.urls import url
from .views import *

urlpatterns = [
    #Example
    url(r'^$', PostLV.as_view(), name = 'index'),

    # Example : /post/ (same as /)
    url(r'^Post/$', PostLV.as_view(), name = 'post_list'),

    #Example : /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example : /archive/
    url(r'^archive/$', PostAV.as_view(), name = 'post_archive'),

    #Example : /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name = 'post_year_archive'),

    #Example : /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<mounth>[a-z]{3})/$', PostMAV.as_view(), name = 'post_mounth_archive'),

    #Example : /2012/nov/10
    url(r'^(?P<year>\d{4})/(?P<mounth>[a-z]{3})/(?P<day>\d{1,2})$', PostDAV.as_view(), name = 'post_day_archive'),

    # Example : /today/
    url(r'^today/$', PostTAV.as_view(), name = 'post_today_archive'),
]