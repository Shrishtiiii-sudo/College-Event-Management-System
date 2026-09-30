# Problem Statement

Colleges organize many events throughout the year like tech fests, sports days, 
seminars and cultural events. Managing these events manually (using registers or 
excel sheets) makes it hard to keep track of event details and which students have 
registered for which event. This project aims to solve that problem using a simple 
Python program.

## Scope of the Project

This project is a basic command-line based system for managing college events. It 
allows the admin (or organizer) to add events, view all events, register students 
for events, and view the list of students registered for a particular event. All 
the data is stored in a local SQLite database, so it stays saved even after the 
program is closed.

This project does not include a graphical interface (GUI) since it is meant to be 
run through the terminal.

## Target Users

- College event organizers / faculty who manage events
- Students who want to check event details (through the organizer)

## High-Level Features

- Add a new event with name, date, venue and capacity
- View all events that have been added
- Register a student for a specific event using the event ID
- View all students registered for a specific event
- Data is validated before saving (empty fields, wrong number formats, invalid 
  event IDs are all checked)
- Data is saved permanently using SQLite, so nothing is lost when the program closes