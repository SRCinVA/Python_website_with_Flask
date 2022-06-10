from crypt import methods
from xmlrpc.client import Boolean
from flask import Blueprint, render_template, request

# we're going to define that our file is a blueprint of this application
auth = Blueprint('auth', __name__)  # convention for how to name this
# so you name Blueprint 'auth' but still drop it in a variable

@auth.route('/login', methods = ['GET', 'POST'])  
def login():  # it's key for these methods to be able to accept requests (the second parameter, in this case)
    # data = request.form
    # print(data) # this is a way to test if the form attribute (the info you fill in) is passed (happily, it is).
    return render_template("login.html", boolean=True) # interestingly, now we can access the text variable from the template
                                                        # in other words, this is how you pass values to your templates
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email') # as in, 'get' the email from the form (we still want to post to the backend).
        firstName = request.form.get('firstName') 
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # to validate the data before creating an account:
        if len(email) < 4:
            pass
        elif len (firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to DB


    return render_template("sign_up.html")
