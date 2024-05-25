# 1

# import time
# from contextlib import contextmanager
#
#
# @contextmanager
# def timer():
#     start_time = time.time()
#     try:
#         yield
#     finally:
#         end_time = time.time()
#         updated_time = end_time - start_time
#         print(f"Elapsed time: {updated_time:.6f} seconds")
#
#
# with timer():
#     product = 1
#     for i in range(1, 100001):
#         product *= i


# 2

import sqlite3
from contextlib import contextmanager

@contextmanager
def database_manager(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table")
    initial_data = cursor.fetchall()
    print("Initial data:", initial_data)

    try:
        yield cursor
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


db_name = 'test.db'


with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, value TEXT)")
    cursor.execute("INSERT INTO test_table (value) VALUES ('Initial')")
    conn.commit()


with database_manager(db_name) as cursor:
    cursor.execute("INSERT INTO test_table (value) VALUES ('Updated')")


with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table")
    updated_data = cursor.fetchall()
    print("Updated data:", updated_data)
