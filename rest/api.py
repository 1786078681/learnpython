#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-26 下午2:12
# @Author  : Gavin Gan
# @Site    : 
# @File    : api.py
# @Software: PyCharm
# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer