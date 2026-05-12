# Sticky Notes App

## Project Overview

The Sticky Notes App is a full-stack web application built with Django that allows users to create, update, manage, and organize digital notes in a simple and efficient way.

This project demonstrates core backend development concepts including:

* CRUD functionality (Create, Read, Update, Delete)
* Django Models & ORM
* Form handling
* URL routing
* Template rendering
* Database relationships
* Unit testing with Django Test Framework

The application simulates a lightweight productivity tool similar to digital sticky note applications used for task management, reminders, and note-taking.

## It is ideal for:

Beginner to intermediate Django developers
Portfolio projects
Learning Django CRUD operations
Understanding MVC/MVT architecture
Practicing backend testing

## Features
1. Note Management
- Create new sticky notes
- View all saved notes
- Open individual notes
- Edit/update existing notes
- Delete notes instantly

2. Author System
- Assign notes to authors
- One author can own multiple notes
- Database relationship using ForeignKey

3. Automatic Timestamps
- Each note automatically stores:
- Creation date & time
- Last updated date & time
- Using Django’s:
- auto_now_add=True
- auto_now=True
  
4. Form Handling
- Django ModelForms implementation
- Form validation
- User-friendly note creation/editing workflow

5. Automated Testing

The project includes Django unit tests for:

- Models
- Views
- HTTP response validation
- Content rendering checks
  
## Tech Stack
1. Backend
2. Python
3. Django
4. Database
5. SQLite (default Django database)
6. Frontend
7. HTML
8. Django Templates
9. SS
10. Testing
11. Django Test Framework
    
## Application Views

* View	Description
* note_list	Displays all notes
* note_detail	Displays a single note
* create_note	Creates a new note
* update_note	Updates an existing note
* delete_note	Deletes a note
  
## Running Tests

The project currently tests:

- Note model creation
- Note content validation
- Note list page
- Note detail page
  
## Key Learnings

This project demonstrates:

* Django CRUD operations
* Django ORM relationships
* ModelForm implementation
* Dynamic template rendering
* URL routing & views
* Database migrations
* Unit testing in Django
* Backend architecture fundamentals
* Clean project structure organization
  
## License

This project is open-source and available under the MIT License.

## Author

Built as a Django portfolio project to demonstrate backend web development skills, CRUD functionality, database relationships, testing, and full-stack application architecture using Python and Django.
