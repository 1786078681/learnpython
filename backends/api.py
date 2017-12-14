#encoding:utf8
#17-10-30 下午8:19
#Add

from rest_framework import viewsets, serializers
from backends.models import Test, Author, Book

class BookListSerializers(serializers.ModelSerializer):
    # authors = serializers.HyperlinkedRelatedField(view_name="author_create_view", many=True)
    # author  = serializers.StringRelatedField(many=True)
    author  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # author = serializers.HyperlinkedRelatedField(
    #     view_name="api:author_list",
    #     many=True,
    #     read_only=True,
    # )
    class Meta:
        model = Book
        fields = ("id", "name", "author")
        depth = 2



class BookListViewsets(viewsets.ModelViewSet):
    serializer_class = BookListSerializers
    queryset = Book.objects.all()

class AuthorListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name")
class AuthorLlistViewsets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializers



class TestListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ("id", "name", "createTime", "updateTime", "msg")


class TestListViewsets(viewsets.ModelViewSet):
    serializer_class = TestListSerializers
    queryset = Test.objects.all()