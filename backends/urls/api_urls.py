#encoding:utf8
#17-10-30 下午8:16
#Add
from django.conf.urls import url,include

from rest_framework import routers
from backends import api



router = routers.DefaultRouter()
router.register("test/list", api.TestListViewsets, base_name="test_list")
router.register("books", api.BookListViewsets, "book_list")
router.register("authors", api.AuthorLlistViewsets, "author_list")


urlpatterns = []

urlpatterns += router.urls