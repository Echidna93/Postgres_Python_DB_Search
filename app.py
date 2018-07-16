from user import User
from database import Database

Database.initialize(user='postgres', password='Edinburgh.1993', database='dvdrental', host='localhost')


user1 = User("gzckx022@umn.edu", "Agg", "ggk", None)
user1.save_to_db()
user2 = User.load_from_db_by_email('gzckx022@umn.edu')

print(user2)
