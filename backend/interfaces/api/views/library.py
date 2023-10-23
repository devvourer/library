from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from apps.library.models import Book, Comment
from interfaces.api.serializers.library import (
    BookListSerializer,
    BookDetailSerializer,
    CommentSerializer,
    FavoriteSerializer
)


class LibraryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'created_at': ['gt', 'lt'],
        'author': ['exact'],
        'category': ['exact'],
    }

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = BookDetailSerializer
            return self.serializer_class
        return super().get_serializer_class()

    @action(methods=['post'], detail=False, serializer_class=FavoriteSerializer)
    def add_book_to_favorite(self, request):
        serializer = FavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'book added to favorites'}, status=status.HTTP_201_CREATED)


class CommentViewSet(CreateModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


