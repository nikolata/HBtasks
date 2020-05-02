import sqlite3
from tabulate import tabulate


def create_hours_table():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS hours(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        type VARCHAR(10) NOT NULL,
        CONSTRAINT ID_TIME UNIQUE (id,time)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_hour():
    ddate = input('Enter date: ')
    hour = input('Enter hour: ')
    type = input('Enter type (busy/free): ')
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO hours (date, time, type)
        VALUES (?, ?, ?)
    '''
    cursor.execute(query, (ddate, hour, type))
    connection.commit()
    connection.close()


def list_all_free_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id, date, time
        FROM hours
            WHERE type == 'free';
    '''
    cursor.execute(query)
    information = cursor.fetchall()
    table = []
    header = ['id', 'date', 'time']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(tup[1])
        temp.append(tup[2])
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()


def list_all_busy_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id, date, time
        FROM hours
            WHERE type == 'busy';
    '''
    cursor.execute(query)
    information = cursor.fetchall()
    table = []
    header = ['id', 'date', 'time']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(tup[1])
        temp.append(tup[2])
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()


def list_free_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id, date, time
        FROM hours
            WHERE type == 'free' AND date == ?;
    '''
    cursor.execute(query, (date,))
    information = cursor.fetchall()
    table = []
    header = ['id', 'date', 'time']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(tup[1])
        temp.append(tup[2])
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()


def list_busy_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id, date, time
        FROM hours
            WHERE type == 'busy' AND date == ?;
    '''
    cursor.execute(query, (date,))
    information = cursor.fetchall()
    table = []
    header = ['id', 'date', 'time']
    for tup in information:
        temp = []
        temp.append(tup[0])
        temp.append(tup[1])
        temp.append(tup[2])
        table.append(temp)
    print(tabulate(table, header, tablefmt="pretty"))
    connection.commit()
    connection.close()


def make_hour_busy(number):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    UPDATE hours
        SET type = 'busy'
            WHERE id = ?
    '''
    cursor.execute(query, (number,))
    connection.commit()
    connection.close()


def make_hour_free(number):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    UPDATE hours
        SET type = 'free'
            WHERE id = ?
    '''
    cursor.execute(query, (number,))
    connection.commit()
    connection.close()


def update_repair_hour(id_number):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT date, time, username, maker, model, bill, hours_id
        FROM vehicle_repair
        JOIN vehicle
        ON vehicle_repair.vehicle_id = vehicle.id
        JOIN hours
        ON vehicle_repair.hours_id = hours.id
        JOIN user
        ON vehicle.client_id = user.id
            WHERE hours_id == ?
    '''
    cursor.execute(query, (id_number,))
    info = cursor.fetchall()
    if len(info) == 0:
        print('YOU DONT HAVE BOOKINGS YET!')
        return
    print(f'''
On {info[0][0]} at {info[0][1]}
Client: {info[0][2]}
Vehicle: {info[0][3]} {info[0][4]}
Current Bill: {info[0][5]}''')
    print('''
Choose one of the following:
1 - change start hour
2 - change bill
3 - return to main menu
        ''')
    decision = int(input())
    if decision == 1:
        list_all_free_hours()
        hour_id = input('Choose hour id: ')
        make_hour_busy(hour_id)
        make_hour_free(info[0][6])
        query = '''
        UPDATE vehicle_repair
        SET hours_id = ?
            WHERE hours_id = ?
        '''
        cursor.execute(query, (hour_id, info[0][6]))
        connection.commit()
        connection.close()
        update_repair_hour(hour_id)
    if decision == 2:
        print(f'Current bill is {info[0][5]}')
        new_bill = input('New bill: ')
        query = '''
        UPDATE vehicle_repair
        SET bill = ?
            WHERE hours_id = ?
        '''
        cursor.execute(query, (new_bill, info[0][6]))
        connection.commit()
        connection.close()
        update_repair_hour(id_number)
    if decision == 3:
        connection.commit()
        connection.close()
        return


def update_repair_hour_for_clients(id_number):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT date, time, username, maker, model, bill, hours_id
        FROM vehicle_repair
        JOIN vehicle
        ON vehicle_repair.vehicle_id = vehicle.id
        JOIN hours
        ON vehicle_repair.hours_id = hours.id
        JOIN user
        ON vehicle.client_id = user.id
            WHERE hours_id == ?
    '''
    cursor.execute(query, (id_number,))
    info = cursor.fetchall()
    print(info)
    print(f'''
On {info[0][0]} at {info[0][1]}
Client: {info[0][2]}
Vehicle: {info[0][3]} {info[0][4]}
Current Bill: {info[0][5]}''')
    print('''
Choose one of the following:
1 - change start hour
2 - return to main menu
        ''')
    decision = int(input())
    if decision == 1:
        list_all_free_hours()
        hour_id = input('Choose hour id: ')
        make_hour_busy(hour_id)
        make_hour_free(info[0][6])
        query = '''
        UPDATE vehicle_repair
        SET hours_id = ?
            WHERE hours_id = ?
        '''
        cursor.execute(query, (hour_id, info[0][6]))
        connection.commit()
        connection.close()
        update_repair_hour_for_clients(hour_id)
    if decision == 2:
        connection.commit()
        connection.close()
        return


# not woriking, it give's me DATABASE IS LOCKED
def delete_repair_hour(hour_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    DELETE FROM vehicle_repair
      WHERE hours_id = ?
    '''
    cursor.execute(query, (hour_id,))
    make_hour_free(hour_id)
    connection.commit()
    connection.close()
