from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField, HyperlinkedIdentityField

from apps.library.models import Book, Comment, Favorite


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    book = SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author(self, obj):
        return obj.author.username

    def get_book(self, obj):
        return obj.book.name


class BookSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = SerializerMethodField()
    rating = SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('name', 'author', 'category')

    def get_author(self, obj):
        return [obj.author.id, obj.author.user.username]

    def get_category(self, obj):
        return [obj.category.id, obj.category.name]

    def get_rating(self, obj):
        return obj.rating


class BookListSerializer(BookSerializer):
    detail = HyperlinkedIdentityField(view_name='book-detail', read_only=True)
    favorite = SerializerMethodField()

    def get_favorite(self, obj):
        user = self.context.get('request').user
        if user.favorites.filter(book=obj):
            return True
        return False


class BookDetailSerializer(BookSerializer):
    comments = CommentDetailSerializer(many=True, read_only=True)


class FavoriteSerializer(ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('book', 'user')
