from flask import Blueprint,session,jsonify,request
from flask import Blueprint, request, jsonify, session
from models import db, User, Notes

notes_blueprint = Blueprint('notes', __name__)

@notes_blueprint.route('/add_note', methods=['POST'])
def add_note():
    if 'name' in session:
        data = request.get_json()
        note_text = data.get('note_text')

        user = User.query.filter_by(name=session['name']).first()
        new_note = Notes(note=note_text, user=user)
        db.session.add(new_note)
        db.session.commit()

        return jsonify({'message': 'Note added successfully'})
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@notes_blueprint.route('/get_notes')
def get_notes():
    if 'name' in session:
        user = User.query.filter_by(name=session['name']).first()
        notes = Notes.query.filter_by(user=user).all()

        return jsonify({'notes': [i.note for i in notes]})
    else:
        return jsonify({'error': 'Unauthorized'}), 401
