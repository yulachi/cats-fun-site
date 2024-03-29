# Generated by Django 4.1.7 on 2023-06-07 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("algo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskResult",
            fields=[
                (
                    "task",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="algo.algotask",
                    ),
                ),
                ("fit_in_cube", models.BooleanField()),
                ("fit_in_cylinder", models.BooleanField()),
            ],
        ),
    ]
