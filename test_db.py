from pymongo import MongoClient



client = MongoClient('localhost',27017)

my_db = client['Employee']

mycollection = my_db['Worker']

mycollection.insert_many([
    {"name":"Ivan",
     "age":20,
     "job":"Doctor"},
    {"name":"Oleks",
     "age":21,
     "job":"Developer"},
    {"name":"Max",
     "age":21,
     "job":"Developer"}
])







