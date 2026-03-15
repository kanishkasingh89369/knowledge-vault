

from flask import Flask, request, jsonify
from flask_cors import CORS
from db import db, cursor

app = Flask(__name__)
CORS(app)

# Add note
@app.route('/add-note', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data['title']
    content = data['content']

    query = "INSERT INTO notes (title, content) VALUES (%s,%s)"
    cursor.execute(query,(title,content))
    db.commit()

    return jsonify({"message":"Note added successfully"})


# Get all notes
@app.route('/notes', methods=['GET'])
def get_notes():

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    return jsonify(notes)


# Get note by title
@app.route('/note/<title>', methods=['GET'])
def get_note(title):

    query = "SELECT * FROM notes WHERE title=%s"
    cursor.execute(query,(title,))
    note = cursor.fetchone()

    return jsonify(note)


if __name__ == "__main__":
    app.run(debug=True)    