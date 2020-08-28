from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^cv/$', views.cv_view, name='cv_view'),
    url(r'^cv/(?P<pk>\d+)/edit/$', views.cv_edit, name='cv_edit'),
    url(r'^cv/new/$', views.cv_new, name='cv_new'),
    
]

