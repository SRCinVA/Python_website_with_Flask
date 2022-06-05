from xmlrpc.client import Boolean
from flask import Blueprint, render_template

# we're going to define that our file is a blueprint of this application
auth = Blueprint('auth', __name__)  # convention for how to name this
# so you name Blueprint 'auth' but still drop it in a variable

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True) # interestingly, now we can access the text variable from the template
                                                        # in other words, this is how you pass values to your templates
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
