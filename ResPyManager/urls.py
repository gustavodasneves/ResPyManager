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
<<<<<<< HEAD
    url(r'^admin/', include(admin.site.urls)),
	(r'', include('model_report.urls')),
=======
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^novoAluguel/$', views.novoAluguel, name="novoaluguel.html"),
    url(r'^excluirAluguel/(?P<id_aluguel>.*)/$', views.excluirAluguel),
    url(r'^finalizarAluguel/(?P<id_aluguel>.*)/$', views.finalizarAluguel),
>>>>>>> c6837c3bd908e7fd08d83aa2e9b183b635bbc95b
)
