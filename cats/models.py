from django.db import models


class Person(models.Model):
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
        ("A", "Another"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__lte=120),
                name="age_lte_120",
                violation_error_message="Age should be less or equal to 120",
            ),
        ]

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.gender}, {self.age}"
