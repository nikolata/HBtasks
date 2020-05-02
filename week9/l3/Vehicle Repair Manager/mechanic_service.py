import sqlite3


def create_mechanic_service():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS mechanic_service(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        mechanic_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY (mechanic_id) REFERENCES mechanic (mechanic_id) ON DELETE CASCADE,
        FOREIGN KEY (service_id) REFERENCES services (id) ON DELETE CASCADE,
        CONSTRAINT ID_HOUR UNIQUE (id)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_mechanic_service(mechanic_id, service_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO mechanic_service (mechanic_id, service_id)
        VALUES (?, ?)
    '''
    cursor.execute(query, (mechanic_id, service_id))
    connection.commit()
    connection.close()
