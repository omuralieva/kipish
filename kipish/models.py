from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Place(models.Model):
    title = models.CharField(verbose_name='Заведение', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(upload_to='image/', verbose_name='Главное изображение', null=True, blank=True)
    average_check = models.CharField(verbose_name='Средний чек', max_length=10)
    working_time = models.CharField(verbose_name='Рабочие часы', max_length=15)
    contact = models.CharField(verbose_name='Контакты', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    top = models.BooleanField(verbose_name='Топ заведение', default=False)

    def get_absolute_url(self):
        return reverse('place-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ImagePost(models.Model):
    class Meta:
        ordering = ['-created_at']

    title = models.CharField(verbose_name='Событие или день недели', max_length=100)
    place = models.ForeignKey(to=Place, on_delete=models.SET_NULL, null=True, verbose_name='Заведение', blank=True)
    image = models.ImageField(upload_to='image/', verbose_name='Главное изображение', null=True)
    created_at = models.DateTimeField(verbose_name='Дата события')
    photographer = models.CharField(verbose_name='Имя фотографа', max_length=100)
    slug = models.SlugField(max_length=300, unique=True)
    top = models.BooleanField(verbose_name='Актуальный фотоотчет', default=False)

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'slug': self.slug})


class ImageItem(models.Model):
    image = models.ImageField(upload_to='image/', verbose_name='Фотографии', null=True)
    image_posts = models.ForeignKey(to=ImagePost, related_name='Image', on_delete=models.CASCADE)


class VideoPost(models.Model):
    class Meta:
        ordering = ['-created_at']

    title = models.CharField(verbose_name='Событие или день недели', max_length=100)
    place = models.ForeignKey(to=Place, on_delete=models.SET_NULL, null=True, verbose_name='Заведение', blank=True)
    url = EmbedVideoField(verbose_name='Ссылка на видео')
    created_at = models.DateTimeField(verbose_name='Дата события')
    slug = models.SlugField(max_length=300, default=True)
    top = models.BooleanField(verbose_name='Актуальный видеоотчет', default=False)

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, default='')
    body = models.CharField(verbose_name='Номер телефона или email', max_length=150, default='')
    link = models.CharField(verbose_name='Ссылка', max_length=100)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(verbose_name='Социальная сеть', max_length=100)
    link = models.URLField(verbose_name='Ссылка на социальную сеть')
    icon = models.FileField(upload_to='img/icon/')

    def __str__(self):
        return self.name
