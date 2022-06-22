from asyncore import file_dispatcher
from crypt import methods
from xmlrpc.client import Boolean
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

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
            flash("Email must be longer than 3 characters.", category="error") # an interesting module within Flask, and you can label the category.
        elif len (firstName) < 2:
            flash("The first name must be longer than 1 character.", category="error")
        elif password1 != password2:
            flash("The passwords don\'t match.", category="error") # notice the escape character
        elif len(password1) < 7:
            flash("The password must be at least 7 characters long.", category="error")
        else:
            new_user = User(email = email, firstName = firstName, password = generate_password_hash(password1, method="sha256"))  # here, we are importing a new user. 
            db.session.add(new_user) # adds the user to the db
            db.session.commit()      # commits it to the database
            flash("Account created!", category="success")
            # Related note:
            # sha256 is a hashing algorithm, which hashes the password into a new form such that the old form can't be retrieved (making it more secure).
            # now we need to add it to the database
            # after we create the user, we should redirect them to the sign-in page.
            # net, we will return a redirect to the url for the homepage:
            return redirect(url_for("views.home"))  # we want to go there to the 'home' function of the 'views' blueprint.
                                                    # it's better to spell out the url_for and the page name. If you just cited the direct link ('/') you could never change it.

    return render_template("sign_up.html")
