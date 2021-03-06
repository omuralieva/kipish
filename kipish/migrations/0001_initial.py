# Generated by Django 4.0.3 on 2022-03-11 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заведение')),
                ('description', models.TextField(max_length=400, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Главное изображение')),
                ('average_check', models.IntegerField(verbose_name='Средний чек')),
                ('working_time', models.DateField(verbose_name='Рабочие часы')),
                ('contact', models.IntegerField(verbose_name='Контакты')),
                ('address', models.TextField(verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Событие или день недели')),
                ('created_at', models.DateTimeField(verbose_name='Дата события')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kipish.place', verbose_name='Заведение')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Событие или день недели')),
                ('image', models.ImageField(null=True, upload_to='image/', verbose_name='Главное изображение')),
                ('created_at', models.DateTimeField(verbose_name='Дата события')),
                ('photographer', models.CharField(max_length=100, verbose_name='Имя фотографа')),
                ('places', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kipish.place', verbose_name='Заведение')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ImageItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/', verbose_name='Фотографии')),
                ('image_posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kipish.imagepost')),
            ],
        ),
    ]
