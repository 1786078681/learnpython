from django.shortcuts import render

# Create your views here.
# from django.views.generic import TemplateView,CreateView, UpdateView
# from backends.forms import TestModelForm, Test, Author, Book,\
#     AuthorForm, BookForm
# from django.urls import reverse, reverse_lazy
#
#
# class AuthorCreateView(CreateView):
#     form_class = AuthorForm
#     template_name = "index.html"
#     success_url = reverse_lazy("books:author_create_view")
#
# class BookCreateView(CreateView):
#     form_class = BookForm
#     template_name = "index.html"
#     success_url = reverse_lazy("books:book_create_view")
#
#
# class TestCreateView(CreateView):
#     form_class = TestModelForm
#     template_name = "index.html"
#     success_url = reverse_lazy("test_create_view")
#
#     def get_context_data(self, **kwargs):
#         kwargs.update({
#             "title": "create view test",
#         })
#         return super(TestCreateView, self).get_context_data(**kwargs)
#
#
# class TestUpdateView(UpdateView):
#     model = Test
#     form_class = TestModelForm
#     template_name = "index.html"
#     success_url = reverse_lazy("test_create_view")
#
# class TestListView(TemplateView):
#     template_name = "list.html"
#
#     def get_context_data(self, **kwargs):
#         kwargs.update({
#             "title": "Test list",
#         })
#         return super(TestListView, self).get_context_data(**kwargs)


from backends import forms, models
from django.shortcuts import render, HttpResponse

def test(request):
    obj = ""
    if request.method == "GET":
        obj = forms.AuthorForm()
    else:
        obj = forms.AuthorForm(data=request.POST)
        if obj.is_valid():
            data = obj.clean()
            print(data)
            models.Author.objects.create(**data)



    return render(request, "test.html", {"obj": obj})



















































