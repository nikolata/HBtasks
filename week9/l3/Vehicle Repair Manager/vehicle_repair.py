import sqlite3


def create_vehicle_repair():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS vehicle_repair(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        vehicle_id INTEGER NOT NULL,
        hours_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        bill INTEGER DEFAULT 0,
        FOREIGN KEY (vehicle_id) REFERENCES vehicle (id) ON DELETE CASCADE,
        FOREIGN KEY (hours_id) REFERENCES hours (id) ON DELETE CASCADE,
        FOREIGN KEY (service_id) REFERENCES services (id) ON DELETE CASCADE,
        CONSTRAINT ID_HOUR UNIQUE (id,hours_id)
    );
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def add_vehicle_repair(vehicle_id, hours_id, service_id):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
    INSERT INTO vehicle_repair (vehicle_id, hours_id, service_id)
        VALUES (?, ?, ?)
    '''
    cursor.execute(query, (vehicle_id, hours_id, service_id))
    connection.commit()
    connection.close()
