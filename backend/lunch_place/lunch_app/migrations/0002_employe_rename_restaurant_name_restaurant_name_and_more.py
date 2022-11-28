# Generated by Django 4.0.8 on 2022-11-24 06:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("lunch_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employe",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=100, unique=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameField(
            model_name="restaurant",
            old_name="restaurant_name",
            new_name="name",
        ),
        migrations.AddField(
            model_name="restaurant",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last Modified At"),
        ),
    ]
