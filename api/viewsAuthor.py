from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Author
from .serializers import AuthorSerializer, RentalSerializer, BookSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class AuthorListView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        author = Author.objects.get(id=self.kwargs["id"])
        return author


class AuthorCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorSerializer
