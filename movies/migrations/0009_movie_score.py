# Generated by Django 5.0.6 on 2024-07-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0008_alter_movie_poster"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="score",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
