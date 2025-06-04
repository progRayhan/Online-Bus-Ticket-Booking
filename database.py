import sqlite3

def database_of_bus_ticket():
    """
    Establishes a connection to the 'bus_ticket.db' SQLite database and
    returns both the connection and cursor objects.
    """

    db_conn = sqlite3.connect("bus_ticket.db")
    cursor = db_conn.cursor()

    return db_conn, cursor


def execute_sql(sql_query, params=None):
    """
    Executes a given SQL query using the bus_ticket.db connection.
    """

    try:
        db_conn, cursor = database_of_bus_ticket()

        if params:
            cursor.executemany(sql_query, params)
        else:
            cursor.execute(sql_query)

        db_conn.commit()
        db_conn.close()
        return "Query executed successfully"
    except Exception as e:
        return f"Error: {e}"
    