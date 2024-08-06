from rest_framework import serializers
from .models import Post, Comment, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    image = serializers.ImageField(required=False)  # Incluir el campo de imagen en el serializador

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'image']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at']
