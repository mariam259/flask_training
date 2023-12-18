# store our main views(pages), store main routes for our web
# anyting that is not related to authentication user can navigate to will have a route here

# blueprint allow us to sperate our files and give each one url to navigate to
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

from .models import Note
from . import db


# it's recommended to name your blueprint variable as your file
views = Blueprint('views', __name__)

# define the name route for our home page


@views.route('/', methods=['GET', 'POST'])
@login_required  # you can't access the home page until you are logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Note is too short", category='error')
        else:
            # create object from Note table then added to database
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # our data come in json form so we need json library to deal with it
    # notes saved as string so we send request to index.js to load it and turn it to dictionary to access it
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:  # check if this note is exist
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
