📝 Flask Todo App

A small Todo application built with Flask to practice backend fundamentals, CRUD operations, routing, and rendering templates using Jinja2. The app provides a Home page for listing and creating tasks, and a separate Update page for editing existing tasks. Data is persisted locally using SQLite via SQLAlchemy ORM.

The application includes:

Home page: view task list + create tasks

Update page dedicated to editing tasks

Storage using SQLite via SQLAlchemy

🚀 UI Demo
🏠 Home page
<img width="2551" height="1340" alt="Screenshot 2026-01-19 210227" src="https://github.com/user-attachments/assets/a1175810-b9c6-4126-a065-d9e677b50baa" />
✏️ Update page
<img width="2557" height="1345" alt="Screenshot 2026-01-19 210255" src="https://github.com/user-attachments/assets/cf277c8e-c719-4868-9272-8772def4dd47" />
✨ Features

✔ Create tasks

✔ List all tasks

✔ Delete tasks

✔ Edit tasks on a dedicated update page

✔ Persist data with SQLite

✔ Rendered using Jinja2 templates

🧱 Tech Stack
Component	Technology
Backend	Flask
Database	SQLite + SQLAlchemy
Template	Jinja2
Auth	(optional) JWT support
UI	HTML + SCSS basic
📦 Installation & Run
1️⃣ Clone repo
git clone https://github.com/yourname/flask-todo-app.git
cd flask-todo-app

2️⃣ Setup Environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3️⃣ Run the App
flask run


App will run at:

👉 http://127.0.0.1:5000/

📁 Project Structure
.
├── app.py
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
│   └── styles.css
├── screenshots/
└── requirements.txt
