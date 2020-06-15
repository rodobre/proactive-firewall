import mysql.connector

def init_connection(password, user='threathunter', database='threats'):
    # Connect to the database
    conn = mysql.connector.connect(user=user, password=password, host='127.0.0.1', port=23305, database=database)

    # Instantiate a cursor
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS THREATS (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    date DATETIME NOT NULL,
                    prediction_type VARCHAR(64) NOT NULL,
                    src VARCHAR(64) NOT NULL,
                    dst VARCHAR(64) NOT NULL,
                    confidence FLOAT NOT NULL)''')

    # Close the cursor
    cursor.close()

    # Commit changes
    conn.commit()

    # Return the connecion
    return conn

def execute_prepared_update(conn, statement, params):
    # Instantiate a cursor
    cursor = conn.cursor()

    # Execute the prepared update
    cursor.execute(statement, params)

    # Close the cursor
    cursor.close()

    # Commit changes
    conn.commit()

def execute_prepared_select(conn, statement, params):
    # Instantiate a cursor
    cursor = conn.cursor()

    # Execute the prepared update
    cursor.execute(statement, params)

    # Get the returned values
    response = cursor.fetchall()

    # Close the cursor
    cursor.close()

    return response