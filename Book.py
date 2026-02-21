from flask import request, jsonify, Flask
import json
import random
import os

dir_name = os.path.dirname(__file__)
with open(os.path.join(dir_name, 'Keys.json'), 'r') as f:
    keys = json.load(f)
    for i in list(keys.keys()):
        del keys[i]
        keys[int(i)] = True
with open(os.path.join(dir_name,'Book_Loader.json')) as f:
    data = json.load(f)
    book = data
app = Flask(__name__)
@app.route('/signup',methods=['POST'])
def signup():
    data = request.get_json()
    if data is None or 'password' not in data or 'username' not in data:
        return jsonify({'message': 'not have all'}),400
    data['key'] = random.randint(1000000000,10000000000000000000000000)
    data['password'] = hash(str(data['password']))
    file_name = os.path.join(os.path.join(dir_name,'Users'),data['username'])
    with open(file_name,'w') as f:
        f.write(json.dumps(data))
    return jsonify({'message': 'success'})
@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    if data is None or 'password' not in data or 'username' not in data:
        return jsonify({'message': 'not have all'}),400
    data['password'] = hash(str(data['password']))
    try:
        file_name = os.path.join(os.path.join(dir_name,'Users'),data['username'])
        with open(file_name,'r') as f:
            json_data = json.loads(f.read())
            if json_data['password'] == data['password'] and json_data['username'] == data['username']:
                keys[json_data['key']] = True
                with open(os.path.join(dir_name,'Keys.json'),'w') as f:
                    f.write(json.dumps(keys))
                print(f'username:{json_data["username"]}\npassword:{json_data["password"]}\nkey:{json_data["key"]}\nthis user login successfully!')
                return jsonify({'message': 'success','key': json_data['key']})
            elif json_data['password'] != data['password']:
                return jsonify({'message': 'password is bad'}),400
            elif json_data['username'] != data['username']:
                return jsonify({'message': 'username is bad'}),400
    except FileNotFoundError:
        return jsonify({'message': 'username is bad'}),400
@app.route('/add_book/<int:key>', methods=['POST'])
def add_book(key):
    try:
        if keys[key]:
            data = request.get_json()
            if 'book_name' not in data or 'book_content' not in data or 'book_id' not in data or 'writer' not in data or data == None:
                return jsonify({'Not have all!'}), 400
            new_book = {
                'book_name': data['book_name'],
                'book_content': data['book_content'],
                'book_id': data['book_id'],
                'writer': data['writer']
            }
            book[new_book['book_id']] = new_book
            with open(os.path.join(dir_name,"Book_Loader.json"), 'w') as f:
                f.write(json.dumps(book))
            return jsonify({'Success': 'New book added'}), 201
    except KeyError:
        return jsonify({'message': 'Not login'}),400
@app.route('/get_all_book/<int:key>', methods=['GET'])
def get_all_book(key):
    try:
        if keys[key]:
            return jsonify({'book': book}), 200
    except KeyError:
        return jsonify({'message': 'Not login!'}), 401

@app.route('/delete_book/<int:book_id>/<int:key>', methods=['DELETE'])
def delete_book(book_id,key):
    try:
        if keys[key]:
            deleted_book = None
            for i in book.values():
                if i["book_id"] == book_id:
                    deleted_book = str(i['book_id'])
                    break
            if deleted_book == None:
                return jsonify({'error': 'Not found!'}), 404
            del book[deleted_book]
            with open(os.path.join(dir_name,'Book_Loader.json'), 'w') as f:
                f.write(json.dumps(book))
            return jsonify({'Success': 'Book deleted'}), 200
    except KeyError:
        return jsonify({'message': 'Not login!'}), 400
@app.route('/logout/<int:key>', methods=['DELETE'])
def logout(key):
    try:
        if keys[key]:
            del keys[key]
            with open(os.path.join(dir_name,'Keys.json'),'w') as f:
                f.write(json.dumps(keys))
            return jsonify({'message': 'success'}), 200
    except KeyError:
        return jsonify({'message': 'Not Login!'}), 401
if __name__ == '__main__':
    app.run(debug=True)