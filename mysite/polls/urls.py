from django.conf.urls import url,include

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.result,name='result'),
    url(r'^(?P<question_id>[0-9]+)/votes/$',views.votes,name='votes'),
    url(r'^(?P<question_id>[0-9]+)/add_comment/$',views.add_comment,name='add_comment'),
    url(r'^(?P<comment_id>[0-9]+)/del_comment/$',views.del_comment,name='del_comment'),
    url(r'^(?P<comment_id>[0-9]+)/add_like/$',views.add_like,name='add_like'),
    url(r'^page/(\d+)/$', views.index)
]
