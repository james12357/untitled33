import uuid
import pymysql
from flask import Flask, request, render_template, \
    send_from_directory, url_for, redirect, make_response
import os

sql_url = ("127.0.0.1", 3306, "root", "123456")
app = Flask(__name__)
connection = pymysql.connect(host=sql_url[0], port=sql_url[1], user=sql_url[2], passwd=sql_url[3])
cursor = connection.cursor()
cursor.execute("use testdb")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form["username"]

        cursor.execute("select * from webtest where username = '" + data + "'")
        for x in cursor:
            return str(x)
        return "nothing match"
    else:
        return render_template("login.html")


@app.route("/")
def root():
    return make_response(redirect(url_for("login")))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file_upload"]
        if file:
            name = uuid.uuid4().hex + "." + (file.filename.split(".") if "." in file.filename else [file.filename])[-1]
            file.save(os.path.join("upl", name))
            return "Success\n" + "<a href=/view_file/" + name + ">点我</a>"
    else:
        return render_template("printtest.html")


@app.route("/view_file/<filename>")
def view_file(filename):
    return send_from_directory("upl/", filename)


app.run(debug=True)
