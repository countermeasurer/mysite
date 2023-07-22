from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.post_list, name='post_list'),
    path(r'^(?p<year>\d{4}/(?P<month>\d{2}/(?p<day>\d{2}/'
         r'(?P<post>[-\w]+/$',
         views.post_detail,
         name='post_detail'),
]
