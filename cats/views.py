from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import VisitorForm
from .models import Visitor


def index(request: HttpRequest):
    return render(request, "cats/index.html")


def memes(request: HttpRequest):
    return render(request, "cats/memes.html")


def perse(request: HttpRequest):
    return render(request, "cats/perse.html")


def scotland(request: HttpRequest):
    return render(request, "cats/scotland.html")


def wild(request: HttpRequest):
    return render(request, "cats/wild.html")


def guests(request: HttpRequest):
    post_data = request.POST or None
    visitor_form = VisitorForm(post_data)
    if visitor_form.is_valid():
        visitor = visitor_form.save()
        return HttpResponseRedirect(reverse("cats:visitor", args=(visitor.id,)))

    return render(request, "cats/guests.html", {"form": visitor_form})


class VisitorView(generic.DetailView):
    model = Visitor
    template_name = "cats/visitor.html"
