# Generated by Django 5.2.1 on 2025-06-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0006_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="video",
            field=models.FileField(
                blank=True, null=True, upload_to="movies/movie_files"
            ),
        ),
    ]
