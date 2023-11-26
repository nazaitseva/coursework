from rest_framework import serializers

from .models import Comment
from .models import Product

class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'content', 'created_at')



class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')