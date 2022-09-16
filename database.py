# DB Management
import sqlite3

# Banco de dado informações usuários
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


# DB  Functions
# Tabela dos usuários
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')


def delete_userstable():
    c.execute(
        'DROP TABLE IF EXISTS usertable')


def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username, password) VALUES (?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data


