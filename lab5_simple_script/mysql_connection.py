import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="exdb"
)

c = db.cursor();

c.execute("INSERT INTO books (name, description) VALUES (%s, %s);", ('book', 'book description'))

db.commit()

c.execute("SELECT * FROM books;")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()

