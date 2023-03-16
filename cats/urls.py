from django.urls import path

from . import views

app_name = "cats"
urlpatterns = [
    # ex: /cats/
    path("", views.index, name="index"),
    # ex: /cats/memes/
    path("memes/", views.memes, name="memes"),
    # ex: /cats/perse/
    path("perse/", views.perse, name="perse"),
    # ex: /cats/scotland/
    path("scotland/", views.scotland, name="scotland"),
    # ex: /cats/wild/
    path("wild/", views.wild, name="wild"),
    # ex: /cats/guests/
    path("guests/", views.guests, name="guests"),
    # ex: /cats/person/5/
    path("person/<int:pk>/", views.PersonView.as_view(), name="person"),
]
