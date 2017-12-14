#encoding:utf8
#17-10-30 下午8:46
#Add
from django.conf.urls import url
from backends import views

urlpatterns = [
    url(r"^author/add/$", views.AuthorCreateView.as_view(), name="author_create_view"),
    url(r"^book/add/$", views.BookCreateView.as_view(), name="book_create_view"),
    # url(r"^author/add/$", views.AuthorCreateView.as_view(), name="author_create_view"),

]