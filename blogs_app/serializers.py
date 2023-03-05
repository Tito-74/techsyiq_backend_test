from .models import Blog, Category
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['name','Author']


class BlogSerializers(serializers.ModelSerializer):
  # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False)
  category_name = serializers.CharField(source="category.name", read_only=True)
  class Meta:
    model = Blog
    fields = "__all__"

