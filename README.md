# 📝 Flask Blog App

A fully functional **CRUD web application** built with **Flask**, **SQLAlchemy**, and **Flask-WTF**.  
It allows users to create, view, edit, and delete blog posts through a clean, responsive interface.

---

## 🚀 Features

✅ Create, Read, Update, and Delete (CRUD) blog posts  
✅ Flask-WTF form validation  
✅ SQLite database with SQLAlchemy ORM  
✅ Flash messages for user feedback  
✅ Responsive layout with custom CSS  
✅ Modular Jinja2 templates (base, home, post, form)  
✅ Clean and production-ready folder structure  

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Database** | SQLite + SQLAlchemy ORM |
| **Forms** | Flask-WTF |
| **Frontend** | HTML, CSS, Jinja2 |
| **Version Control** | Git + GitHub |

---

## 📁 Project Structure

flask_blog/
│
├── app.py # Main Flask app
├── forms.py # Flask-WTF form class
├── requirements.txt # Project dependencies
│
├── instance/
│ └── blog.db # SQLite database
│
├── static/
│ └── style.css # Final professional CSS
│
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── new_post.html
│ ├── post.html
│ └── edit_post.html
│
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/kaydder/blog_flask.git
2️⃣ Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Initialize the database
python
>>> from app import db
>>> db.create_all()
>>> exit()
5️⃣ Run the app
python app.py
Then open 👉 http://127.0.0.1:5000

📜 License
This project is open-source and available under the MIT License.

👤 Author
Kayder Murillo
📍 Panama
💼 Systems and Computing Engineering Student – Universidad Interamericana de Panamá
