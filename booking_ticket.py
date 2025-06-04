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
        return f"Error: {e}"
  
