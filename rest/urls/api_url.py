#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-26 下午1:12
# @Author  : Gavin Gan
# @Site    : 
# @File    : api_url.py
# @Software: PyCharm

from django.conf.urls import url, include
from rest_framework import routers
from rest import api


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet, base_name="users")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = []
urlpatterns += router.urls

