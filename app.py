from flask import Flask, render_template ,request ,redirect ,session
import sqlite3


app = Flask(__name__)
app.secret_key = "akibaco"


# ログインでっせ
@app.route("/" , methods = ["GET"])
def login_get():
    return render_template("top.html")

@app.route("/" , methods = ["POST"])
def login_post():
    name = request.form.get("user_name")
    password = request.form.get("password")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users where name = ? and password = ?", (name,password))
    user_id = c.fetchone()
    c.close()
    if user_id is None:
        return render_template("top.html")
    else:
        session["user_id"]=user_id[0]
        print(user_id)
        return redirect("/map")


# 投稿でっせ
@app.route("/add", methods =["GET"])
def add_get():
    return render_template("add.html")

@app.route("/add", methods = ["POST"])
def add_post():
    user_id = session["user_id"]
    task = request.form.get("task")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("Insert into task values (null,?,?)",(task , user_id))
    conn.commit()
    c.close()
    return redirect("/bbs")


# マップ情報でっせ
@app.route("/map")
def seat():
    return render_template("map.html")
    # if "user_id" in session:
    #     user_id = session["user_id"]
    #     conn = sqlite3.connect("akibacoDB.db")
    #     c = conn.cursor()
    #     c.execute("SELECT seat_number , use_seat FROM map")
    #     task_list = []
    #     for row in c.fetchall():
    #         task_list.append({"seat_number":row[0],"use_seat":row[1]})
    #     c.close()
    #     print(task_list)
    #     return render_template("map.html", task_list = task_list)
    # else:
    #     return redirect("/map")

# 投稿リストでっせ
@app.route("/bbs")
def list():
    if "user_id" in session:
        print("読み込めた")
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
        return "読み込めない!"
        print("読み込めない!")





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
    return redirect("/")


# @app.route("/edit")
# def mapedit():
#     return render_template("map.html")

if __name__ == "__main__":
    app.run (debug=True)