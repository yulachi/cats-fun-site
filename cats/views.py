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
    print("Method: %r\n%r", request.method, request.POST)
    if request.method == "POST":
        form = PersonForm(request.POST)
        print("GOT FORM")
        print(form, form.is_valid(), form.data)
        if form.is_valid():
            print("FORM IS VALID")
            person = form.save()
            return HttpResponseRedirect(reverse("cats:person", args=(person.id,)))
        else:
            print(form.errors)
    else:
        form = PersonForm()

    return render(request, "cats/guests.html", {"form": form})


class PersonView(generic.DetailView):
    model = Person
    template_name = "cats/person.html"
