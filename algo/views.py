from django.db.models import Avg, Count, Max, Min, StdDev, Sum
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import TaskForm
from .models import AlgoTask, TaskResult
from .solver import solve_task


def index(request: HttpRequest):
    return render(request, "algo/index.html")


def task(request: HttpRequest):
    post_data = request.POST or None
    task_form = TaskForm(post_data)
    if task_form.is_valid():
        task = task_form.save()

        # solving task and saving results
        task_conditions = model_to_dict(task)
        task_conditions.pop("id")
        fit_in_cube, fit_in_cylinder = solve_task(**task_conditions)
        result = TaskResult(task=task, fit_in_cube=fit_in_cube, fit_in_cylinder=fit_in_cylinder)
        result.save()

        return HttpResponseRedirect(reverse("algo:task_result", args=(result.pk,)))

    return render(request, "algo/task.html", {"form": task_form})


class ResultView(generic.DetailView):
    model = TaskResult
    template_name = "algo/task_result.html"


def history(request: HttpRequest):
    # objects_list
    objects_values = AlgoTask.objects.values()

    # values_list
    objects_values_list = AlgoTask.objects.values_list()

    cur_objects = AlgoTask.objects.all()
    statistics_val = [
        cur_objects.aggregate(Count("a")),
        cur_objects.aggregate(Avg("a")),
        cur_objects.aggregate(Min("a")),
        cur_objects.aggregate(Max("a")),
        cur_objects.aggregate(StdDev("a")),
        cur_objects.aggregate(Sum("a")),
    ]

    statistics = {"statics_val": statistics_val}

    # fields_name
    fields = AlgoTask._meta.get_fields()

    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)

    field_names = verbose_name_list
    context = {
        "objects_values": objects_values,
        "objects_values_list": objects_values_list,
        "statistics": statistics,
        "field_names": field_names,
    }
    return render(request, "table.html", context)
