# Generated by Django 3.2.13 on 2022-11-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=100)),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('video', models.BooleanField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre_ids', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
            ],
        ),
    ]
