# School Management System
## Overview

The School Management System is a web-based application developed using Python and the Django framework.
It is designed to simplify and digitize the administrative and academic tasks within a school environment. 
The system provides two distinct roles—Teacher and Student—each with specific access rights and functionalities, managed through a custom user model. 
This role-based access control ensures that users are provided with only the information and tools necessary for their respective roles.

## Key Features

### 1.	Custom User Model:
The system differentiates between two user types: teachers and students. Each user role has specific capabilities based on their needs within the system.
### 2.	Attendance Management:
Students can mark their attendance for each subject on a daily basis, making the process simple and accessible.<br>
Teachers can view attendance records of students in the subjects they teach, providing a real-time overview of class participation.
### 3.	Subject and Class Management:
Students can view the subjects they are enrolled in, along with the information about the subject teacher.<br>
Teachers can manage their subjects, including adding or removing students from their class lists, and view the total number of students enrolled in each subject.
### 4.	Dashboard for Students and Teachers:
The system features role-specific dashboards, giving students access to their attendance records, subjects, and teacher information, while teachers can view student data, manage class rosters, and track attendance.
### 5.	Security and Access Control:
Role-based permissions ensure that students and teachers only have access to functionalities relevant to their roles.
Teachers cannot access other teachers’ subjects, and students cannot access other students' information.

## Usage
### Login:
Teachers and students must log in to access the system.
### Teacher Actions:
After logging in, teachers will have access to the teacher dashboard where they can manage attendance, subjects, and student enrollment.
### Student Actions:
After logging in, students can mark their attendance, view their attendance records, and see their subjects and assigned teachers.

## Technology Stack
### Python: The core programming language for building the application.
### Django: The web framework used for developing the backend and frontend, along with its built-in ORM for database management.
### SQLite: The default database used for development. However, the system is scalable and can be integrated with databases like PostgreSQL or MySQL for larger-scale deployments.
