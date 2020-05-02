import sqlite3


def create_BaseUser_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
        username VARCHAR(20) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        email VARCHAR(50) NOT NULL,
        adress VARCHAR(50) NOT NULL,
        type VARCHAR(10),
        CONSTRAINT USER_C UNIQUE(id, username, phone, email)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_user(type):
    username = input('Enter user name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    adress = input('Enter adress: ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO user (username, phone, email, adress, type)
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (username, phone, email, adress, type))
    connection.commit()
    connection.close()
