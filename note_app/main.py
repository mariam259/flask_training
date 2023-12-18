from website import create_app

# we will use our create_app function here
app = create_app()
if __name__ == '__main__':      ## if condition is true run this flask app
    app.run(debug=True)       # we set our debug mode to true so if you make any changes to web it will automatically show