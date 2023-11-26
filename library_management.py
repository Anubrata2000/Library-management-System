import cx_Oracle

# Establish connection with Oracle database
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='ADMIN', password='java', dsn=dsn_tns)

# Function to create a new database table
def create_table():
    cur = conn.cursor()
    #cur.execute("DROP TABLE books")
    #cur.execute("DROP TABLE users")
    #cur.execute("DROP TABLE loans")
    cur.execute("CREATE TABLE books (id NUMBER PRIMARY KEY, title VARCHAR2(100), author VARCHAR2(100), year NUMBER, ISBN NUMBER)")
    cur.execute("CREATE TABLE users (id NUMBER PRIMARY KEY, name VARCHAR2(100), email VARCHAR2(100))")
    cur.execute("CREATE TABLE loans (id NUMBER PRIMARY KEY, book_id NUMBER, user_id NUMBER, loan_date DATE, return_date DATE)")
    conn.commit()
    cur.close()

# Function to insert a new book into the database
def insert_book(id, title, author, year, ISBN):
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (:id, :title, :author, :year, :ISBN)", {'id': id, 'title': title, 'author': author, 'year': year, 'ISBN': ISBN})
    conn.commit()
    cur.close()

# Function to update a book in the database
def update_book(id, title, author, year, ISBN):
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=:title, author=:author, year=:year, ISBN=:ISBN WHERE id=:id", {'id': id, 'title': title, 'author': author, 'year': year, 'ISBN': ISBN})
    conn.commit()
    cur.close()

# Function to delete a book from the database
def delete_book(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=:id", {'id': id})
    conn.commit()
    cur.close()

# Function to search for a book in the database
def search_book(title="", author="", year="", ISBN=""):
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=:title OR author=:author OR year=:year OR ISBN=:ISBN", {'title': title, 'author': author, 'year': year, 'ISBN': ISBN})
    rows = cur.fetchall()
    cur.close()
    return rows

# Function to insert a new user into the database
def insert_user(id, name, email):
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (:id, :name, :email)", {'id': id, 'name': name, 'email': email})
    conn.commit()
    cur.close()

# Function to update a user in the database
def update_user(id, name, email):
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=:name, email=:email WHERE id=:id", {'id': id, 'name': name, 'email': email})
    conn.commit()
    cur.close()

#
# Create tables
#create_table()

# # Insert books
#insert_book(1,"The Great Gatsby", "F. Scott Fitzgerald", 1925, 9780195150339)
#insert_book(2,"To Kill a Mockingbird", "Harper Lee", 1960, 9780446310789)
#insert_book(3,"1984", "George Orwell", 1949, 9780451524935)
#insert_book(4,"Sherlock Holmes", "Arthur Conan Doyle", 1930, 9780451524238)

# Update book
#update_book(1, "The Great Gatsby (Revised Edition)", "F. Scott Fitzgerald", 1925, 9780195150339)

# Delete book
#delete_book(3)

# Search for books
#print(search_book(title="To Kill a Mockingbird"))
#print(search_book(author="George Orwell"))

# Insert users
#insert_user(4, "John Smith", "john.smith@example.com")
#insert_user(5, "Jane Doe", "jane.doe@example.com")

# Update user
#update_user(1, "John Smith Jr.", "john.smith.jr@example.com")

# Close database connection
conn.close()