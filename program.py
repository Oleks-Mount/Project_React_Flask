from flask import Flask,render_template,request, redirect,url_for
import psycopg2


app = Flask(__name__)


db = psycopg2.connect(database ="postgres",user="postgres",password = "111",host = "127.0.0.1",)
con = db.cursor()

@app.route('/')
def show_post():
    p_db = con
    p_db.execute('select * from Employee;')
    post = con.fetchall()
    return render_template('main_page.html',post = post)



if __name__ == '__main__':
    app.run(debug=True)