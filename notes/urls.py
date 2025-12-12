# notes/urls.py
from django.urls import path
from .views import (
    note_list,
    note_detail,
    create_note,
    update_note,
    delete_note,
    )

urlpatterns = [
    path("", note_list, name="note_list"),
    # # <int:pk> it convert int to pk
    path("note/<int:pk>/", note_detail, name="note_detail"),
    path("note/new/", create_note, name="create_note"),
    path("note/<int:pk>/edit/", update_note, name="update_note"),
    path("note/<int:pk>/delete/", delete_note, name="delete_note"),
]