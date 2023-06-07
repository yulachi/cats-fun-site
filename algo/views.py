from django.db.models import Avg, Count, Max, Min, StdDev, Sum
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import TaskForm
from .models import AlgoTask


def index(request: HttpRequest):
    return render(request, "algo/index.html")


def task(request: HttpRequest):
    post_data = request.POST or None
    task_form = TaskForm(post_data)
    if task_form.is_valid():
        task = task_form.save()
        return HttpResponseRedirect(reverse("algo:task_result", args=(task.id,)))

    return render(request, "algo/task.html", {"form": task_form})


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


class TaskResultView(generic.DetailView):
    model = AlgoTask
    template_name = "algo/task_result.html"
