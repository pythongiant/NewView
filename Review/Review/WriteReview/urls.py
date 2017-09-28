#usr/bin/python3

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns=[
    url(r'^$',views.start,name="Index"),
    url(r'^review',views.RevDone,name="RevForm"),
    url(r'(?P<rev_id>[0-9]+)/$',views.ReviewDetail,name="ReviewDetail"),
    url(r'^art$',views.form,name="articleForm"),
    url(r'login$',views.loginForm,name="login"),
    url(r'signup$',views.signupForm,name="signup"),
    url(r'sign$',views.signup,name="add"),
    url(r'loginForm$',views.loginAction,name="login"),
    url(r'signout$',views.signout,name="asignout")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)