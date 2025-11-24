Project Statement – Student Attendance Management System (CRUD)

1. Problem Statement

Teachers often face difficulty maintaining student attendance using manual registers. Traditional paper-based systems are prone to errors, difficult to update, and lack historical tracking.
This project aims to digitize the attendance process by creating a simple, file-based Python application that allows teachers to add students, mark attendance, view the history, and delete records when necessary.

⸻

2. Scope of the Project

The project includes:
	•	A command-line interface to manage class attendance
	•	Storage of student records using text files without external databases
	•	CRUD operations (Create, Read, Update, Delete)
	•	Ability to mark and view attendance for any date
	•	Support for storing attendance history for the full semester

Not included in the current scope:
	•	GUI interface
	•	Cloud/database integration
	•	Attendance percentage calculation

⸻

3. Target Users

This system is designed for:
	•	Teachers handling class attendance
	•	Students who need a lightweight demo project
	•	Beginners in Python exploring file handling and CRUD logic

⸻

4. High-Level Features
	•	Add new students with name and roll number
	•	Mark attendance (P/A) for the current date
	•	View full attendance history
	•	View attendance of a specific date
	•	Delete a student record
	•	Automatic text-file storage (attendance.txt)
	•	Custom delimiter-based parser/serializer implementation
