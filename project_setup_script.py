from database import execute_sql
from create_db_tables import create_bus_table, create_ticket_booking_table

def seed_bus_data():
    """
    Inserts 50 rows of bus data for 'Midline123' into the buses table.
    10 Female seats, 40 Male seats.
    """

    insert_sql = """
    INSERT INTO buses (bus_name, seat_type, seat_no, is_book)
    VALUES (?, ?, ?, ?)
    """

    bus_name = "Midline123"
    is_book = 0  # False

    data = []

    # Female seats: 1-10
    for seat_no in range(1, 11):
        data.append((bus_name, "Female", seat_no, is_book))

    # Male seats: 1-40
    for seat_no in range(1, 41):
        data.append((bus_name, "Male", seat_no, is_book))

    return execute_sql(insert_sql, data)

create_bus = create_bus_table()
seed_bus = seed_bus_data()
create_ticket_table = create_ticket_booking_table()
