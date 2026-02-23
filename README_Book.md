#Book file guide

This project is a simple Flask API for user authentication and book management.
It allows users to sign up, log in, add books, view all books, delete books, and log out.
All data is stored locally using JSON files and no database is used.
The project uses Python and Flask.
Required libraries are Flask, json, random, and os.
Flask must be installed manually using pip, the other libraries are built into Python.
User information is stored in the Users folder.
Each user has a separate file that contains the username, hashed password, and a unique key.
Keys.json is used to store active login keys.
When a user logs in, their key is saved there and used to authorize requests.
Book_Loader.json stores all book data.
Each book has a name, content, writer, and book ID.
The signup endpoint creates a new user and saves their information.
The login endpoint verifies user credentials and returns a key.
The add book endpoint allows logged‑in users to add new books.
The get all books endpoint returns all stored books.
The delete book endpoint removes a book by its ID.
The logout endpoint removes the user key and ends the session.

To run the project, execute the Python file and the Flask server will start on localhost.

