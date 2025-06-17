# MovieReviewHub – Student Starter App

This is a minimal Flask application that allows users to add and view movie reviews. It uses **SQLite** to keep setup simple—no database installation required!

---

## 📁 Project Structure

```
MiniApp/
├── app.py              # Main Flask app
├── config.py           # Database config (uses SQLite)
├── controllers.py      # Route handlers
├── models.py           # SQLAlchemy model for movies
├── templates/          # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   └── add.html
├── static/style.css    # Basic styling
├── requirements.txt    # List of Python packages
└── app.db              # SQLite database (auto-generated)
```

---

## 🧰 Prerequisites

- Python 3.x
- VS Code or any editor
- (Optional) DB Browser for SQLite: https://sqlitebrowser.org/

---

## ⚙️ Setup Instructions

1. **Clone the repo or unzip the folder**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate it**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Run the App

```bash
flask run
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 💾 Database Info

- The app uses `SQLite`, and the file `app.db` is created **automatically** on first run.
- You don’t need to manually create any tables.
- Reviews are stored in the `movie` table.

---

## 🔍 View or Inspect the Database

Optionally use:
- `sqlite3 app.db` from the terminal
- Or open `app.db` in [DB Browser for SQLite](https://sqlitebrowser.org/)

---

## 🧪 Add a Review

1. Click “Add New Review”
2. Submit a movie title, director, and review
3. It will be saved and shown on the homepage

---

## ✅ Reminder

If the app isn't saving:
- Make sure only one terminal/browser session is open
- Visit the homepage first to trigger DB creation
- Check for any errors in the terminal

---

Happy coding! 🎬
