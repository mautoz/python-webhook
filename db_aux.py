from datetime import date
import psycopg2 as db
from random import randrange
import random as rand
import datetime
from contextlib import contextmanager

rand.seed(datetime.datetime.now())

@contextmanager
def connect_db(db_credentials):
    conn = db.connect(**db_credentials)
    print("Conectando ao BD!")
    yield conn
    conn.close()

def insert_db(conn, table, review):
    try:
        cur = conn.cursor()
        query = f"INSERT INTO {table} ( \
                scraper_date, \
                review_source, \
                review_app, \
                review_language, \
                review_raw \
            ) VALUES (%s, %s, %s, %s, %s)"
        values = (
            review["scraper_date"],
            review["source"],
            review["app_name"],
            review["language"],
            review["review_content"]
        )
        cur.execute(query, values)
        print("+ Inserting...")
        conn.commit()
    except Exception as err:
        print(err)
        print("- Something get wrong! The file wasn't inserted!")
        raise


def search_file(conn, table, id):
    cur = conn.cursor()
    cur.execute(f"SELECT review_app, review_raw FROM {table} WHERE id={id}")
    current_review = cur.fetchone()
    return current_review

def random_review(conn, table):
    cur = conn.cursor()
    nrows = total_rows(conn, table)
    random_id = randrange(nrows)

    cur.execute(f"SELECT id, review_app, review_raw FROM {table} WHERE id={random_id}")
    current_review = cur.fetchone()

    while current_review == None:
        random_id = randrange(nrows)
        cur.execute(f"SELECT id, review_app, review_raw FROM {table} WHERE id={random_id}")
        current_review = cur.fetchone()
    
    return current_review

def total_rows(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT count(*) FROM {table} WHERE is_a11y_human=-1")
    result = cur.fetchone()
    return result[0]