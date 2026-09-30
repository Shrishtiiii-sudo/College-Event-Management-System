from modules import database
from modules import event_functions
from modules import student_functions


while True:
    print("\n===== EVENT MANAGER =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Register Student")
    print("4. View Registrations")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event_functions.add_event()

    elif choice == "2":
        event_functions.view_events()

    elif choice == "3":
        student_functions.register_student()

    elif choice == "4":
        student_functions.view_registrations()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
