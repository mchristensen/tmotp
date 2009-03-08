from django.conf.urls.defaults import *
import views

urlpatterns = patterns('foo.views',
    (r'^$', views.index),
)
