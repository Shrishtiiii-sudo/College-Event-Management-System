from modules.database import db, cur

def register_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    event_id_text = input("Enter event ID: ")

    if name.strip() == "" or roll.strip() == "":
        print("Name and roll number cannot be empty.")
        return

    if not event_id_text.isdigit():
        print("Event ID must be a number.")
        return

    event_id = int(event_id_text)

    cur.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = cur.fetchone()

    if event is None:
        print("No event found with that ID.")
        return

    cur.execute("INSERT INTO students (name, roll) VALUES (?, ?)", (name, roll))
    student_id = cur.lastrowid

    cur.execute("INSERT INTO registrations (event_id, student_id) VALUES (?, ?)", (event_id, student_id))
    db.commit()
    print("Student registered!")

def view_registrations():
    event_id_text = input("Enter event ID: ")

    if not event_id_text.isdigit():
        print("Event ID must be a number.")
        return

    event_id = int(event_id_text)

    cur.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = cur.fetchone()

    if event is None:
        print("No event found with that ID.")
        return

    cur.execute("SELECT students.name, students.roll FROM students JOIN registrations ON students.id = registrations.student_id WHERE registrations.event_id = ?", (event_id,))
    result = cur.fetchall()

    if len(result) == 0:
        print("No students registered for this event.")
    else:
        for row in result:
            print("Name:", row[0], "| Roll:", row[1])