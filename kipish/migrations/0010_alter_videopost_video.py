# Generated by Django 4.0.3 on 2022-03-17 10:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kipish', '0009_videopost_top_videopost_video_alter_contact_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='video',
            field=embed_video.fields.EmbedVideoField(verbose_name='Ссылка на видео'),
        ),
    ]
