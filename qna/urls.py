from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stream/$', views.StreamListView.as_view(), name='stream-listview'),
    # url(r'^popular/$', views.PopularListView.as_view(), name='popular-listview'),

    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-detailview'),

    url(r'^post/(?P<pk>\d+)/heart/$', views.HeartView, name='heart'),
    url(r'^post/(?P<pk>\d+)/unheart/$', views.UnheartView, name='unheart'),
]
