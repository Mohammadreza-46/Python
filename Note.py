from flask import request, jsonify,Flask

app = Flask(__name__)
notes = []
@app.route('/notes',methods=['GET'])

def get_all_notes():
    return jsonify({'notes':notes})
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = None
    for i in notes:
        if i['id'] == note_id:
            note = i
            break
    if note == None:
        return jsonify({'error':'Not found!'}),404
    return jsonify({'note':note})
@app.route('/add_notes', methods=['POST'])
def create_note():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data or 'id' not in data:
        return jsonify({'Not have all!'}),400
    new_note = {
        'id':data['id'],
        'title':data['title'],
        'content':data['content']}

    notes.append(new_note)

    return jsonify({'message':'New note created!','note':new_note}),201

@app.route('/edit_notes/<int:note_id>', methods=['PUT'])

def update_note(note_id):
    note = None
    for i in notes:
        if i['id'] == note_id:
            note = i
            break
    if note == None:
        return jsonify({'error':'Not found!'}),404

    data = request.get_json()
    if 'title' in data:
        note['title'] = data['title']
    if 'content' in data:
        note['content'] = data['content']
    return jsonify({'message':'Note updated!'})
@app.route('/delete_notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = None
    for i in notes:
        if i['id'] == note_id:
            note = i
            break
    if note == None:
        return jsonify({'error':'Not found!'}),404
    notes.remove(note)
    return jsonify({'message':'Note deleted!'})
if __name__ == '__main__':
    app.run(debug=True)
