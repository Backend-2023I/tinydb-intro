from tinydb import TinyDB
from tinydb.database import Document

db = TinyDB('db.json', indent=4)

document = Document({"name": "Javohir", "age": 24}, doc_id=4)

db.insert(document)