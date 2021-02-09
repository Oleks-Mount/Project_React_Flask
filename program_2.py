from flask import Flask,render_template,url_for,request,json,jsonify

from pymongo import MongoClient


app = Flask(__name__,template_folder = "client/build",static_folder = "client/build/static")


@app.route('/')
def show_users():
    #url_for('static', filename='style.css')
    return render_template('index.html')

#display data
@app.route('/get_employee', methods =['GET'])
def get_data():
    client = MongoClient('localhost',27017)
    db = client['Employee']
    my_collection = db['Worker']
    data = []
    for t in my_collection.find():
        data.append({'name': t['name'],
                'age': t['age'],
                'job': t['job']})
    return jsonify({'workers':data})


#insert data/try create form
@app.route('/insert_employee',methods = ['POST'])
def new_worker():
    client = MongoClient('localhost',27017)
    db = client['Employee']
    my_collection = db['Worker']
    name = request.json['name']
    age = request.json['age']
    job = request.json['job']
    entry = my_collection.insert({'name':name,'age':age,'job':job})
    new_entry = my_collection.find({'_id':entry})
    data_new_worker = {'name':new_entry['name'],'age':new_entry['age'],'job':new_entry['job']}
    return jsonify({'new_worker':data_new_worker})





if __name__ == '__main__':
    app.run(debug=True)