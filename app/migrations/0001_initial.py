# Generated by Django 4.0.3 on 2022-04-11 23:13

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('url', models.URLField(blank=True)),
                ('location', models.CharField(default='Nairobi', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('usability_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('content_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('avg_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
                ('contact', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
