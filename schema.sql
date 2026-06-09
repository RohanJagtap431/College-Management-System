CREATE DATABASE collage_management;
USE collage_management;

CREATE TABLE Students(
	student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    phone VARCHAR(10),
    department VARCHAR(200),
    admission_date DATE
);

CREATE TABLE Courses(
	course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(200) UNIQUE NOT NULL,
    duration INT,
    fees INT
);

CREATE TABLE Faculty(
	faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    faculty_name VARCHAR(200)  NOT NULL,
	email VARCHAR(200) UNIQUE NOT NULL
);

CREATE TABLE Enrollments(
	enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    UNIQUE(student_id, course_id)
);

CREATE TABLE Payments(
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    amount INT NOT NULL,
    payment_date DATE,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

CREATE TABLE Admins(
	admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(200) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

