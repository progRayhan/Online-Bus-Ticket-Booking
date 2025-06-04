from database import execute_sql

def create_bus_table():
    """
    Creates the 'buses' table in the 'bus_ticket.db' database with a unique bus_name.
    Returns a success message or error string.
    """

    create_bus_sql = """
    CREATE TABLE IF NOT EXISTS buses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_name TEXT NOT NULL,
        seat_type TEXT NOT NULL,
        seat_no INTEGER NOT NULL,
        is_book INTEGER NOT NULL CHECK (is_book IN (0, 1))
    )
    """

    result = execute_sql(create_bus_sql)
    return result


def create_ticket_booking_table():
    """
    Creates the 'ticket_booking' table in the 'bus_ticket.db' database.
    Returns a success message or error string.
    """

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ticket_booking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bus_name TEXT NOT NULL,
        seat_type TEXT NOT NULL,
        seat_no INTEGER NOT NULL,
        payment_taka INTEGER NOT NULL
    )
    """

    result = execute_sql(create_table_sql)
    return result
