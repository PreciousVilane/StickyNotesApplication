from django.db import models

# Create your models here.
''' Model representing sticky note '''


class Note(models.Model):
    title = models.CharField(max_length=100)  # short text field for note title
    content = models.TextField()  # large text field for the actual note
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # links each note to a user via foreignkey
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    ''' Model Representing the author of the note'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name