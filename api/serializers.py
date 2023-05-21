from rest_framework import serializers
from .models import Author, Book, Reader, Rental


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ("__all__",)


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"
        read_only_fields = ("__all__",)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
            required=False,
            queryset=Author.objects.all(),
            )

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("__all__",)


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"
        read_only_fields = ("__all__",)
