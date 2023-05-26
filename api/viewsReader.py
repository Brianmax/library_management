from .serializers import ReaderSerializer
from .models import Reader
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ReaderListView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReaderSerializer
