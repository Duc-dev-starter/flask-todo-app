from flask import Flask, request, jsonify, render_template, redirect
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss 
from datetime import datetime, timedelta

app = Flask(__name__)
Scss(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"] = "super-secret-key" 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

jwt = JWTManager(app)

# Data class ~ row of data
class MyTask(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task ${self.id}"
    
with app.app_context():
    db.create_all()

# Home page
@app.route("/", methods=["POST", "GET"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    # See all current task
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
    return render_template("index.html", tasks=tasks)

# Delete an item
@app.route("/delete/<int:id>")
def delete(id: int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"

# Edit
@app.route("/edit/<int:id>", methods = ["GET", "POST"])
def edit(id: int):
    task = MyTask.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error:{e}"
    else:
        return render_template("edit.html", task=task)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Fake check
    if username != "admin" or password != "123":
        return jsonify({"msg": "Wrong username or password"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    })


@app.route("/profile")
@jwt_required()
def profile():
    username = get_jwt_identity()
    return jsonify({
        "username": username,
        "role": "admin",
        "email": "admin@example.com"
    })


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    username = get_jwt_identity()
    new_access_token = create_access_token(identity=username)
    return jsonify({
        "access_token": new_access_token
    })


if __name__ == "__main__":
   

    app.run(debug=True)
