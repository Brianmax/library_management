from .models import Book, Author
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BookListViewGen(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListViewCus(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs["id"])


class BookCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_id = self.kwargs["id"]
        author = Author.objects.get(id=author_id)
        serializer.save(author=author)
