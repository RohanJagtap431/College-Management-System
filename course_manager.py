class CourseManager:
    def __init__(self, db):
        self.db = db
        
    def add_course(self):
        course_name = input("Enter Course Name: ").strip()
        if course_name == "":
            print("Invalid Course ! Try Again")
            return
        
        query = "SELECT * FROM Courses WHERE course_name = %s"
        
        self.db.cur.execute(query, (course_name,))
        
        record = self.db.cur.fetchone()
        if record:
            print("Name Already Exists")
            return
                    
                    
        duration = input("Enter Your Duration: ").strip()
        if not duration.isdigit() or int(duration) <= 0:
            print("Invalid Duration!")
            return
        
        
        fees = input("Enter Your Fees: ")
        if not fees.isdigit() or int(fees) <= 0:
            print("Invalid Fees!")
            return
        
        duration = int(duration)
        fees = int(fees)
        
        query = '''INSERT INTO Courses
                    (course_name, duration, fees)
                    VALUES
                    (%s, %s, %s)'''
                    
        self.db.cur.execute(
            query,
            (course_name, duration, fees)
        )
        self.db.con.commit()
        print("Course Added Successfully")

    def view_courses(self):
        query = "SELECT * FROM Courses"
        
        self.db.cur.execute(query)
        
        courses = self.db.cur.fetchall()
        if not courses:
            print("Course Not Found!")
            return
            
        for course in courses:
            print(f"ID: {course[0]}")
            print(f"Course Name: {course[1]}")
            print(f"Duration: {course[2]}")
            print(f"Fees: {course[3]}")
            
    def search_course(self):
        course_id = input("Enter Your Course ID: ")
        
        if not course_id.isdigit():
            print("Invalid Course ID")
            return
        
        course_id = int(course_id)
        
        query = "SELECT * FROM Courses WHERE course_id = %s"
        
        self.db.cur.execute(query,(course_id,))
        
        course = self.db.cur.fetchone()
        
        if not course:
            print("Course Not Found")
            return
        
        print(f"Id: {course[0]}")
        print(f"Course Name: {course[1]}")
        print(f"Duration: {course[2]}")
        print(f"Fees: {course[3]}")
        
    def update_course(self):
        course_id = input("Enter Your Course ID: ")
        if not course_id.isdigit():
            print("Invalid Course Id")
            return
        
        course_id = int(course_id)
        
        query = '''SELECT * FROM Courses 
                    WHERE course_id = %s'''
                    
        self.db.cur.execute(query, (course_id,))
        
        course = self.db.cur.fetchone()
        if not course:
            print("Course Not Found")
            return
        
        name = input("Enter New Name: ").strip()
        if name =="":
            print("Invalid Name! Try Again")
            return
        
        query = '''SELECT * FROM Courses
                    WHERE course_name = %s
                    AND course_id != %s
                '''
                
        self.db.cur.execute(query, (name, course_id))
        record = self.db.cur.fetchone()
        
        if record:
            print("Course Name Already Exist")
            return
        
        duration = input("Enter New Duration: ").strip()
        if not duration.isdigit():
            print("Invalid Duration")
            return
        duration = int(duration)
        if duration <= 0:
            print("Invalid Duration")
            return
        
        fees = input("Enter New Fees: ").strip()
        if not fees.isdigit():
            print("Invalid Fees")
            return
        fees = int(fees)
        if fees <= 0:
             print("Invalid Fees")
             return
        
        query = '''UPDATE Courses
                   SET
                   course_name = %s,
                   duration = %s,
                   fees = %s
                   WHERE course_id = %s
                   '''
                   
        self.db.cur.execute(query, (name, duration, fees, course_id))
        self.db.con.commit()
        print("Course Updated Successfully")
        
    def delete_course(self):
        course_id = input("Enter Course ID: ")
        if not course_id.isdigit():
            print("Invalid Course Id")
            return
        course_id = int(course_id)
        
        query = '''SELECT * FROM Courses
                WHERE course_id = %s'''
                
        self.db.cur.execute(query, (course_id,))
        
        course = self.db.cur.fetchone()
        if not course:
            print("Course Not Found")
            return
        
        print(f"Course Found: {course[1]}")
        
        confirm = input("Are you sure you want to delete? (y/n): ").lower()
        if confirm != "y":
            print("Delete Cancelled")
            return
        
        query = '''DELETE FROM Courses
                    WHERE course_id = %s'''
                    
        self.db.cur.execute(query, (course_id,))
        self.db.con.commit()
        
        print("Course Deleted Successfully")
        
        
        
        
        