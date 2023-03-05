# Generated by Django 4.1.5 on 2023-01-29 08:39

import ckeditor.fields
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
            name="EnrollmentApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("phone_no", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("module", models.CharField(max_length=255)),
                (
                    "starting_date",
                    models.CharField(
                        choices=[("1", "2ND Feb"), ("2", "8th Aug"), ("3", "9th Nov")],
                        default="1",
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TechsyiqTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("social_media_link", models.URLField(blank=True)),
                ("description", models.TextField()),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        default=None, max_length=255, verbose_name="images"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "Author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", ckeditor.fields.RichTextField()),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        default=None, max_length=255, verbose_name="images"
                    ),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date_published"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blogs_app.category",
                    ),
                ),
            ],
        ),
    ]