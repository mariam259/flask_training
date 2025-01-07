# Note App

A full-stack Note-taking application built with Flask and Ninja Templates. This app allows users to create an account, log in, and manage their notes by adding or deleting them. The application uses Flask-Login for user authentication and Flask-SQLAlchemy for database management.

---

## Features

- User Authentication:
  - Create a new account
  - Log in with an existing account
  - Log out
- Note Management:
  - Add new notes
  - Delete existing notes
- Secure and scalable architecture using Flask Blueprints

---

## Technology Stack

- **Backend Framework:** Flask
- **Frontend:** Ninja Templates
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Authentication:** Flask-Login
- **Blueprints:** For modular view management
- **werkzeug.security**: For password hashing

---


## Database Schema

### User Table
| Field         | Type       | Description             |
|---------------|------------|-------------------------|
| id            | Integer    | Primary key             |
| email         | String     | Unique email            |
| password_hash | String     | Hashed password         |
| first_name    | String     | username                |


### Notes Table
| Field         | Type       | Description             |
|---------------|------------|-------------------------|
| id            | Integer    | Primary key             |
| data          | String     | Note Content            |
| date          | DateTime   | Note Date               |
| user_id       | Integer    | Foreign Key             |

---

## Usage

1. **Create an account:**
   - Go to the signup page and create a new account.

2. **Log in:**
   - Log in with your credentials.

3. **Manage notes:**
   - Add a new note using the input field and "Add" button.
   - Delete notes by clicking the "Delete" button next to a note.

---
