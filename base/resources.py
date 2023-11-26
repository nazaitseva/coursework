from import_export import resources

from .models import Comment
from .models import Product

class CommentsResource(resources.ModelResource):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'content', 'created_at')

class ProductsResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')