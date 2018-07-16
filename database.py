from psycopg2 import pool

#want to create connection pool variable
#connection
#__connection_pool is a private variable
class Database:
    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1,
                                                          1,
                                                          **kwargs)
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()

class CursorFromConnectionFromPool:
    def __init__(self):

        self.connection = None # Initialize the new connection; notice we don't assign connection
        self.cursor = None     # Since the connection has yet to be used

    # Want to return a connection, i.e. connection pool object. Cursor.
    # __enter__ when we enter the with statement we:

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    # An error happens w/in the "with clause" the 3 values of the __exit__ method
    #           1. the exception_type, what type of error it is
    #           2. the exception_value is the value stored within the error
    #           3. exception_traceback where the error happened in the data entry

    #When we exit the with statement in app.py we:
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
