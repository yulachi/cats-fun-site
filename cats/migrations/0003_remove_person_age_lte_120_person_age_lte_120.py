# Generated by Django 4.1.7 on 2023-03-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cats", "0002_person_age_lte_120"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="person",
            name="age_lte_120",
        ),
        migrations.AddConstraint(
            model_name="person",
            constraint=models.CheckConstraint(
                check=models.Q(("age__lte", 120)),
                name="age_lte_120",
                violation_error_message="Age should be less or equal to 120",
            ),
        ),
    ]
