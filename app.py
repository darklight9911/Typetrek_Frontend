from flask import Flask,render_template,flash,session,url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = "adkasdkljaskldjklajdklajsdkljaklsdjasd"
@app.route("/")
def index():
    flash(" this an error message this an error message this an error message this an error message","info")
    return render_template("index.html")
@app.route("/registration")
def registrationPage():
    return render_template("registration.html")
@app.route("/login")
def loginPage():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True,port=4545,host='localhost')