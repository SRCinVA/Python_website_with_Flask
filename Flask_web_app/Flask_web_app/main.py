from website import create_app

app = create_app()  # the normal set-up stuff

if __name__ == '__main__':  # we have to run just this file, not import something else
    app.run(debug=True)  # everytime we make a change to the code, it will re-run the web server.
    
    # amazingly, this is all it takes to run a webserver



