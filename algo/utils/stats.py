from typing import Dict

from django.db.models import Avg, Max

from algo.models import AlgoTask, TaskResult


def format_stat(stat: float) -> str:
    return f"{stat:.1f}"


def format_stat_percent(stat: float) -> str:
    return f"{stat * 100:.0f}%"


def get_stats() -> Dict[str, str]:
    results = TaskResult.objects.all()
    tasks = AlgoTask.objects.all()

    return {
        "mean_cube_edge": format_stat(tasks.aggregate(Avg("a"))["a__avg"]),
        "max_cylinder_height": format_stat(tasks.aggregate(Max("h"))["h__max"]),
        "mean_cube_fit": format_stat_percent(
            results.aggregate(Avg("fit_in_cube"))["fit_in_cube__avg"],
        ),
        "mean_cylinder_fit": format_stat_percent(
            results.aggregate(Avg("fit_in_cylinder"))["fit_in_cylinder__avg"],
        ),
    }
