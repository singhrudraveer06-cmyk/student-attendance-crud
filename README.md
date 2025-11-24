# Student Attendance Management System (CRUD)

This is a simple *Command-Line Based Student Attendance Application* built as part of the *VITyarthi Course Project*.

The project implements complete *CRUD operations*:
- *Create* – Add a new student  
- *Read* – View student list & view attendance  
- *Update* – Mark attendance  
- *Delete* – Delete student  

All data is stored in a simple *attendance.txt* file.

---

## Project Details

*Course:* Python Programming  
*Student Name:* Rudraveer Singh  
*Registration Number:* 25BCE10659  
*Project Type:* CLI-based CRUD Application  
*Semester:* 1st Semester  

---

## Features Implemented

###  Add New Student  
Stores:
- Name  
- Roll number  

###  Mark Attendance  
Marks *P (Present)* or *A (Absent)* for today's date.

###  View Attendance  
- View full attendance report  
- View attendance on a specific date  

###  Show All Students  
List all registered students

###  Delete Student  
removes a student by roll number

###  File-Based Storage  
Data is saved in:
`attendance.txt`  
(Automatically created when the program runs)

---

## 📁 Project Structure
├── attendance.py          # Main application file
├── attendance.txt         # Auto-generated storage file
├── screenshots/           # Screenshots for demonstration
│     ├── 1.png
│     ├── 2.png
│     └── ...
├── statement.md           # Problem, scope & features (required)
└── README.md              # Project documentation

### Technologies Used
	•	Python 3
	•	File handling (open, read, write)
	•	Date handling (datetime.date)
	•	Custom delimiter-based data parsing
