from flask import Flask


# create flask app

app = Flask(__name__)


# comment

# creating the first route for index page
@app.route("/")
def index():
    return f'Homepage'




if __name__ == '__main__':
    app.run(debug=True)