# Blueprints for book methods.

import re
from helpers import *

AMAZON_RE = re.compile(r"(https?:\/\/)?(www\.)?amazon\.[^/]+\/")

def valid_amazon_url(url):
    return AMAZON_RE.match(url)

mod = Blueprint('books', __name__)

@mod.route('/reading_list/<int:reading_list_id>')
@mod.route('/reading_list/<int:reading_list_id>/books')
def show_book(reading_list_id):
    """Renders page containing the books in a given reading list. If user is
    logged in and is the user who created the list, user sees book creation and
    editing features. Otherwise the user sees a public template without list
    creation and editing features."""
    reading_list = session.query(ReadingList).filter_by(id=reading_list_id).one()
    creator = get_user_info(reading_list.user_id)
    books = session.query(Book).filter_by(reading_list_id=reading_list_id).order_by(Book.id.asc()).all()
    if 'username' not in login_session:
        return render_template('publicbook.html', reading_list=reading_list,
            books=books, creator=creator)
    elif creator.id != login_session['user_id']:
        return render_template('publicbook.html',
            username=login_session['username'],
            picture=login_session['picture'],
            reading_list=reading_list,
            books=books, creator=creator)
    else:
        return render_template('book.html', username=login_session['username'],
            picture=login_session['picture'], reading_list=reading_list,
            books=books, creator=creator)

@mod.route('/reading_list/<int:reading_list_id>/books/new',
    methods=['GET', 'POST'])
def new_book(reading_list_id):
    """Renders template for adding a book to a given reading list. Only the
    user who created the reading list can add books to it. Template also has
    error validation to ensure entries are complete and contain an Amazon URL.
    """
    if 'username' not in login_session:
        return redirect('/login')
    has_error = False
    params = dict(reading_list_id=reading_list_id)
    if request.method == 'POST':
        if not request.form['name']:
            params['name_error'] = "Please give your book a title."
            has_error = True
        # Set a default value to category so the post request won't error out
        if request.form.get('category', 0) == 0:
            params['category_error'] = "Please give your book a category."
            has_error = True
        if not (request.form['author_first_name'] and
            request.form['author_last_name']):
            params['author_error'] = """Please provide the author's first and
            last name."""
            has_error = True
        if not request.form['description']:
            params['description_error'] = """Please provide a description of
            your book."""
            has_error = True
        if not valid_amazon_url(request.form['website']):
            params['website_error'] = "Please provide an Amazon listing URL."
            has_error = True
        if has_error:
            return render_template('newbook.html',
                username=login_session['username'],
                picture=login_session['picture'],
                name=request.form['name'],
                author_first_name=request.form['author_first_name'],
                author_last_name=request.form['author_last_name'],
                description=request.form['description'],
                website=request.form['website'], **params)
        else:
            new_book = Book(name=request.form['name'],
                category=request.form['category'],
                author_first_name=request.form['author_first_name'],
                author_last_name=request.form['author_last_name'],
                description=request.form['description'],
                website=request.form['website'],
                reading_list_id=reading_list_id,
                user_id = login_session['user_id'])
            session.add(new_book)
            session.commit()
            flash("Book added")
            return redirect(url_for('books.show_book',
                reading_list_id=reading_list_id))
    else:
        return render_template('newbook.html',
            username=login_session['username'],
            picture=login_session['picture'],
            reading_list_id=reading_list_id)

@mod.route('/reading_list/<int:reading_list_id>/books/<int:book_id>/edit',
    methods=['GET', 'POST'])
def edit_book(reading_list_id, book_id):
    """Renders template for editing a book in given reading list. Only the
    user who created the reading list can edit books. If the user changes the
    Amazon URL, there's validation to make sure the new URL is also on an
    Amazon website."""
    edited_book = session.query(Book).filter_by(id=book_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if edited_book.user_id != login_session['user_id']:
        return """<script>function myFunction() {alert("You're not authorized to edit this book. Please create your own reading list and books to edit them.");} setTimeout(function() {window.location.href = '/reading_list/%s/books';});</script><body onload='myFunction()'>""" % reading_list_id
    if request.method == 'POST':
        if request.form['website']:
            if not valid_amazon_url(request.form['website']):
                website_error = "Please provide an Amazon listing URL."
                return render_template('editbook.html',
                    username=login_session['username'],
                    picture=login_session['picture'],
                    reading_list_id=reading_list_id, book_id=book_id,
                    book=edited_book, website_error=website_error)
            else:
                edited_book.website = request.form['website']
        if request.form['name']:
            edited_book.name = request.form['name']
        if request.form['category']:
            edited_book.category = request.form['category']
        if request.form['author_first_name']:
            edited_book.author_first_name = request.form['author_first_name']
        if request.form['author_last_name']:
            edited_book.author_last_name = request.form['author_last_name']
        if request.form['description']:
            edited_book.description = request.form['description']
        session.add(edited_book)
        session.commit()
        flash("Book edited")
        return redirect(url_for('books.show_book',
            reading_list_id=reading_list_id))
    else:
        return render_template('editbook.html',
            username=login_session['username'],
            picture=login_session['picture'],
            reading_list_id=reading_list_id,
            book_id=book_id, book=edited_book)

@mod.route('/reading_list/<int:reading_list_id>/books/<int:book_id>/delete',
    methods=['GET', 'POST'])
def delete_book(reading_list_id, book_id):
    """Renders template for deleting a book in a given reading list. Only the
    user who created the reading list can delete books from it."""
    deleted_book = session.query(Book).filter_by(id=book_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if deleted_book.user_id != login_session['user_id']:
        return """<script>function myFunction() {alert("You're not authorized to delete this book. Please create your own reading list and books to delete them.");} setTimeout(function() {window.location.href = '/reading_list/%s/books';});</script><body onload='myFunction()'>""" % reading_list_id
    if request.method == 'POST':
        session.delete(deleted_book)
        session.commit()
        flash("Book deleted")
        return redirect(url_for('books.show_book',
            reading_list_id=reading_list_id))
    return render_template('deletebook.html',
        username=login_session['username'],
        picture=login_session['picture'],
        reading_list_id=reading_list_id,
        book_id=book_id, book=deleted_book)