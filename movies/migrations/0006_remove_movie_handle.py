# Generated by Django 5.0.6 on 2024-07-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_alter_movie_handle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="handle",
        ),
    ]
