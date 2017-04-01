# Blueprints for JSON-generating methods.

from helpers import *

mod = Blueprint('jsons', __name__)

@mod.route('/reading_lists/JSON')
def reading_lists_json():
    """Generates JSON containing information about all reading lists."""
    reading_lists = session.query(ReadingList).order_by(ReadingList.name.asc()).all()
    return jsonify(ReadingLists=[r.serialize for r in reading_lists])

@mod.route('/reading_list/<int:reading_list_id>/JSON')
def reading_list_json(reading_list_id):
    """Generates JSON containing information for one reading list."""
    reading_list = session.query(ReadingList).filter_by(id=reading_list_id).one()
    return jsonify(ReadingList=reading_list.serialize)

@mod.route('/reading_list/<int:reading_list_id>/books/JSON')
def reading_list_books_json(reading_list_id):
    """Generates JSON containing information for all books in a given reading
    list."""
    reading_list = session.query(ReadingList).filter_by(id=reading_list_id).one()
    books = session.query(Book).filter_by(reading_list_id=reading_list.id).order_by(Book.id.asc()).all()
    return jsonify(Books=[b.serialize for b in books])

@mod.route('/reading_list/<int:reading_list_id>/books/<int:book_id>/JSON')
def book_json(reading_list_id, book_id):
    """Generates JSON containing information for one book in a given reading
    list."""
    book = session.query(Book).filter_by(id=book_id).one()
    return jsonify(Book=book.serialize)