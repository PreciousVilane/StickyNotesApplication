from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# geting all notes


def note_list(request):
    notes = Note.objects.all()

    # notes in dictionary form
    context = {
        "notes": notes,
        "page_title": "note_list",
    }

    return render(request, "notes/note_list.html", context)

# getting specific note


def note_detail(request, pk):
    note = get_object_or_404(Note, id=pk)

    # returning the note requested
    return render(request, "notes/note_detail.html", {"note": note})


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)  # requesting the form from note form
        if form.is_valid():
            note = form.save(commit=False)
            note.author = None
            note.save()
            return redirect("note_list")  # redirecting to show saved note

    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def update_note(request, pk):
    # view to update existing note
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")

    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def delete_note(request, pk):
    # view to update existing note

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")

