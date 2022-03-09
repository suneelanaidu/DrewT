# import "packages" from flask

from flask import Flask, render_template, request
import requests

# create a Flask instance
app = Flask(__name__)


from crud3.app_crud import app_crud

#from gigiChat import app_gigiChat
#app.register_blueprint(app_gigiChat)

# create a Flask instance

app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("api/unUsed/home.html")

@app.route('/anikaCraft')


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port="5001")
