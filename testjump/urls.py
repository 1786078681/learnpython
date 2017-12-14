from django.conf.urls import url, include

from backends import views
urlpatterns = [
    #
    # url(r'^api/test/', include("backends.urls.api_urls", namespace="api")),
    # # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^test/$', views.TestCreateView.as_view(), name="test_create_view"),
    # url(r'^test/(?P<pk>\d+)/update/$', views.TestUpdateView.as_view(), name="test_update_view"),
    # url(r'^books/', include("backends.urls.view_urls", namespace="books"))
    url(r'test/$', views.test),
]