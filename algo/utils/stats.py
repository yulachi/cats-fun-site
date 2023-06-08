from typing import Dict

from django.db.models import Avg, Max
from django.db.models.query import QuerySet


def format_stat(stat: float) -> str:
    return f"{stat:.1f}"


def format_stat_percent(stat: float) -> str:
    return f"{stat * 100:.0f}%"


def get_stats(objects: QuerySet) -> Dict[str, str]:
    return {
        "mean_cube_edge": format_stat(objects.aggregate(Avg("task__a"))["task__a__avg"]),
        "max_cylinder_height": format_stat(objects.aggregate(Max("task__h"))["task__h__max"]),
        "mean_cube_fit": format_stat_percent(
            objects.aggregate(Avg("fit_in_cube"))["fit_in_cube__avg"],
        ),
        "mean_cylinder_fit": format_stat_percent(
            objects.aggregate(Avg("fit_in_cylinder"))["fit_in_cylinder__avg"],
        ),
    }
