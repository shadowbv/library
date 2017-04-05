from django.conf.urls import url

from documents import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^(?P<id_doc>\d+)', views.document, name='document'),
]
