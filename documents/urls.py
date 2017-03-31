from django.conf.urls import url

from documents import views

urlpatterns = [
    url(r'^(?P<id_doc>\d+)', views.index, name='index'),
]
