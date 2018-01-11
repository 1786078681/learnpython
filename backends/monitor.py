# -*- coding: utf-8 -*-
# @Time    : 18-1-11 下午5:47
# @Author  : Gavin Gan
# @File    : monitor.py

from django.views.generic import DetailView, TemplateView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin


class UserAdminRequireMixin(UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        elif not self.request.user.is_superuser:
            self.raise_exception = True
            return False
        return True


class GameServerDetail(UserAdminRequireMixin, UpdateView):
    model = ""
    template_name = ""
    form_class = ""

    def get_context_data(self, **kwargs):
        kwargs.update({
            "title": "update ....",
            "app": "....",
            # ....
        })
        # ...
        return super(GameServerDetail, self).__init__(**kwargs)