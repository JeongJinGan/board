# Generated by Django 3.2.13 on 2022-11-07 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('map_url', models.TextField(default='')),
                ('telephone', models.TextField()),
                ('opening', models.TextField()),
                ('picture1', imagekit.models.fields.ProcessedImageField(blank=True, max_length=1000, upload_to='images/')),
                ('picture2', imagekit.models.fields.ProcessedImageField(blank=True, max_length=1000, upload_to='images/')),
                ('picture3', imagekit.models.fields.ProcessedImageField(blank=True, max_length=1000, upload_to='images/')),
                ('score', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('taste', models.IntegerField(default=0)),
                ('interior', models.IntegerField(default=0)),
                ('dessert', models.IntegerField(default=0)),
                ('emotion', models.IntegerField(default=0)),
                ('hip', models.IntegerField(default=0)),
                ('study', models.IntegerField(default=0)),
                ('love', models.IntegerField(default=0)),
                ('sight', models.IntegerField(default=0)),
                ('bookmarks', models.ManyToManyField(related_name='bookmarksuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('picture2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('picture3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('tag', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '커피맛'), (2, '인테리어'), (3, '디저트'), (4, '감성'), (5, '힙한'), (6, '집중'), (7, '데이트'), (8, '뷰')], max_length=15)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.cafe')),
                ('like', models.ManyToManyField(related_name='likeuser', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]