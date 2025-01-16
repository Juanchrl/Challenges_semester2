from flask import Flask, render_template
app = Flask(__name__)

titleWeb = "FlaskKu"

data = ["I", "G", "S"]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', titleWeb = titleWeb, data = data, usia = 25 )

@app.route('/IGS')
def about():
    return render_template('IGS.html',data = data)
if __name__ == '__main__':

    app.run(debug=True)