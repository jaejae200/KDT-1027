# Generated by Django 3.2.13 on 2022-10-27 06:01

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('like_users', models.ManyToManyField(related_name='like_articles', to='accounts.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
