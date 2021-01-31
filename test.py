import psycopg2


db = psycopg2.connect(dbname="postgres", user="postgres", password="111", host="127.0.0.1", port="5432")

con = db.cursor()
p_db = con

p_db.execute("create table Employee (id serial primary key,name text,age integer,job text);")
db.commit()

p_db.execute("insert into Employee  (name,age,job) values('Ivan Peshkov',20,'Developer');")
p_db.execute("insert into Employee  (name,age,job) values('Oleksandr Smith',30,'Doctor');")
p_db.execute("insert into Employee  (name,age,job) values('Ivan Peshkov',25,'PM');")
p_db.execute("insert into Employee  (name,age,job) values('Oleksandr Smith',19,'QA');")
db.commit()

p_db.execute("select * from Employee ;")
posts  = con.fetchall()
for i in posts:
    print(i)
