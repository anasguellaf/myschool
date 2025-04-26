from flask import Flask, render_template


# create flask app

app = Flask(__name__)


# comment

# creating the first route for index page
@app.route("/")
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)