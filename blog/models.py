from django.db import models


class PostTag(models.Model):
    """Теги постов."""

    name = models.CharField('Название тега', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    """Пост в блоге."""

    tags = models.ManyToManyField(PostTag, blank=True, related_name='Теги')
    is_news = models.BooleanField('Является новостью?', default=False,
                                  help_text='Новости будут отображаться на соответствующей странице новостей')
    title = models.CharField('Заголовок статьи', max_length=200)
    title_image = models.ImageField('Изображение для новости', upload_to='posts/images')
    body = models.TextField('Текст новости')
    description = models.TextField('Превью статьи', max_length=200, default='')
    created = models.DateTimeField('Время создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class ForeignPost(models.Model):
    parent = models.ForeignKey('Post', models.CASCADE, related_name='foreign_posts')
    foreign = models.ForeignKey('Post', models.CASCADE, related_name='parent_posts')
