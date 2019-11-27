from database import DB

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create(self):
        with DB() as db:
            values = (self.id, self.name)
            db.execute('INSERT INTO categories (id, name) VALUES (?, ?)', values)
            return self

    # def save(self):
    #     with DB() as db:
    #         values = (self.name, self.id)
    #         db.execute('UPDATE categories SET name = ? WHERE id = ?', values)
    #         return self

    @staticmethod
    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM categories').fetchall()
            return [Category(*row) for row in rows]
