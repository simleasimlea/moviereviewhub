# MovieReviewHub

MovieReviewHub is a minimal Flask MVC web application where users can submit and view personal reviews of their favorite movies. This project is designed to demonstrate the fundamentals of full-stack application development using Flask, a MySQL backend, and basic HTML/CSS for the frontend.

---

## 🧱 Project Structure

```
moviereviewhub/
├── app.py                # Main Flask app entry point
├── config.py             # App configuration (including DB URI)
├── controllers.py        # Controller functions (routes)
├── models.py             # SQLAlchemy models
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   └── add.html
├── static/               # CSS files
│   └── style.css
├── README.md             # Project instructions
└── create_moviereviewhub_db.sql # SQL script to initialize the DB
```

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure the following are installed on your machine:
- Python 3.7 or higher
- pip (Python package manager)
- MySQL Server (or a local MySQL-compatible database like MariaDB)
- Git (optional but recommended)

---

### 2. Set Up MySQL Database

1. Start your MySQL server.
2. Open your MySQL client and run the following command:

```sql
CREATE DATABASE moviereviewhub;
```

3. Alternatively, you can run the provided SQL script:

```bash
mysql -u <your_username> -p < create_moviereviewhub_db.sql
```

Replace `<your_username>` with your MySQL username. The script includes table creation.

---

### 3. Clone or Download the Repository

If you haven't already:
```bash
git clone https://github.com/yourusername/moviereviewhub.git
cd moviereviewhub
```

---

### 4. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate      # Windows
```

---

### 5. Install Dependencies

```bash
pip install flask flask_sqlalchemy pymysql
```

---

### 6. Configure Database Connection

In `config.py`, update the database URI with your credentials:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/moviereviewhub'
```

Replace `username` and `password` with your MySQL credentials.

---

### 7. Initialize the Database

Start a Flask shell:

```bash
flask shell
```

Then run:

```python
from app import db
db.create_all()
exit()
```

---

### 8. Run the App

```bash
flask run
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## ✍️ How to Use

- On the home page, you'll see a list of submitted movie reviews.
- Click “Add New Review” to submit a new movie title, director, and your opinion.
- Reviews will be saved and shown on the homepage.

---

## ✅ Educational Goals

- Understand MVC architecture in Flask
- Learn SQLAlchemy and database integration
- Use Jinja templates and HTML forms
- Practice using Git and GitHub for version control

---

## 🔐 Security Notes

This app is for educational use. If deploying publicly:
- Add CSRF protection
- Sanitize user input
- Implement login/authentication
