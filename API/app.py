# use jsonify to encode python dictionary
from flask import Flask, request, jsonify
import json
import sqlite3
app = Flask(__name__)

# commented code is before using database to store our data

'''
 book_list = book_list = [
    {
        "id": 0,
        "author": "J.K. Rowling",
        "language": "English",
        "title": "Harry Potter and the Sorcerer's Stone",
    },
    {
        "id": 1,
        "author": "J.R.R. Tolkien",
        "language": "English",
        "title": "The Lord of the Rings: The Fellowship of the Ring",
    },
    {
        "id": 2,
        "author": "C.S. Lewis",
        "language": "English",
        "title": "The Lion, the Witch and the Wardrobe",
    },
    {
        "id": 3,
        "author": "Harper Lee",
        "language": "English",
        "title": "To Kill a Mockingbird",
    },
    {
        "id": 4,
        "author": "George Orwell",
        "language": "English",
        "title": "Animal Farm",
    },
    {
        "id": 5,
        "author": "J.D. Salinger",
        "language": "English",
        "title": "The Catcher in the Rye",
    },
    {
        "id": 6,
        "author": "F. Scott Fitzgerald",
        "language": "English",
        "title": "The Great Gatsby",
    },
    {
        "id": 7,
        "author": "Ernest Hemingway",
        "language": "English",
        "title": "The Old Man and the Sea",
    },
    {
        "id": 8,
        "author": "Jane Austen",
        "language": "English",
        "title": "Pride and Prejudice",
    },
    {
        "id": 9,
        "author": "Charles Dickens",
        "language": "English",
        "title": "A Tale of Two Cities",
    },
]
'''


def db_connection():  # used to connect to database
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        # using database to handle our get request
        cursor = conn.execute("SELECT * FROM book")
        books = [
            # create a dictionary from our rows in database
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            # fetchall return all the rows in database
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        # if len(book_list) > 0:
        #     #jsonify() function used to convert the output of a function to a JSON response object
        #     return jsonify(book_list)
        # else:
        #     "Nothing Found" , 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        # ID = book_list[-1]['id'] + 1          #it will added to database automatically

        # insert our new book in our database
        sql = """ INSERT INTO book (author , language, title) VALUES (? , ? ,?)"""      # ? is a placeholder for values we will pass
        cursor = cursor.execute(sql, (new_author, new_language, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201
        # lastrowid return the id of the last inserted record
        # new_book = {'id': ID, 'author': new_author,
        #             'language': new_language, 'title': new_title}
        # book_list.append(new_book)
        # return jsonify(book_list), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "something is wrong", 404
        # for book in book_list:
        #     if book['id'] == id:
        #         return jsonify(book)

    if request.method == 'PUT':
        sql = """UPDATE book 
        SET title=?, author=? , language=? 
        WHERE id=?"""
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        # for book in book_list:
        #     if book['id'] == id:
        #         book['author'] = request.form['author']
        #         book['language'] = request.form['language']
        #         book['title'] = request.form['title']
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return f"The book with id: {id} has been deleted", 200
        # for index, book in enumerate(book_list):
        #     if book['id'] == id:
        #         book_list.pop(index)
        #         return jsonify(book_list)


if __name__ == '__main__':
    app.run()
