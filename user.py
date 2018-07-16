import psycopg2
#from database import ConnectionFromPo
from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        # short way to use connection.close(), connection.commit()
        #
        with CursorFromConnectionFromPool() as cursor:
            # using variable cursor using connection called connection to read data
            # data will be read while 'with' command until it is closed by indentation

        #i.e. .closee and .commit are built into with

            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES(%s, %s, %s)',
                           (self.email, self.users.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
                # Query the DB for an email specified by users email (self.email)
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))  # tuple
            user_data = cursor.fetchone()
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
