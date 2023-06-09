"""Модуль, содержащий сериализаторы для приложения api."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()

SELF_FOLLOW_ERROR = 'Нельзя подписаться на самого себя'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Определяет модель и поля для сериализации модели Comment."""

        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        """Определяет модель и поля для сериализации модели Group."""

        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Определяет модель и поля для сериализации модели Post."""

        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
        allow_null=True
    )

    class Meta:
        """Определяет модель и поля для сериализации модели Follow."""

        fields = ('user', 'following')
        model = Follow

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'],
            message='Вы уже подписаны на этого автора'
        )
    ]

    def validate_following(self, value):
        """Проверяет, что это не текущий пользователь."""
        if value == self.context['request'].user:
            raise ValidationError(SELF_FOLLOW_ERROR)
        return value
