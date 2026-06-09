class EnrollmentManager:
    def __init__(self, db):
        self.db = db
        
    def enroll_student(self):
        student_id = input("Enter Student Id: ")
        if not student_id.isdigit():
            print("Invalid Student ID")
            return
        student_id = int(student_id)
        
        query = "SELECT * FROM Students WHERE student_id = %s"
        
        self.db.cur.execute(query, (student_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Student Not Found")
            return
        
        course_id = input("Enter Course Id: ")
        if not course_id.isdigit():
            print("Invalid Course ID")
            return
        course_id = int(course_id)
        
        query = "SELECT * FROM Courses WHERE course_id = %s"
        
        self.db.cur.execute(query, (course_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Course Not Found")
            return
        
        query = "SELECT * FROM Enrollments WHERE student_id = %s AND course_id = %s"
        self.db.cur.execute(query, (student_id, course_id))
        record = self.db.cur.fetchone()
        
        if record:
            print("Student Already Enrolled In This Course")
            return
        
        query = '''INSERT INTO Enrollments
                    (student_id, course_id, enrollment_date)
                    VALUES
                    (%s, %s, CURDATE())'''
                    
        self.db.cur.execute(query, (student_id, course_id))
        
        self.db.con.commit()
        print("Student Enrolled Successfully")
        
    def view_enrollments(self):
        query = "SELECT * FROM Enrollments"
        self.db.cur.execute(query)
        
        enrollments = self.db.cur.fetchall()
        
        if not enrollments:
            print("No Enrollments Found")
            return
        
        for enrollment in enrollments:
            print(f"Enrollment ID: {enrollment[0]}")
            print(f"Student ID: {enrollment[1]}")
            print(f"Course ID: {enrollment[2]}")
            print(f"Enrollment Date: {enrollment[3]}")
        
    def search_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")
        if not enrollment_id.isdigit():
            print("Invalid Enrollment ID")
            return
        enrollment_id = int(enrollment_id)
        
        query = "SELECT * FROM Enrollments WHERE enrollment_id = %s"
        
        self.db.cur.execute(query, (enrollment_id,))
        
        enrollment = self.db.cur.fetchone()
        if not enrollment:
            print("Enrollment Not Found")
            return

        print(f"Enrollment ID: {enrollment[0]}")
        print(f"Student ID: {enrollment[1]}")
        print(f"Course ID: {enrollment[2]}")
        print(f"Enrollment Date: {enrollment[3]}")
            
    def delete_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")
        
        if not enrollment_id.isdigit():
            print("Invalid Enrollment ID")
            return
        
        enrollment_id = int(enrollment_id)
        
        query = "SELECT * FROM Enrollments WHERE enrollment_id = %s"
        
        self.db.cur.execute(query, (enrollment_id,))
        enrollment = self.db.cur.fetchone()
        
        if not enrollment:
            print("Enrollment Not Found")
            return
        
        print(f"Enrollment Found: {enrollment[0]}")  
        
        confirm = input("Are you sure you want to delete? (y/n):").lower()
        
        if confirm != "y":
            print("Delete Cancelled")
            return
        
        query = '''DELETE FROM Enrollments 
                   WHERE enrollment_id = %s'''
                   
        self.db.cur.execute(query, (enrollment_id,))
        self.db.con.commit()
        
        print("Enrollment Deleted Successfully")
            
    def update_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")
        if not enrollment_id.isdigit():
            print("Invalid Enrollment ID")
            return
        enrollment_id = int(enrollment_id)
        
        query = "SELECT * FROM Enrollments WHERE enrollment_id = %s"
        
        self.db.cur.execute(query, (enrollment_id,))
        enrollments = self.db.cur.fetchone()
        
        if not enrollments:
            print("Enrollment Not Found")
            return
        
        student_id = input("Enter New Student ID: ").strip()
        if not student_id.isdigit():
            print("Invalid Student ID")
            return
        student_id = int(student_id)
        
        query = "SELECT * FROM Students WHERE student_id = %s"
        self.db.cur.execute(query, (student_id,))
        record = self.db.cur.fetchone()
        if not record:
            print("Student Not Found")
            return
        
        
        course_id = input("Enter Course ID").strip()
        if not course_id.isdigit():
            print("Invalid Course ID")
            return
        course_id = int(course_id)
        
        query = "SELECT * FROM Courses WHERE course_id = %s"
        self.db.cur.execute(query, (course_id,))
        record = self.db.cur.fetchone()
        if not record:
            print("Course Not Found")
            return
        
        query = """
                SELECT * FROM Enrollments
                WHERE student_id = %s
                AND course_id = %s
                AND enrollment_id != %s
            """

        self.db.cur.execute(
            query,
            (student_id, course_id, enrollment_id)
        )

        record = self.db.cur.fetchone()

        if record:
            print("Student Already Enrolled In This Course")
            return
        
        
        query = '''UPDATE Enrollments
                   SET
                   student_id = %s,
                   course_id = %s
                   WHERE enrollment_id = %s'''
                   
        self.db.cur.execute(query, (student_id, course_id, enrollment_id))
        self.db.con.commit()
        
        print("Enrollment Updated Successfully")
        
        