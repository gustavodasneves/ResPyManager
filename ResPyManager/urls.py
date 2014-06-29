from django.conf.urls import patterns, include, url
from respy import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ResPyManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index.html"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^novoAluguel/', views.novoAluguel, name="novoaluguel.html"),
    url(r'^finalizarAluguel/', views.finalizarAluguel),
    url(r'^excluirAluguel/', views.excluirAluguel),
)
