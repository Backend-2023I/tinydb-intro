from tinydb import TinyDB

db = TinyDB('db.json', indent=4)

user = db.table('users')
language = db.table("programming_language")

data = {
    "languabe": "Python",
    "use": ["Backend", "AI"]
}

print(language.insert(data))