from flask import Flask,render_template,request,redirect,make_response
from orm import operateorm as operate
import datetime

app =Flask(__name__)

app.send_file_max_age_default = datetime.timedelta(seconds=1)
app.debug = True

@app.route("/")
def home():
    user = request.cookies.get("username")
    return render_template("home.html",userid = user)

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        account = request.form["account"]
        password = request.form["pwd"]
        try:
            result = operate.checkuser(account,password)
            if result == -1:
                return render_template("login.html")
            else:
                resp = make_response(redirect("/userinfo"))
                resp.set_cookie("username",result,expires=datetime.datetime.now()+datetime.timedelta(seconds=60))
                return resp
        except:
            return render_template("login.html")


@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        account = request.form["account"]
        password = request.form["pwd"]
        try:
            result = operate.insertuser(username,account,password)
            if result:
                return redirect("/login")
            else:
                return render_template("register.html",resultid = result)
        except:
            return render_template("register.html")

@app.route("/userinfo")
def useinfo():
    return render_template("userinfo.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/applyservice",methods = ["GET","POST"])
def applyservice():
    if request.method == "GET":
        return render_template("applyservice.html")
    elif request.method == "POST":
        project = request.form["pro"]
        describe = request.form["descr"]
        building = request.form["building"]
        unit = request.form["unit"]
        roomnum = request.form["roomnum"]
        username = request.cookies.get("username")
        tel = request.form["phone"]
        try:
            operate.insertservice(project,describe,building,unit,roomnum,username,tel)
            return redirect("/service")
        except:
            return render_template("applyservice.html")

@app.route("/viewservice")
def viewservice():
    username = request.cookies.get("username")
    result = operate.viewservice(username)
    return render_template("viewservice.html",resultlist = result)

@app.route("/maservice")
def maservice():
    username = request.cookies.get("username")
    result = operate.viewservice(username)
    return render_template("maservice.html", resultlist=result)

@app.route("/maservice/<id>")
def delservice(id):
    operate.delservice(id)
    return redirect("/maservice")

@app.route("/quit")
def quit():
    resp = make_response(redirect("/"))
    resp.delete_cookie("username")
    return resp


if __name__ == "__main__":
    app.run()