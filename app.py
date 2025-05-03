from flask import Flask, render_template


# create flask app

app = Flask(__name__)



# creating the first route for index page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# creating the student route
@app.route("/student", methods=['GET', 'POST'])
def student_list():
    return render_template('student.html')



if __name__ == '__main__':
    app.run(debug=True)