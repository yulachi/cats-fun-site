from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import TaskForm
from .models import TaskResult
from .utils.solver import solve_task
from .utils.stats import get_stats


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
    context_object_name = "task_result"


class ResultListView(generic.ListView):
    model = TaskResult
    template_name = "algo/history.html"
    context_object_name = "results"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**get_stats())
        return context
