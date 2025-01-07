# Flask Book API

This project is a simple Flask API that allows users to interact with a book database.

**Features:**

* **Retrieve all books:** Retrieve a list of all books stored in the database.
* **Add a new book:** Create a new book entry in the database.
* **Update a book:** Update the details of an existing book by its ID.
* **Delete a book:** Remove a book from the database by its ID.

**Technologies Used:**

* **Flask:** Python web framework for building the API.
* **SQLite:** Lightweight database for storing book information.
* **Python:** Programming language for API development and database interactions.

**Project Structure:**

* `app.py`: Main application file containing API routes and logic.
* `db.py`: Defines database models for books.
* `books.sqlite` 

**API Endpoints:**

* **GET /books:** Retrieve a list of all books.
* **GET /book/<book_id>:** Retrieve a specific book by its ID.
* **POST /books:** Create a new book.
* **PUT /book/<book_id>:** Update an existing book.
* **DELETE /books/<book_id>:** Delete a book.
