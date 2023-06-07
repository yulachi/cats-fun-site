from django.db import models


class Visitor(models.Model):
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
        ("A", "Another"),
    )

    BREEDS = (
        ("SI", "Siamese"),
        ("PE", "Persian"),
        ("MC", "Maine Coon"),
        ("RA", "Ragdoll"),
        ("BE", "Bengal"),
        ("AB", "Abyssinian"),
        ("BI", "Birman"),
        ("OS", "Oriental Shorthair"),
        ("SX", "Sphynx"),
        ("DR", "Devon Rex"),
        ("HI", "Himalayan"),
        ("AS", "American Shorthair"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveSmallIntegerField()

    cat_name = models.CharField(max_length=30)
    cat_age = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=2, choices=BREEDS)

    # for checking constraints in db
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__lte=120),
                name="age_lte_120",
                violation_error_message="Age should be less or equal to 120",
            ),
            models.CheckConstraint(
                check=models.Q(cat_age__lte=40),
                name="cat_age_lte_40",
                violation_error_message="Cat age should be less or equal to 40",
            ),
        ]

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.gender}, {self.age}"
