from flask import Flask, render_template ,request ,redirect ,session
import sqlite3


app = Flask(__name__)
app.secret_key = "akibaco"


# ログインでっせ
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


# 投稿でっせ
@app.route("/map", methods =["GET"])
def add_get():
    return render_template("map.html")

@app.route("/map", methods = ["POST"])
def add_post():
    task = request.form.get("task_kist")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("Insert into post_column values (null,?,?)",(task,user_id))
    conn.commit()
    c.close()
    return redirect("/map")


# マップ情報でっせ

#@app.route("")


# 投稿リストでっせ
@app.route("/map")
def list():
    if "user_id" in session:
        user_id = session["user_id"]
        conn = sqlite3.connect("akibacoDB.db")
        c = conn.cursor()
        c.execute("SELECT id, task FROM task where user_id = ?", (user_id,))
        task_list = []
        for row in c.fetchall():
            task_list.append({"id":row[0],"task":row[1]})
        c.close()
        print(task_list)
        return render_template("map.html", task_list = task_list)
    else:
        return redirect("/top")


# 新規登録でっせ
@app.route("/regist", methods = ["get"])
def regist_get():
    return render_template("regist.html")

@app.route("/regist", methods = ["POST"])
def regist_post():
    name = request.form.get("user_name")
    password = request.form.get("password")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("Insert into users values (null,?,?)",(name,password))
    conn.commit()
    c.close()
    return redirect("/map")


if __name__ == "__main__":
    app.run (debug=True)