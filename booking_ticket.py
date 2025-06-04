from database import database_of_bus_ticket

def get_bus_info(bus_name):
    """
    Fetches all rows from 'buses' table where bus_name matches the given value.
    Returns a list of dictionaries or an error message.
    """
    try:
        conn, cursor = database_of_bus_ticket()

        cursor.execute("""
            SELECT id, bus_name, seat_type, seat_no, is_book
            FROM buses
            WHERE bus_name = ?
        """, (bus_name,))

        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return f"No buses found with name '{bus_name}'."

        # Optional: Convert to list of dictionaries for readability
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "bus_name": row[1],
                "seat_type": row[2],
                "seat_no": row[3],
                "is_book": bool(row[4])
            })

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None
  

def insert_ticket_booking(bus_name, seat_type, seat_no, payment_taka):
    """
    Inserts a ticket into 'ticket_booking' table only if:
    - bus_name exists in 'buses'
    - the seat (seat_type + seat_no) is not already booked

    Also updates the corresponding seat's is_book to 1.

    Returns a success message or error string.
    """

    try:
        conn, cursor = database_of_bus_ticket()

        if get_bus_info(bus_name=bus_name) is None:
            print("There is no bus")
            return None

        # 2️⃣ Check if seat is available
        cursor.execute("""
            SELECT is_book FROM buses
            WHERE bus_name = ? AND seat_type = ? AND seat_no = ?
        """, (bus_name, seat_type, seat_no))
        seat = cursor.fetchone()

        if seat is None:
            conn.close()
            return f"Error: Seat {seat_no} ({seat_type}) not found for bus '{bus_name}'."

        if seat[0] == 1:
            conn.close()
            return f"Error: Seat {seat_no} ({seat_type}) is already booked."

        # 3️⃣ Insert into ticket_booking
        cursor.execute("""
            INSERT INTO ticket_booking (bus_name, seat_type, seat_no, payment_taka)
            VALUES (?, ?, ?, ?)
        """, (bus_name, seat_type, seat_no, payment_taka))

        # 4️⃣ Update seat to booked
        cursor.execute("""
            UPDATE buses SET is_book = 1
            WHERE bus_name = ? AND seat_type = ? AND seat_no = ?
        """, (bus_name, seat_type, seat_no))

        conn.commit()
        conn.close()
        return f"Ticket booked for {bus_name} bus, seat_type: {seat_type}, seat_no {seat_no} => marked as booked successfully."

    except Exception as e:
        return f"Error: {e}"
