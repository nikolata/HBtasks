import sqlite3
from baseUser import add_user
from client import add_client
from mechanic import add_mechanic


def check_if_user_is_in_the_system(username):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT *
      FROM user
        WHERE username == ?
    '''
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(data) == 0:
        return False
    return True


def create_user_if_not_in_the_system():
    answer = input('Would you like to create new user? [yes/no]: ')
    if answer != 'yes':
        return False
    user_type = input('Are you a Client or Mechanic? ')
    if user_type == 'Client':
        add_user('Client')
        add_client()
    elif user_type == 'Mechanic':
        add_user('Mechanic')
        add_mechanic()
    return True

def get_user_type(username=None):
    if username is None:
        connection = sqlite3.connect('vehicle_management.db')
        cursor = connection.cursor()
        query = '''
        SELECT type
          FROM user
            ORDER BY id desc LIMIT 1
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data[0][0]
    if username is not None:
        connection = sqlite3.connect('vehicle_management.db')
        cursor = connection.cursor()
        query = '''
        SELECT type
          FROM user
            WHERE username = ?
        '''
        cursor.execute(query, (username,))
        data = cursor.fetchall()
        connection.commit()
        connection.close()
        return data[0][0]


def display_menu_for_client():
    print('''
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
save_repair_hour <hour_id>
update_repair_hour <hour_id>
delete_repair_hour <hour_id>
add_vehicle
update_vehicle <vehicle_id>
delete_vehicle <vehicle_id>
exit
''')


def display_menu_for_mechanic():
    print('''
You can choose from the following commands:
list_all_free_hours
list_free_hours <date>
list_all_busy_hours
list_busy_hours <date>
add_new_repair_hour
add_new_service
update_repair_hour <hour_id>
exit
''')


def get_mechanic_id(username):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id
      FROM user
        WHERE username = ?
    '''
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data[0][0]


def get_service_id():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id
      FROM services
        ORDER BY id desc LIMIT 1
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data[0][0]


def get_username():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT username
      FROM user
        ORDER BY id desc LIMIT 1
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data[0][0]


def get_id_from_username(username):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    SELECT id
      FROM user
        WHERE username == ?
    '''
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data[0][0]

print(get_username())