from tinydb import TinyDB
from tinydb.database import Document
from tinydb.queries import Query

db = TinyDB('db.json', indent=4)
User = Query()

data = {"age": 24}

print(db.update(data, User.age == 21))