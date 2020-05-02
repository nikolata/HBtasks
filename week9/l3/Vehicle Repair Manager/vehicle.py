import sqlite3
from tabulate import tabulate


def create_Vehicle_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS vehicle(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        category VARCHAR(20) NOT NULL,
        maker VARCHAR(20) NOT NULL,
        model VARCHAR(20) NOT NULL,
        reg_number VARCHAR(10) NOT NULL,
        gear_box VARCHAR(10) NOT NULL,
        client_id INTEGER,
        FOREIGN KEY (client_id) REFERENCES client (client_id) ON DELETE CASCADE
        CONSTRAINT ID_REGNUM UNIQUE (id,reg_number)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_vehicle(client_id):
    category = input('Enter category: ')
    maker = input('Enter maker: ')
    model = input('Enter model: ')
    reg_number = input('Enter reg_number: ')
    gear_box = input('Enter gear_box: ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO vehicle (category, maker, model, reg_number, gear_box, client_id)
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (category, maker, model, reg_number, gear_box, client_id))
    connection.commit()
    connection.close()


def list_all_vehicles(user_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT *
        FROM vehicle
          WHERE client_id == ?
    '''
    cursor.execute(query, (user_id,))
    information = cursor.fetchall()
    table = []
    header = ['id', 'Vehicles']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(f'{tup[2]} {tup[3]} with RegNumer: {tup[4]}')
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()


def update_vehicle(vehicle_id):
    category = input('Enter category: ')
    maker = input('Enter maker: ')
    model = input('Enter model: ')
    reg_number = input('Enter reg_number: ')
    gear_box = input('Enter gear_box: ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    UPDATE vehicle
    SET category = ?, maker = ?, model = ?, reg_number = ?, gear_box = ?
    WHERE id == ?
    '''
    cursor.execute(query, (category, maker, model, reg_number, gear_box, vehicle_id))
    connection.commit()
    connection.close()


def delete_vehicle(vehicle_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    DELETE FROM vehicle
    WHERE id == ?
    '''
    cursor.execute(query, (vehicle_id))
    connection.commit()
    connection.close()
