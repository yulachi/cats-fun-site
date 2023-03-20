from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import PersonForm
from .models import Person


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
    person_form = PersonForm(post_data)
    if person_form.is_valid():
        person = person_form.save()
        return HttpResponseRedirect(reverse("cats:person", args=(person.id,)))

    return render(request, "cats/guests.html", {"form": person_form})


class PersonView(generic.DetailView):
    model = Person
    template_name = "cats/person.html"
