from django.conf.urls import patterns, include, url
from respy import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ResPyManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^equipamentos/', 'respy.views.equipamentos'),
)
