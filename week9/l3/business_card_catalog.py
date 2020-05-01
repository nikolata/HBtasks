import sqlite3


def create_user_table():
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
        full_name VARCHAR(20) NOT NULL,
        email VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(15) NOT NULL,
        additional_info TEXT,
        UNIQUE(id, full_name, email)
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add():
    name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    info = input('Enter additional info: ')
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO user (full_name, email, age, phone, additional_info)
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (name, email, age, phone, info))
    connection.commit()
    connection.close()


def list():
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    users_data = cursor.fetchall()
    for l in users_data:
        print(f'ID: {l[0]}, Email: {l[2]}, Full name: {l[1]}')
    connection.commit()
    connection.close()


def get(*, id_num):
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = 'SELECT * FROM user WHERE id == ?'
    cursor.execute(query, (id_num,))
    users_data = cursor.fetchall()
    print(f'''
        ##############
        Id: {users_data[0][0]},
        Full name: {users_data[0][1]},
        Email: {users_data[0][2]},
        Age: {users_data[0][3]},
        Phone: {users_data[0][4]},
        Additional info: {users_data[0][5]}
        #############
        ''')
    connection.commit()
    connection.close()


def delete(*, id_num):
    connection = sqlite3.connect('catalog.db')
    cursor = connection.cursor()
    query = 'SELECT * FROM user WHERE id == ?'
    cursor.execute(query, (id_num,))
    users_data = cursor.fetchall()
    print(f'Following contact is deleted successfully: ')
    print(f'''
        ################
        Id: {users_data[0][0]},
        Full name: {users_data[0][1]},
        Email: {users_data[0][2]},
        Age: {users_data[0][3]},
        Phone: {users_data[0][4]},
        Additional info: {users_data[0][5]}
        ###############
        ''')

    query = 'DELETE FROM user WHERE id == ?'
    cursor.execute(query, (id_num,))
    connection.commit()
    connection.close()


def main():
    create_user_table()
    s = 'Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)'
    print(s)
    while True:
        command = input('Enter command: ')
        if command == 'help':
            print('''
                #################
                #####OPTIONS#####
                #################

                `add` - insert new business card
                `list` - list all business cards
                `delete` - delete a certain business card (`ID` is required)
                `get` - display full information for a certain business card (`ID` is required)
                `help` - list all available options
                ''')
        elif command == 'add':
            add()
        elif command == 'list':
            list()
        elif command == 'get':
            num = input("Enter ID number: ")
            get(id_num=num)
        elif command == 'delete':
            num = input("Enter ID number: ")
            delete(id_num=num)
        else:
            print('WRONG COMMAND!!! TRY AGAIN!!!')


if __name__ == '__main__':
    main()
