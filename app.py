from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration")
def registrationPage():
    return render_template("registration.html")
@app.route("/login")
def loginPage():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True,port=4545,host='localhost')