# Blueprints for reading list methods.

from helpers import *

mod = Blueprint('reading_lists', __name__)

@mod.route('/')
@mod.route('/reading_lists')
def show_reading_lists():
    """Renders main page of web application containing every reading list.
    If user is logged in, user sees the template with list creation and editing
    features, otherwise the user sees a public template without list creation
    and editing features."""
    reading_lists = session.query(ReadingList).order_by(ReadingList.name.asc()).all()
    if 'username' not in login_session:
        return render_template('publicreadinglists.html',
            reading_lists=reading_lists)
    else:
        return render_template('readinglists.html',
            username=login_session['username'],
            picture=login_session['picture'],
            reading_lists=reading_lists)

@mod.route('/reading_list/new', methods=['GET', 'POST'])
def new_reading_list():
    """Renders template for creating a new reading list."""
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        if request.form['name'] and request.form['description']:
            created_reading_list = ReadingList(name=request.form['name'],
            description=request.form['description'],
            user_id=login_session['user_id'])
            session.add(created_reading_list)
            session.commit()
            flash("Reading list added")
            return redirect(url_for('reading_lists.show_reading_lists'))
        else:
            name = request.form['name']
            description = request.form['description']
            error = "Please enter both a name and description"
            return render_template('newreadinglist.html',
                username=login_session['username'],
                picture=login_session['picture'], name=name,
                description=description, error=error)
    else:
        return render_template('newreadinglist.html',
            username=login_session['username'],
            picture=login_session['picture'])

@mod.route('/reading_list/<int:reading_list_id>/edit', methods=['GET', 'POST'])
def edit_reading_list(reading_list_id):
    """Renders template for editing a reading list. Only the user who created
    a given reading list can edit that list."""
    edited_reading_list = session.query(ReadingList).filter_by(id=reading_list_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if edited_reading_list.user_id != login_session['user_id']:
        return """<script>function myFunction() {alert("You're not authorized to edit this reading list. Please create your own reading list to edit it.");} setTimeout(function() {window.location.href = '/reading_lists';});</script><body onload='myFunction()'>"""
    if request.method == 'POST':
        if request.form['name']:
            edited_reading_list.name = request.form['name']
        if request.form['description']:
            edited_reading_list.description = request.form['description']
        session.add(edited_reading_list)
        session.commit()
        flash("Reading list edited")
        return redirect(url_for('reading_lists.show_reading_lists'))
    else:
        return render_template('editreadinglist.html',
            username=login_session['username'],
            picture=login_session['picture'],
            reading_list=edited_reading_list)

@mod.route('/reading_list/<int:reading_list_id>/delete',
    methods=['GET', 'POST'])
def delete_reading_list(reading_list_id):
    """Renders template for deleting a reading list. Only the user who created
    a given reading list can delete that list."""
    deleted_reading_list = session.query(ReadingList).filter_by(id=reading_list_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if deleted_reading_list.user_id != login_session['user_id']:
        return """<script>function myFunction() {alert("You're not authorized to delete this reading list. Please create your own reading list to edit it.");} setTimeout(function() {window.location.href = '/reading_lists';});</script><body onload='myFunction()'>"""
    if request.method == 'POST':
        session.delete(deleted_reading_list)
        session.commit()
        flash("Reading list deleted")
        return redirect(url_for('reading_lists.show_reading_lists'))
    return render_template('deletereadinglist.html',
        username=login_session['username'],
        picture=login_session['picture'],
        reading_list=deleted_reading_list)