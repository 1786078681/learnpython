# -*- coding: utf-8 -*-
# @Time    : 18-1-9 下午2:28
# @Author  : Gavin Gan
# @File    : count.py

from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
class Count(MiddlewareMixin):

    def process_request(self, request):
        # val = {"/": 3, "/test/": 5}
        print(request.path_info)
        val = cache.get("val")
        if not val:
            val = {request.path_info: 1}

        if request.path_info in val:
            print(val.get(request.path_info))
            val[request.path_info] += 1
        else:
            val.update({request.path_info: 1})
        cache.set("val", val)
        print(cache.get("val"))

    def process_response(self, request, response):
        return response
