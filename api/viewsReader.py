from .serializers import ReaderSerializer
from .models import Reader
from rest_framework.generics import ListAPIView, CreateAPIView


class ReaderListView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderCreateView(CreateAPIView):
    serializer_class = ReaderSerializer
