# Generated by Django 5.0.6 on 2024-07-18 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ratings", "0004_alter_rating_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rating",
            options={"ordering": ["-timestamp"]},
        ),
    ]