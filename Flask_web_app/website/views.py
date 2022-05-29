from flask import Blueprint

# we're going to define that our file is a blueprint of this application
views = Blueprint('views', __name__) # convention for how to name this
                                    # so you name Blueprint 'views' but still drop it in a variable

# Remember that a view and a route are the same thing
@views.route('/') # obviously the simplest route possible, this will be the homepage
def home():  # couldn't be simpler: this function will run whenever we go to this page.
    return "<h1>Test<h1>"