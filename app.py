from flask import Flask, render_template ,request ,redirect ,session
import sqlite3, random

app = Flask(__name__)

app.secret_key = "akibaco"


@app.route("/" , methods = ["get"])
def login_get():
    return render_template("top.html")

@app.route("/" , methods = ["post"])
def login_post():
    name = request.form.get("user_name")
    password = request.form.get("password")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users where name = ? and password = ?", (name,password))
    id = c.fetchone()
    c.close()
    if id is None:
        return render_template("top.html")
    else:
        session["id"]=id[0]
        print(id)
        return redirect("/map")



















if __name__ == "__main__":
    app.run (debug=True)