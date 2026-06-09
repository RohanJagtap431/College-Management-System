class StudentManager:
    def __init__(self, db):
        self.db = db
        
    def add_student(self):
        name = input("Enter Your Name: ").strip()
        if name == "":
            print("Invalid Name! try again")
            return
        
        email = input("Enter email: ").strip()

        if email == "":
            print("Invalid Email! Try Again")
            return

        query = "SELECT * FROM Students WHERE email = %s"
        self.db.cur.execute(query, (email,))

        record = self.db.cur.fetchone()

        if record:
            print("Email already exists")
            return
        
        phone = input("Enter Phone Number: ").strip()
        if len(phone) != 10 or not phone.isdigit():
            print("Invalid Phone Number")
            return
        
        department = input("Enter Department: ").strip()

        if department == "":
            print("Invalid Department")
            return
        
        query = '''INSERT INTO Students
                    (name, email, phone, department, admission_date)
                    VALUES
                    (%s, %s, %s, %s, CURDATE())'''
                    
        self.db.cur.execute(
            query,
            (name, email, phone, department)
        )
        self.db.con.commit()
        print("Student Added Successfully")
        
    def view_all_students(self):
        query = "SELECT * FROM Students"
        self.db.cur.execute(query)
        
        students = self.db.cur.fetchall()
        
        if not students:
                print("No Students Found")
                return
            
        for student in students:
            print("ID: ",student[0])
            print("Name: ",student[1])
            print("Email: ",student[2])
            print("Phone: ",student[3])
            print("Department: ",student[4])
            print("Admission Date:", student[5])
            print()
            print()
            
    def search_student(self):
        student_id = input("Enter Student ID: ")
        
        if not student_id.isdigit():
            print("Invalid Student ID")
            return
        
        query = '''SELECT * FROM Students
                    WHERE student_id = %s'''
                    
        self.db.cur.execute(query, (student_id,))
        
        student = self.db.cur.fetchone()
        if not student:
            print("Student Not Found")
            return
        
        print("ID:", student[0])
        print("Email:", student[2])
        print("Name:", student[1])
        print("Phone:", student[3])
        print("Department:", student[4])
        print("Admission Date:", student[5])
        
    def update_student(self):
        student_id = input("Enter Student ID: ")

        if not student_id.isdigit():
            print("Invalid Student ID")
            return

        student_id = int(student_id)

        query = """
                SELECT * FROM Students
                WHERE student_id = %s
                """

        self.db.cur.execute(query, (student_id,))

        student = self.db.cur.fetchone()

        if not student:
            print("Student Not Found")
            return
        
        name = input("Enter Your Name: ").strip()
        if name == "":
            print("Invalid Name! try again")
            return
        
        email = input("Enter email: ").strip()

        if email == "":
            print("Invalid Email! Try Again")
            return

        query = '''SELECT * FROM Students
                    WHERE email = %s
                    AND student_id != %s
                '''
                
        self.db.cur.execute(query, (email, student_id))

        record = self.db.cur.fetchone()

        if record:
            print("Email already exists")
            return
        
        phone = input("Enter Phone Number: ").strip()
        if len(phone) != 10 or not phone.isdigit():
            print("Invalid Phone Number")
            return
        
        department = input("Enter Department: ").strip()

        if department == "":
            print("Invalid Department")
            return
        
        query = '''UPDATE Students
                   SET
                   name = %s,
                   email = %s,
                   phone = %s,
                   department = %s
                WHERE student_id = %s'''
                    
        self.db.cur.execute(
            query,
            (name, email, phone, department, student_id)
        )
        self.db.con.commit()
        print("Student Updated Successfully")
        
    def delete_student(self):
        student_id = input("Enter Student ID: ")

        if not student_id.isdigit():
            print("Invalid Student ID")
            return

        student_id = int(student_id)

        query = """
            SELECT * FROM Students
            WHERE student_id = %s
            """

        self.db.cur.execute(query, (student_id,))
        student = self.db.cur.fetchone()

        if not student:
            print("Student Not Found")
            return

        print("Student Found:", student[1])

        confirm = input("Are you sure you want to delete? (y/n): ").lower()

        if confirm != "y":
            print("Delete Cancelled")
            return

        query = """
                DELETE FROM Students
                WHERE student_id = %s
                """

        self.db.cur.execute(query, (student_id,))
        self.db.con.commit()

        print("Student Deleted Successfully")
        
    