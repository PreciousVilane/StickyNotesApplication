from django.test import TestCase
from django.urls import reverse
from .models import Note, Author

# Create your tests here.


class NoteModelTest(TestCase):
    def setUp(self):
        # creating data that all test can use. Author object & Note objects for testing
        author = Author.objects.create(name='Test Author')
        Note.objects.create(title='Test Note', content='This is a test note', author=author)

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertHTMLEqual(note.content, 'This is a test note')

# Testing views


class NoteViewTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name='Test Author')
        Note.objects.create(title='Test Note', content='This is a test note', author=author)

    def test_note_list(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail(self):
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note')