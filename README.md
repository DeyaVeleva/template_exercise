# Bookstore Project

A simple Django web app built to manage books and user reviews. It uses Bootstrap for a responsive frontend and showcases standard Django template logic like custom filters, inheritance, and dynamic data binding.

## Core Features
* **Dynamic Content:** All content is pulled straight from the SQLite database.
* **Smart Layouts:** Built with a global base template (`base.html`) and reusable review card includes.
* **Custom Filters & Tags:** Features a custom filter to turn numeric ratings into visual stars (`★`) and a template tag that displays the 3 latest books on the home page.
* **Text & Data Formatting:** Title casing, word truncating, conditional pricing logic, and clean date presentation are handled directly in the templates.

## App Structure
* `books/` — Handles book cataloging, metadata, and detail pages.
* `reviews/` — Manages reader ratings, feedback text, and the custom template tags folder.
* `templates/` — Houses the master layout skeleton.

## Quick Start

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run database migrations:
```bash
python manage.py migrate
```

3. Start the local development server:
```bash
python manage.py runserver
```
Once started, view the project at `http://127.0.0`.
