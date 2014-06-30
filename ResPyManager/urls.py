from django.conf.urls import patterns, include, url
import model_report
from respy import views
from django.contrib import admin
from model_report import report

admin.autodiscover()
report.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ResPyManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index.html"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^novoAluguel/', views.novoaluguel),
    url(r'^excluirAluguel/(?P<id_aluguel>.*)/$', views.excluirAluguel),
    url(r'^finalizarAluguel/(?P<id_aluguel>.*)/$', views.finalizarAluguel),
	url(r'', include('model_report.urls')),
)
