from flask import Flask,render_template,request, redirect,url_for,jsonify,json
import psycopg2


app = Flask(__name__)


db = psycopg2.connect(database ="postgres",user="postgres",password = "111",host = "127.0.0.1",)
con = db.cursor()

@app.route('/')
def show_post():
    render_template('')



@app.route('/get_employees')
def get_data():
    p_db = con
    p_db.execute('select json_agg(Employee) from Employee;')
    post = con.fetchall()
    return jsonify({'entry': post})


if __name__ == '__main__':
    app.run(debug=True)