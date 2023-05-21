from .viewsAuthor import AuthorListView, AuthorCreateView, AuthorView
from .viewsBook import BookCreateView, BookListViewGen, BookListViewCus
from .viewsReader import ReaderListView, ReaderCreateView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
        path("author/list/",
             AuthorListView.as_view(),
             name="listaAuthors"),

        path("author/<int:id>/",
             AuthorView.as_view(),
             name="specificAuthor"),

        path("author/create/",
             AuthorCreateView.as_view(),
             name="CreateAuthor"),

        path("author/<int:id>/createBook/",
             BookCreateView.as_view(),
             name="createBook"),

        path("book/list/",
             BookListViewGen.as_view(),
             name="genBookList"),

        path("author/<int:id>/book/list/",
             BookListViewCus.as_view(),
             name="customListBook"),

        path("reader/list/",
             ReaderListView.as_view(),
             name="readerList"),

        path("reader/create/",
             ReaderCreateView.as_view(),
             name="createReader")
        ]
