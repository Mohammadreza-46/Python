This project is a simple REST API built with Flask. It allows users to sign up, log in, and manage books. The system stores users and books in JSON files. Authentication is handled using a generated key after login.

Features
User signup
User login
User logout
Add a new book
Get all books
Delete a book

Technologies Used
Python
Flask
JSON file storage

Project Structure
Users are stored as separate JSON files inside the Users folder.
Books are stored inside Book_Loader.json.
Active login keys are stored inside Keys.json.

How To Run

Install Python.

Install Flask using pip install flask

Run the file using python filename.py

The server will start in debug mode.

API Endpoints

POST /signup
Create a new user.
Required fields: username, password

POST /login
Login with username and password.
Returns a login key.

DELETE /logout/<key>
Logout user and remove session key.

POST /add_book/<key>
Add a new book.
Required fields: book_name, book_content, book_id, writer

GET /get_all_book/<key>
Return all stored books.

DELETE /delete_book/<book_id>/<key>
Delete a book by its id.

Notes
Username must be at least 8 characters.
Passwords are stored using Python hash function.
Data persistence is handled using JSON files.