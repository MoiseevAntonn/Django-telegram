from django.conf.urls import url,include
from . import views

app_name = 'auth'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^cabinet/$',views.cabinet,name='cabinet'),
    url(r'^get_email/$',views.get_email,name='get_email'),
    url(r'^link_with_account/$',views.link_with_account,name='link_with_account'),
    url(r'^get_links/$',views.get_links,name='get_links'),
    url(r'^register/$',views.register,name='register')
]