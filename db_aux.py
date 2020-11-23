import psycopg2 as db
from random import randrange
import random as rand
import datetime
import unidecode
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


def insert_contato(conn, mensagem):
    try:
        cur = conn.cursor()
        query = f"INSERT INTO contato ( \
                registro, \
                nome, \
                email, \
                conteudo \
            ) VALUES (%s, %s, %s, %s)"
        values = (
            datetime.datetime.now(),
            mensagem["nome"],
            mensagem["email"],
            mensagem["conteudo"]
        )
        cur.execute(query, values)
        print("+ Inserting...")
        conn.commit()
    except Exception as err:
        print(err)
        print("- Something get wrong! The contact wasn't registred!")
        raise


# Recebe uma lista de palavras fornecidas pelo usuário e
# as insere na tabela 'a11y_words'
def insert_review_words(conn, id, words):
    for word in words:
        if len(word) > 0:
            word_modified = formatar_palavra_chave(word)
            insert_word(conn, id, word_modified)


# Padroniza as palavras do a11y_words! São removidos acentos 
# ç e convertido para minúsculo
def formatar_palavra_chave(palavra):
    return unidecode.unidecode(palavra).lower()


def update_is_a11y(conn, id, value):
    try:
        cur = conn.cursor()
        query = f"UPDATE reviews_data SET is_a11y_human = (%s) WHERE id = (%s)"
        values = (value, id)
        cur.execute(query, values)
        print("+ Updating human feedback...")
        conn.commit()
    except Exception as err:
        print(err)
        print("- Something get wrong! Update wasn't done!")
        raise


def insert_word(conn, id, word):
    try:
        cur = conn.cursor()
        query = f"INSERT INTO a11y_words ( \
                reviews_data_id, \
                word \
            ) VALUES (%s, %s)"
        values = (
            id,
            word
        )
        cur.execute(query, values)
        print("+ Inserting word...")
        conn.commit()
    except Exception as err:
        print(err)
        print("- Something get wrong! The word wasn't inserted!")
        raise


def search_file(conn, table, id):
    cur = conn.cursor()
    cur.execute(f"SELECT review_app, review_raw FROM {table} WHERE id={id}")
    current_review = cur.fetchone()
    return current_review


# O usuário precisa receber um review que ainda não tenha sido classificado e
# de preferência de maneira aleatória
def random_review(conn, table):
    cur = conn.cursor()
    nrows = max_id(conn, table)
    print(f'nrows = {nrows}')
    random_id = randrange(nrows)

    cur.execute(f"SELECT id, review_app, review_raw FROM {table} WHERE id={random_id} and is_a11y_human=-1")
    current_review = cur.fetchone()

    while current_review == None:
        random_id = randrange(nrows)
        cur.execute(f"SELECT id, review_app, review_raw FROM {table} WHERE id={random_id} and is_a11y_human=-1")
        current_review = cur.fetchone()
    
    return current_review


def max_id(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT max(id) FROM {table}")
    result = cur.fetchone()
    return result[0]
