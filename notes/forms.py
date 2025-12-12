# notes/forms.py
from django import forms
from .models import Note


# Creating a form for the creation and updating of the notes

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ["title", "content"]
