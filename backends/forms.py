#encoding:utf8
#17-10-30 下午5:42
#Add
from backends.models import Test, Author, Book
# from django.forms import ModelForm
from django import forms
# class AuthorForm(forms.Form):
#     name = forms.CharField()
#     age = forms.CharField()
#
#     def clean_age(self):
#         age = self.cleaned_data.get("age")
#         if age.isdigit():
#             self.add_error("age","age must Integer %s" % age )
#
#         return age


# class TestModelForm(ModelForm):
#
#     class Meta:
#         model = Test
#         fields = ("name", "msg")
#
#
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ("name", "author")



# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ("name", "age")


class GameServerInfoForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"
        help_texts = {
            "name": "input your name",
            # ...
        }
        widgets = {
            "author": forms.TextInput(
                attrs={"value": "", "class": "form-control form-data", "placeholder": "input a integer"}),
            "name": forms.TextInput(
                attrs={"max-length": 25})
        }

