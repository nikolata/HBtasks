import sqlite3


def create_Mechanic_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS mechanic(
        mechanic_id INTEGER PRIMARY KEY,
        FOREIGN KEY (mechanic_id) REFERENCES user (id) ON DELETE CASCADE
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_mechanic():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    curr_id = 'SELECT MAX(id) FROM user'
    query = '''
    INSERT INTO mechanic (mechanic_id)
        VALUES (?)
    '''
    cursor.execute(curr_id)
    curr_id = cursor.fetchall()
    cursor.execute(query, (curr_id[0][0],))
    connection.commit()
    connection.close()


