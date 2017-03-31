from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'test_pr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^student/', include('students.urls')),
    url(r'^document/', include('documents.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()