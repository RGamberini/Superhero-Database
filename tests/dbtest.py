from Database import Database
db = Database("test.db")
columns = (("First", "text"), ("Last", "text"))
db.create_table("memes",columns)
db.insert("memes", ("Rudy", "Gamberini"))
