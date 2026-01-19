# 📝 Flask Todo App

Ứng dụng Todo nhỏ được viết bằng **Flask** để thực hành kiến trúc backend cơ bản, CRUD và template dùng Jinja.  
Ứng dụng gồm:

- Trang **Home**: xem danh sách task + tạo task
- Trang **Update** riêng để chỉnh sửa task
- Lưu trữ bằng SQLite thông qua SQLAlchemy

---

## 🚀 Demo giao diện

### 🏠 Home page
<p align="center">
  <img src="./screenshots/home.png" width="600">
</p>

### ✏️ Update page
<p align="center">
  <img src="./screenshots/update.png" width="600">
</p>

---

## ✨ Tính năng

✔ Tạo task  
✔ Xem danh sách task  
✔ Xóa task  
✔ Update task tại trang riêng  
✔ Lưu trữ bằng SQLite  
✔ Jinja2 template view  

---

## 🧱 Công nghệ sử dụng

| Component | Công nghệ |
|---|---|
| Backend | Flask |
| Database | SQLite + SQLAlchemy |
| Template | Jinja2 |
| Auth | (tùy) JWT nếu bật |
| UI | HTML + CSS đơn giản |

---

## 📦 Cài đặt & chạy ứng dụng

### 1️⃣ Clone repo

```bash
git clone https://github.com/yourname/flask-todo-app.git
cd flask-todo-app
