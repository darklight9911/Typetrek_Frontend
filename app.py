
from flask import Flask,render_template,flash,session,url_for, request, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = "adkasdkljaskldjklajdklajsdkljaklsdjasd"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration")
def registrationPage():
    return render_template("registration.html")
@app.route("/login",methods = ["GET","POST"])
def loginPage():
    if request.method == "POST":
        print(request.form)
        if request.form.get('email')=="admin@gmail.com":
            if request.form.get('password')=="1234":
                session['user_logged_in'] =True
                flash("Login successful",'success')
                return redirect("/")
            flash("Wrong password","error")
            return redirect("/login")
        flash("Wrong email","error") 
        return redirect("/login")
    return render_template("login.html")
@app.route('/logout')
def logout():
    session['user_logged_in'] =False
    flash("Logout successful","success")
    return redirect("/login")
if __name__=="__main__":
    app.run(debug=True,port=4545,host='localhost')