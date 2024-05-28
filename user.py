import sqlite3

class User:
    def __init__(self, username, firstname, lastname, lieblingsverein):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.lieblingsverein = lieblingsverein

    def to_db(self):
        connection = sqlite3.connect("database.db") 
        cursor = connection.cursor()
        sql = f"INSERT INTO users(username, firstname, lastname, lieblingsverein) VALUES ('{self.username}', '{self.firstname}', '{self.lastname}','{self.lieblingsverein}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    
    @classmethod
    def from_db(cls, username):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        sql = f'SELECT username,firstname,lastname,lieblingsverein FROM users WHERE username = "thowin"'
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return User(row[0], row[1], row[2],row[3])

user = User.from_db("thowin")

print(user.username,user.firstname,user.lastname,user.lieblingsverein)
