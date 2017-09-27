#usr/bin/python3

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns=[
    url(r'^$',views.start,name="Index"),
    url(r'^review',views.RevDone,name="RevForm"),
    url(r'(?P<rev_id>[0-9]+)/$',views.ReviewDetail,name="ReviewDetail")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)