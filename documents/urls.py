from django.conf.urls import url

from documents import views

urlpatterns = [
    #url(r'^term=\.', views.get_name_author, name='get_name_author'),
    url(r'^$', views.search, name='search'),
    #url(r'^?term=.', views.get_name_author, name='get_name_author'),
    url(r'^(?P<id_doc>\d+)', views.document, name='document'),
]
