from .models import Book, Author
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


class BookListViewGen(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListViewCus(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs["id"])


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_id = self.kwargs["id"]
        author = Author.objects.get(id=author_id)
        serializer.save(author=author)
