# Generated by Django 4.0.6 on 2022-08-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.director'),
        ),
    ]