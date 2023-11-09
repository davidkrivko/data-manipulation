from rest_framework import serializers

from users.models import UserModel, CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class UserModelDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = UserModel
        fields = "__all__"
