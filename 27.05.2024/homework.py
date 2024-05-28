import sqlite3


class Product:
    def __init__(self, db_name):
        self.db_name = db_name


class CustomConnectDb:
    def __init__(self, product):
        self.product = product
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.product.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        if exc_type:
            print(exc_val)


product = Product("product.db")


with CustomConnectDb(product) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price VARCHAR)")
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Sample Product", '12 000'))
    conn.commit()