from django.conf.urls import url


from . import views

app_name = 'pipkin'
urlpatterns = [
    # example: /pipkin/
    url(r'^$', views.index, name='index'),
    url(r'^persons/$', views.PersonsListView.as_view(), name='persons'),
    url(r'^person/(?P<pk>[0-9]+)$', views.PersonDetailView.as_view(), name='person'),
]
