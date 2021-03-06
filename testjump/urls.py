from django.conf.urls import url, include

from backends import views, models

urlpatterns = [
    #
    # url(r'^api/test/', include("backends.urls.api_urls", namespace="api")),
    # # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^test/$', views.TestCreateView.as_view(), name="test_create_view"),
    # url(r'^test/(?P<pk>\d+)/update/$', views.TestUpdateView.as_view(), name="test_update_view"),
    # url(r'^books/', include("backends.urls.view_urls", namespace="books"))
    # url(r'test/$', views.test),
    url(r'^api/', include("rest.urls.api_url", namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^asio$', views.testAsio),

]

l = [url(r'^%s/$' % a.path_info, views.testurl) for a in models.MyUrl.objects.all()]

urlpatterns += l
#
# l = [a.path_info for a in models.MyUrl.objects.all()]
# print(l)
