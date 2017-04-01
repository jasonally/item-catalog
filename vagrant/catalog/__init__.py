from flask import Flask, Blueprint
from key import *

app = Flask(__name__)

from views import auth
from views import books
from views import jsons
from views import reading_lists

app.register_blueprint(auth.mod)
app.register_blueprint(books.mod)
app.register_blueprint(jsons.mod)
app.register_blueprint(reading_lists.mod)

if __name__ == '__main__':
    app.secret_key = key
    app.debug = True
    app.run(host='0.0.0.0', port=5000)