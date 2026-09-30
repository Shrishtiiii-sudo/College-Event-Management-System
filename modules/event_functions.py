from modules.database import db, cur

def add_event():
    name = input("Enter event name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    venue = input("Enter venue: ")
    capacity_text = input("Enter capacity: ")

    if name.strip() == "":
        print("Event name cannot be empty.")
        return

    if not capacity_text.isdigit():
        print("Capacity must be a number.")
        return

    capacity = int(capacity_text)

    cur.execute("INSERT INTO events (name, date, venue, capacity) VALUES (?, ?, ?, ?)", (name, date, venue, capacity))
    db.commit()
    print("Event added!")

def view_events():
    cur.execute("SELECT * FROM events")
    all_events = cur.fetchall()

    if len(all_events) == 0:
        print("No events yet.")
    else:
        for event in all_events:
            print("ID:", event[0])
            print("Name:", event[1])
            print("Date:", event[2])
            print("Venue:", event[3])
            print("Capacity:", event[4])
            print("------")