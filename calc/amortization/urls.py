from django.conf.urls import patterns, url

from amortization import views

urlpatterns = patterns('',
		    url(r'^$', views.browse, name='browse'),
		    url(r'^add$', views.add, name='add'),
		    url(r'^new$', views.new, name='new'),
		    url(r'^(?P<loan_id>\d+)/$', views.read, name='read'),
		        # ex: /loans/1/
		    )
