from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^$', views.api_root),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^statuses/$', views.StatusList.as_view()),
    url(r'^statuses/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
