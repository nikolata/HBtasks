import sqlite3
from tabulate import tabulate


def create_Service_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS services(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        service VARCHAR(50),
        CONSTRAINT id_service UNIQUE(id, service)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_service():
    print('Provide New service name:')
    service = input()
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO services (service)
        VALUES (?)
    '''
    cursor.execute(query, (service,))
    connection.commit()
    connection.close()


def list_all_services():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id, service
        FROM services
    '''
    cursor.execute(query)
    information = cursor.fetchall()
    table = []
    header = ['id', 'Services']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(tup[1])
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()
