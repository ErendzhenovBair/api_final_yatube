"""Модуль, содержащий модели для приложения posts."""

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    """Модель группы для постов."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Возвращает строковое представление объекта Group."""
        return self.title


class Post(models.Model):
    """Модель поста."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name="Группа"
    )
    image = models.ImageField(
        upload_to='posts/images/', null=True, blank=True)

    def __str__(self):
        """Возвращает строковое представление объекта Post."""
        return (
            f"Post '{self.text[:20]}' by {self.author.username} "
            f"({self.pub_date})"
        )


class Comment(models.Model):
    """Модель комментария."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Модель подписки на авторов постов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор постов'
    )

    class Meta:
        """Класс для определения метаданных модели."""

        verbose_name_plural = 'Подписки'
        verbose_name = 'Подписка'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_pair_follower_following'
            )
        ]

    def __str__(self):
        """Возвращает строковое представление объекта Follow."""
        return f'{self.user} подписался на {self.following}'
