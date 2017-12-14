#encoding:utf8
#17-10-30 下午5:42
#Add
from backends.models import Test, Author, Book
from django import forms
from django.forms import forms as dforms

class AuthorForm(forms.Form):
    name = forms.CharField()
    age = forms.CharField()

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age.isdigit():
            self.add_error("age","age must Integer %s" % age )

        return age


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

