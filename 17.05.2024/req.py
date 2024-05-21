import requests
import psycopg2
from collections import namedtuple
import json


Product = namedtuple('Product', ['title', 'description', 'price', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail', 'images'])


url = 'https://dummyjson.com/products/'
r = requests.get(url)


conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='258182126',
                        host='localhost',
                        port=5432)


drop_table_query = "DROP TABLE IF EXISTS products;"


create_table_products_query = """CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    price INT,
    discountPercentage FLOAT,
    rating FLOAT,
    stock INT,
    brand VARCHAR(255),
    category VARCHAR(200),
    thumbnail VARCHAR(255),
    images JSONB
);"""

cur = conn.cursor()

cur.execute(drop_table_query)
cur.execute(create_table_products_query)
conn.commit()


insert_into_query = """INSERT INTO products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


products = r.json()['products']
for product in products:
    product_data = Product(
        title=product['title'],
        description=product['description'],
        price=product['price'],
        discountPercentage=product['discountPercentage'],
        rating=product['rating'],
        stock=product['stock'],
        brand=product['brand'],
        category=product['category'],
        thumbnail=product['thumbnail'],
        images=json.dumps(product['images'])
    )
    cur.execute(insert_into_query, (
        product_data.title, product_data.description, product_data.price, product_data.discountPercentage, product_data.rating,
        product_data.stock, product_data.brand, product_data.category, product_data.thumbnail, product_data.images))
    conn.commit()


Person = namedtuple('Person', ['name', 'age', 'email'])


cur.close()
conn.close()