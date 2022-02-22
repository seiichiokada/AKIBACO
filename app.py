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
    user_id = c.fetchone()
    c.close()
    if user_id is None:
        return render_template("top.html")
    else:
        session["user_id"]=user_id[0]
        print(user_id)
        return redirect("/map")

# 投稿でっせ
@app.route("/map", methods =["GET"])
def add_get():
    return render_template("map.html")

@app.route("/map", methods = ["POST"])
def add_post():
    task = request.form.get("post_column")
    conn = sqlite3.connect("akibacoDB.db")
    c = conn.cursor()
    c.execute("Insert into post_column values (null,?,?)",(task,user_id))
    conn.commit()
    c.close()
    return redirect("/map")

# マップ情報でっせ
@app.route("")




# 投稿リストでっせ





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
    c.execute("Insert into user_name values (null,?,?)",(name,password))
    conn.commit()
    c.close()
    return "登録完了"


if __name__ == "__main__":
    app.run (debug=True)



    # id  name  password  seat_number  use_seat  user_id  contents  