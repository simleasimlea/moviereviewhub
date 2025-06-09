# MovieReviewHub

A minimal Flask MVC app with MySQL backend for submitting personal movie reviews.

## Features

- Add and view movie reviews
- Flask MVC structure
- MySQL database

## Setup Instructions

1. Ensure MySQL is running and create the database:
    ```sql
    CREATE DATABASE moviereviewhub;
    ```

2. Clone this repository.

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

4. Install dependencies:
    ```bash
    pip install flask flask_sqlalchemy pymysql
    ```

5. Update `config.py` with your MySQL username and password.

6. Initialize the database:
    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

7. Run the app:
    ```bash
    flask run
    ```

Visit [http://localhost:5000](http://localhost:5000) in your browser.
