# Generated by Django 5.0.6 on 2024-07-19 09:42

import django_extensions.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movie_rating_avg_movie_rating_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="handle",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from=["title", "release_date"]
            ),
        ),
    ]
