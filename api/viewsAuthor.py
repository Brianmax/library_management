from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Author
from .serializers import AuthorSerializer, RentalSerializer, BookSerializer
# Create your views here.


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        author = Author.objects.get(id=self.kwargs["id"])
        return author


class AuthorCreateView(CreateAPIView):
    serializer_class = AuthorSerializer
