class FacultyManager:
    def __init__(self, db):
        self.db = db
    
    def add_faculty(self):
        faculty_name = input("Enter Faculty Name: ").strip()
        if faculty_name == "":
            print("Invalid Faculty Name")
            return
        
        email = input("Enter Email: ").strip()
        if email == "":
            print("Invalid Email")
            return
        query = '''SELECT * FROM Faculty
                   WHERE email = %s'''
        self.db.cur.execute(query, (email,))
        record = self.db.cur.fetchone()
        if record:
            print("Email Already Exists")
            return
        
        
        query = '''INSERT INTO Faculty
                   (faculty_name, email)
                   VALUES
                   (%s, %s)'''
        self.db.cur.execute(query, (faculty_name, email))
        self.db.con.commit()
        print("Faculty Added Successfully")
    
    def view_faculty(self):
        query = "SELECT * FROM Faculty"  
        self.db.cur.execute(query)
        records = self.db.cur.fetchall()
        if not records:
            print("Faculty Not Found")
            return
        for record in records:
            print()
            print(f"Faculty Id: {record[0]}")
            print(f"Faculty Name: {record[1]}")
            print(f"Faculty Email: {record[2]}")  
            print()
            
    def search_faculty(self):
        faculty_id = input("Enter Faculty Id: ").strip()
        if not faculty_id.isdigit():
            print("Invalid Faculty Id")
            return
        faculty_id = int(faculty_id)
        
        query = '''SELECT * FROM Faculty
                   WHERE faculty_id = %s'''
        self.db.cur.execute(query, (faculty_id,))
        faculty = self.db.cur.fetchone()
        if not faculty:
            print("Faculty Not Found")
            return
        print()
        print(f"Faculty Name: {faculty[1]}")
        print(f"Faculty Email: {faculty[2]}")
        print()
        
    def delete_faculty(self):
        faculty_id = input("Enter Faculty ID: ").strip()
        if not faculty_id.isdigit():
            print("Invalid ID")
            return
        faculty_id = int(faculty_id)
        
        query = '''SELECT * FROM Faculty
                   WHERE faculty_id = %s'''
        self.db.cur.execute(query, (faculty_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Faculty Not Found")
            return
        
        print(f"Faculty Found: {record[1]}")
        confirm = input("Are you sure you want to delete? (y/n): ").lower()
        if confirm != "y":
            print("Delete Cancelled")
            return
        
        query = '''DELETE FROM Faculty
                   WHERE faculty_id = %s'''
        self.db.cur.execute(query, (faculty_id,))
        self.db.con.commit()
        print("Faculty Deleted Successfully!")
        
    def update_faculty(self):
        faculty_id = input("Enter Faculty ID: ").strip()
        if not faculty_id.isdigit():
            print("Invalid Input")
            return
        faculty_id = int(faculty_id)
        
        query = '''SELECT * FROM Faculty
                   WHERE faculty_id = %s'''
        self.db.cur.execute(query, (faculty_id,))
        record = self.db.cur.fetchone()
        
        if not record:
            print("Faculty Not Found")
            return
        
        faculty_name = input("Enter Faculty Name: ").strip()
        if faculty_name == "":
            print("Invalid Faculty Name")
            return
        
        email = input("Enter Email: ").strip()
        if email == "":
            print("Invalid Email")
            return
        query = '''SELECT * FROM Faculty
                   WHERE email = %s
                   AND faculty_id != %s'''
        self.db.cur.execute(query, (email, faculty_id))
        record = self.db.cur.fetchone()
        if record:
            print("Email Already Exists")
            return
        
        query = '''UPDATE Faculty
                   SET
                   faculty_name = %s,
                   email = %s
                   WHERE faculty_id = %s'''
        self.db.cur.execute(query, (faculty_name, email, faculty_id))
        self.db.con.commit()
        print("Faculty Updated Successfully")