# 📝 Flask Todo App

A small Todo application built with Flask to practice backend fundamentals: CRUD operations, routing, and rendering templates with Jinja2. The app provides a Home page to list and create tasks and a dedicated Update page to edit tasks.

## ✨ Features
- Create tasks
- List all tasks
- Delete tasks
- Edit tasks on a dedicated update page
- Persist data with SQLite (SQLAlchemy)
- Rendered using Jinja2 templates

## 🚀 UI Demo

Home page  
<img width="1200" alt="Home page" src="https://github.com/user-attachments/assets/a1175810-b9c6-4126-a065-d9e677b50baa" />

Update page  
<img width="1200" alt="Update page" src="https://github.com/user-attachments/assets/cf277c8e-c719-4868-9272-8772def4dd47" />

## 🧱 Tech Stack

| Component | Technology |
|---|---|
| Backend | Flask |
| Database | SQLite + SQLAlchemy |
| Template | Jinja2 |
| Auth | (optional) JWT |
| UI | HTML + SCSS (basic) |

## 📦 Installation & Run

1) Clone the repo

    git clone https://github.com/Duc-dev-starter/flask-todo-app.git
    cd flask-todo-app

2) Set up environment

- Create a virtual environment:

    python -m venv venv

- Activate (Windows):

    venv\Scripts\activate

- Activate (macOS / Linux):

    source venv/bin/activate

- Install dependencies:

    pip install -r requirements.txt

3) Run the app

    flask run

The app will run at: http://127.0.0.1:5000/

