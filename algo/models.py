from django.db import models


class AlgoTask(models.Model):
    # cube edge
    a = models.FloatField()

    # cylinder height and base radius
    h = models.FloatField()
    r = models.FloatField()

    # given liquid volume
    m = models.FloatField()

    timestamp = models.DateTimeField(auto_now=True)

    # for checking constraints in db
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(a__gte=0),
                name="a_gte_0",
                violation_error_message="Cube edge should be greater or equal than zero",
            ),
            models.CheckConstraint(
                check=models.Q(h__gte=0),
                name="h_gte_0",
                violation_error_message="Cylinder height should be greater or equal than zero",
            ),
            models.CheckConstraint(
                check=models.Q(r__gte=0),
                name="r_gte_0",
                violation_error_message="Cylinder radius should be greater or equal than zero",
            ),
            models.CheckConstraint(
                check=models.Q(m__gte=0),
                name="m_gte_0",
                violation_error_message="Liquid volume should be greater or equal than zero",
            ),
        ]

    def __str__(self):
        return (
            f"cube edge = {self.a}, "
            f"cylinder height = {self.h}, "
            f"radius = {self.r}, "
            f"volume = {self.m}, "
            f"date = {self.timestamp}"
        )
