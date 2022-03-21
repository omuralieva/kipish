# Generated by Django 4.0.3 on 2022-03-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kipish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('whatsapp', models.IntegerField(verbose_name='WhatsApp')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Социальная сеть')),
                ('link', models.URLField(verbose_name='Адрес социальной сети')),
                ('icon', models.FileField(upload_to='img/icon/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='videopost',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='place',
            name='average_check',
            field=models.PositiveIntegerField(verbose_name='Средний чек'),
        ),
    ]